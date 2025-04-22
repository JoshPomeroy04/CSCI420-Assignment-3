# Zero-shot Prompting

## Input
    Convert the data class to a REST API using Ktor:

    data class Product ( val id : Int , val name : String , val price : Double )
    // TODO : Create GET and POST endpoints using Ktor 

## Output
```kotlin
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

@Serializable
data class Product(val id: Int, val name: String, val price: Double)

val products = mutableListOf<Product>(
    Product(1, "Laptop", 1200.00),
    Product(2, "Mouse", 25.00)
)

fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/products") {
                call.respond(HttpStatusCode.OK, products)
            }

            get("/products/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid product ID")
                    return@get
                }
                val product = products.find { it.id == id }
                if (product != null) {
                    call.respond(HttpStatusCode.OK, product)
                } else {
                    call.respond(HttpStatusCode.NotFound, "Product not found")
                }
            }

            post("/products") {
                try {
                    val product = call.receive<Product>()
                    products.add(product)
                    call.respond(HttpStatusCode.Created, product)
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid product data")
                }
            }
        }
    }.start(wait = true)
}
```

Here's a breakdown of the Ktor implementation:

1.  **Dependencies:** Make sure you have the necessary Ktor dependencies in your `build.gradle` (or `pom.xml` for Maven) file:
    ```gradle
    implementation("io.ktor.server:ktor-server-core-jvm:2.3.10")
    implementation("io.ktor.server:ktor-server-netty-jvm:2.3.10")
    implementation("io.ktor.server:ktor-server-content-negotiation-jvm:2.3.10")
    implementation("io.ktor.serialization:ktor-serialization-kotlinx-json-jvm:2.3.10")
    ```
    Replace `2.3.10` with the latest stable Ktor version if needed.

2.  **Serialization:** The `@Serializable` annotation from `kotlinx.serialization` makes the `Product` data class serializable and deserializable, which is essential for handling JSON in the API.

3.  **`products` List:** A mutable list `products` is created to store the `Product` objects in memory for this example. In a real-world application, you would typically interact with a database.

4.  **`embeddedServer`:** This sets up an embedded Netty server on port 8080.

5.  **`routing` Block:** This defines the API endpoints:
    * **`get("/products")`:**
        * This endpoint handles GET requests to `/products`.
        * It responds with an HTTP status code `OK` (200) and the entire `products` list as a JSON array.
    * **`get("/products/{id}")`:**
        * This endpoint handles GET requests to `/products/{id}`, where `{id}` is a path parameter.
        * It extracts the `id` from the URL using `call.parameters["id"]`.
        * It attempts to convert the `id` to an integer. If it fails, it responds with `BadRequest` (400).
        * It searches the `products` list for a product with the matching `id`.
        * If found, it responds with `OK` (200) and the `Product` object as JSON.
        * If not found, it responds with `NotFound` (404).
    * **`post("/products")`:**
        * This endpoint handles POST requests to `/products`.
        * It uses `call.receive<Product>()` to deserialize the JSON request body into a `Product` object. This requires the `ContentNegotiation` feature to be installed (which is done implicitly when you include the serialization dependency).
        * It adds the received `Product` to the `products` list.
        * It responds with `Created` (201) and the newly created `Product` object in the response body.
        * It includes a `try-catch` block to handle potential `BadRequest` (400) if the request body is not valid JSON or cannot be deserialized into a `Product`.

**To run this API:**

1.  Save the code as a `.kt` file (e.g., `ProductApi.kt`).
2.  Make sure you have Kotlin and Gradle (or Maven) set up.
3.  Build and run the application using Gradle (e.g., `./gradlew run`).

**How to test the API:**

You can use tools like `curl`, Postman, or Insomnia to interact with the API:

* **GET all products:**
    ```bash
    curl http://localhost:8080/products
    ```
    Response (example):
    ```json
    [{"id":1,"name":"Laptop","price":1200.0},{"id":2,"name":"Mouse","price":25.0}]
    ```

* **GET a specific product by ID:**
    ```bash
    curl http://localhost:8080/products/1
    ```
    Response:
    ```json
    {"id":1,"name":"Laptop","price":1200.0}
    ```

* **POST a new product:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"id":3,"name":"Keyboard","price":75.0}' http://localhost:8080/products
    ```
    Response:
    ```json
    {"id":3,"name":"Keyboard","price":75.0}
    ```

This provides a basic REST API for your `Product` data class using Ktor. Remember that this is an in-memory implementation. For a production application, you would need to integrate with a persistent data store.


# Chain-of-Thoughts Prompting

## Input 
    Step by step, convert the data class to a REST API using Ktor:

    data class Product ( val id : Int , val name : String , val price : Double )
    // TODO : Create GET and POST endpoints using Ktor 

## Output
Okay, let's walk through the conversion of your `Product` data class into a REST API using Ktor step by step.

**Step 1: Set up your Ktor project.**

If you haven't already, you'll need to create a Ktor project. You can do this using an IDE like IntelliJ IDEA, which has a Ktor project wizard, or manually using Gradle or Maven.

For Gradle, your `build.gradle.kts` file might look something like this (adjust versions as needed):

```kotlin
plugins {
    kotlin("jvm") version "1.9.22"
    id("io.ktor.plugin") version "2.3.10"
    kotlin("plugin.serialization") version "1.9.22"
}

group = "org.example"
version = "0.0.1"

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor.server:ktor-server-core-jvm:2.3.10")
    implementation("io.ktor.server:ktor-server-netty-jvm:2.3.10")
    implementation("io.ktor.server:ktor-server-content-negotiation-jvm:2.3.10")
    implementation("io.ktor.serialization:ktor-serialization-kotlinx-json-jvm:2.3.10")
    implementation("ch.qos.logback:logback-classic:1.2.11")
    testImplementation(kotlin("test-junit5"))
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.8.1")
    testImplementation("org.junit.jupiter:junit-jupiter-engine:5.8.1")
}

ktor {
    fatJar {
        manifest {
            attributes["Main-Class"] = "com.example.ApplicationKt" // Adjust if your main class is different
        }
    }
}

tasks.test {
    useJUnitPlatform()
}
```

**Step 2: Define your `Product` data class and a storage mechanism.**

You already have the `Product` data class defined. For this example, we'll use an in-memory mutable list to store our products. In a real application, you would likely use a database.

```kotlin
package com.example // Adjust your package

import kotlinx.serialization.Serializable

@Serializable
data class Product(val id: Int, val name: String, val price: Double)

val products = mutableListOf<Product>(
    Product(1, "Laptop", 1200.00),
    Product(2, "Mouse", 25.00)
)
```

**Step 3: Create the main application function.**

Create a Kotlin file (e.g., `Application.kt`) with the main function to start the Ktor server and configure routing.

```kotlin
package com.example // Adjust your package

import io.ktor.http.*
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun main() {
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            json()
        }
        routing {
            // Will add GET and POST endpoints here in the next steps
        }
    }.start(wait = true)
}
```

* We use `embeddedServer(Netty, port = 8080)` to create and configure a Netty server on port 8080.
* `install(ContentNegotiation) { json() }` configures Ktor to handle JSON content, which is essential for our REST API.

**Step 4: Implement the GET endpoint to retrieve all products (`/products`).**

Inside the `routing` block, add the following `get` route:

```kotlin
routing {
    install(ContentNegotiation) {
        json()
    }
    get("/products") {
        call.respond(HttpStatusCode.OK, products)
    }
    // ... other routes will go here
}
```

* `get("/products")` defines a route that listens for HTTP GET requests to the `/products` path.
* `call.respond(HttpStatusCode.OK, products)` responds to the client with an HTTP status code `200 OK` and the `products` list. Ktor, with the `ContentNegotiation` plugin configured for JSON, will automatically serialize the `products` list into a JSON array.

**Step 5: Implement the GET endpoint to retrieve a specific product by ID (`/products/{id}`).**

Add another `get` route within the `routing` block:

```kotlin
routing {
    install(ContentNegotiation) {
        json()
    }
    get("/products") {
        call.respond(HttpStatusCode.OK, products)
    }
    get("/products/{id}") {
        val id = call.parameters["id"]?.toIntOrNull()
        if (id == null) {
            call.respond(HttpStatusCode.BadRequest, "Invalid product ID")
            return@get
        }
        val product = products.find { it.id == id }
        if (product != null) {
            call.respond(HttpStatusCode.OK, product)
        } else {
            call.respond(HttpStatusCode.NotFound, "Product not found")
        }
    }
    // ... other routes
}
```

* `get("/products/{id}")` defines a route with a path parameter `{id}`.
* `call.parameters["id"]` retrieves the value of the `id` path parameter as a String.
* `.toIntOrNull()` attempts to convert the ID to an integer. If it fails (e.g., the ID is not a number), it returns `null`, and we respond with a `BadRequest` (400) status.
* `products.find { it.id == id }` searches the `products` list for a product with the matching ID.
* If a product is found, we respond with `OK` (200) and the `Product` object (which will be serialized to JSON).
* If no product is found, we respond with `NotFound` (404).

**Step 6: Implement the POST endpoint to create a new product (`/products`).**

Add a `post` route within the `routing` block:

```kotlin
routing {
    install(ContentNegotiation) {
        json()
    }
    get("/products") {
        call.respond(HttpStatusCode.OK, products)
    }
    get("/products/{id}") {
        // ... (previous get route)
    }
    post("/products") {
        try {
            val newProduct = call.receive<Product>()
            products.add(newProduct)
            call.respond(HttpStatusCode.Created, newProduct)
        } catch (e: Exception) {
            call.respond(HttpStatusCode.BadRequest, "Invalid product data")
        }
    }
}
```

* `post("/products")` defines a route that listens for HTTP POST requests to the `/products` path.
* `call.receive<Product>()` attempts to deserialize the JSON request body into a `Product` object. This relies on the `ContentNegotiation` plugin being configured for JSON.
* If the deserialization is successful, the new `Product` is added to the `products` list, and we respond with `Created` (201) and the newly created `Product` object in the response body.
* A `try-catch` block is used to handle potential exceptions during the `call.receive<Product>()` process, such as if the request body is not valid JSON or doesn't match the structure of the `Product` data class. In such cases, we respond with `BadRequest` (400).

**Step 7: Run your Ktor application.**

You can run your application from your IDE or by using the Gradle command:

```bash
./gradlew run
```

**Step 8: Test your API endpoints.**

You can use tools like `curl`, Postman, or Insomnia to test your API:

* **GET all products:**
    ```bash
    curl http://localhost:8080/products
    ```

* **GET a specific product by ID (e.g., ID 1):**
    ```bash
    curl http://localhost:8080/products/1
    ```

* **POST a new product:**
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"id":3,"name":"Keyboard","price":75.0}' http://localhost:8080/products
    ```

This step-by-step guide should help you convert your `Product` data class into a functional REST API using Ktor with GET and POST endpoints. Remember that this is a basic in-memory implementation. For a production-ready API, you would need to consider database integration, more robust error handling, validation, and other security and architectural best practices.