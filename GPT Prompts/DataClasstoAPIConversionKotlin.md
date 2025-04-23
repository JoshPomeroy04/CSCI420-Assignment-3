# Zero-shot Prompting

## Input
    Convert the data class to a REST API using Ktor:

    data class Product ( val id : Int , val name : String , val price : Double )
    // TODO : Create GET and POST endpoints using Ktor 

## Output
Sure! Here's how you can convert the `Product` data class into a simple REST API with **GET** and **POST** endpoints using **Ktor** in Kotlin.

---

### ✅ Step-by-Step Ktor REST API Example

```kotlin
import io.ktor.application.*
import io.ktor.http.*
import io.ktor.request.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import kotlinx.serialization.Serializable
import io.ktor.features.ContentNegotiation
import io.ktor.serialization.json

// 1. Product Data Class
@Serializable
data class Product(val id: Int, val name: String, val price: Double)

// 2. In-memory product storage
val products = mutableListOf<Product>()

// 3. Main entry point
fun main() {
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            json() // Enable JSON support
        }
        routing {
            // GET all products
            get("/products") {
                call.respond(products)
            }

            // POST a new product
            post("/products") {
                val product = call.receive<Product>()
                products.add(product)
                call.respond(HttpStatusCode.Created, product)
            }
        }
    }.start(wait = true)
}
```

---

### 💡 How to Test It:

- **GET all products:**
  ```
  curl http://localhost:8080/products
  ```

- **POST a new product:**
  ```
  curl -X POST http://localhost:8080/products \
       -H "Content-Type: application/json" \
       -d '{"id":1,"name":"Book","price":10.5}'
  ```

Let me know if you want to add **update/delete endpoints**, use a **database** instead of in-memory list, or structure it using **Ktor modules**.

# Chain-of-Thoughts Prompting

## Input 
    Step by step, convert the data class to a REST API using Ktor:

    data class Product ( val id : Int , val name : String , val price : Double )
    // TODO : Create GET and POST endpoints using Ktor 

## Output
Absolutely! Let’s go step by step to turn the `Product` data class into a REST API with **Ktor**, including **GET** and **POST** endpoints.

---

### ✅ **Step 1: Define the `Product` Data Class**

Start with your Kotlin data class. To support JSON serialization, we annotate it with `@Serializable`.

```kotlin
import kotlinx.serialization.Serializable

@Serializable
data class Product(val id: Int, val name: String, val price: Double)
```

---

### ✅ **Step 2: Set Up a Ktor Project**

Make sure you have Ktor dependencies in your `build.gradle.kts`:

```kotlin
dependencies {
    implementation("io.ktor:ktor-server-core:2.3.4")
    implementation("io.ktor:ktor-server-netty:2.3.4")
    implementation("io.ktor:ktor-server-content-negotiation:2.3.4")
    implementation("io.ktor:ktor-serialization-kotlinx-json:2.3.4")
}
```

---

### ✅ **Step 3: Create an In-Memory List to Store Products**

We'll use a simple `MutableList` to hold the products for now.

```kotlin
val products = mutableListOf<Product>()
```

---

### ✅ **Step 4: Set Up Ktor Application**

Now we’ll set up a basic Ktor server with content negotiation enabled for JSON.

```kotlin
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.application.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.response.*
import io.ktor.server.request.*
import io.ktor.server.routing.*
import io.ktor.http.*

fun main() {
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            json()
        }
        routing {
            // We'll add endpoints here
        }
    }.start(wait = true)
}
```

---

### ✅ **Step 5: Add REST Endpoints**

Now let’s implement:

#### 📥 POST `/products` – Add a new product  
#### 📤 GET `/products` – List all products

Inside the `routing` block:

```kotlin
routing {
    // GET all products
    get("/products") {
        call.respond(products)
    }

    // POST a new product
    post("/products") {
        val product = call.receive<Product>()
        products.add(product)
        call.respond(HttpStatusCode.Created, product)
    }
}
```

---

### ✅ **Final Code (All Together)**

```kotlin
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.application.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*
import io.ktor.server.response.*
import io.ktor.server.request.*
import io.ktor.server.routing.*
import io.ktor.http.*
import kotlinx.serialization.Serializable

@Serializable
data class Product(val id: Int, val name: String, val price: Double)

val products = mutableListOf<Product>()

fun main() {
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            json()
        }
        routing {
            get("/products") {
                call.respond(products)
            }
            post("/products") {
                val product = call.receive<Product>()
                products.add(product)
                call.respond(HttpStatusCode.Created, product)
            }
        }
    }.start(wait = true)
}
```

---

Let me know if you want to:

- Add support for PUT or DELETE
- Persist data using a database (e.g., Exposed + SQLite/Postgres)
- Use dependency injection (e.g., Koin)
- Add error handling or validation

Happy coding!