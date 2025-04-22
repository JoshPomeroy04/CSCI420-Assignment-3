# Zero-shot Prompting

## Input
    Write a brief summary of the function:

    def reverse_words ( sentence ) :
        return ’ ’. join ( sentence . split () [:: -1])

## Output
That Python function `reverse_words` takes a string called `sentence` as input. It first splits the sentence into a list of individual words using the `split()` method (which by default splits on whitespace). Then, it uses slicing `[::-1]` to create a reversed copy of this list of words. Finally, it joins the reversed list of words back into a single string with spaces in between each word using the `' '.join()` method.

In essence, this function **reverses the order of words within a sentence**.


# One-shot Prompting

## Input
    ### Code:
    def is_even(n):
        return n % 2 == 0
    ### Summary:
    Checks if a number is even.

    ### Code:
    def reverse_words ( sentence ) :
        return ’ ’. join ( sentence . split () [:: -1])
    ### Summary:

## Output
Reverses the order of words in a sentence.
