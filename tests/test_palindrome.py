"""
Feature Description and Acceptanced Criteria:

We want to develop a restful endpoint that validates whether a word is a palindrome.
A palindrome is a word, phrase, or sequence that reads the same backward as forward.
For our palindrome identifier we should do the following:
    - ignore
        - spacing
        - punctuation
        - capitalization
    - takes a word or sentence
    - errors are handled gracefully with an error response and reason



Task:
Write tests for application endpoint palindrome

Request Info:

POST to http://localhost:8080/palindrome
header: Content-Type application/json
Request body: { "word": "racecar" }

Sample Response:
{
    "is_palindrome": false,
    "word": "racecar"
}
"""


def test_correctly_identifies_a_palindrome():
    """Validate palindrome endpoint correctly identifies a palindrome"""
    actual_value = None

    # Fill in code to fetch the actual is_palindrome value from application

    assert actual_value
