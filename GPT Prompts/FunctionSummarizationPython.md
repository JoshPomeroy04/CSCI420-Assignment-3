# Zero-shot Prompting

## Input
    Write a brief summary of the function:

    def reverse_words ( sentence ) :
        return ’ ’. join ( sentence . split () [:: -1])

## Output
The function `reverse_words(sentence)` takes a string `sentence` as input, splits it into words, reverses the order of the words, and then joins them back into a single string separated by spaces. It returns this reversed word order as the output.


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
