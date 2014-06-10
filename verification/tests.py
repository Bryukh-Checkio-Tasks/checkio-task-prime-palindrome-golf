"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": 2,
            "answer": 3
        },
        {
            "input": 13,
            "answer": 101
        },
        {
            "input": 101,
            "answer": 131
        },
        {
            "input": 9000,
            "answer": 10301
        },
    ],
    "Edge": [
        {
            "input": 1,
            "answer": 2
        },
        {
            "input": 999999,
            "answer": 1003001
        },
        {
            "input": 10,
            "answer": 11
        },
        {
            "input": 8,
            "answer": 11
        },
        {
            "input": 5,
            "answer": 7
        },

        {
            "input": 11,
            "answer": 101
        },

        {
            "input": 98688,
            "answer": 98689
        },
    ],
    "Extra": [
        {
            "input": 7758,
            "answer": 10301
        },
        {
            "input": 9520,
            "answer": 10301
        },
        {
            "input": 5157,
            "answer": 10301
        },
        {
            "input": 7091,
            "answer": 10301
        },
        {
            "input": 8932,
            "answer": 10301
        },
        {
            "input": 1401,
            "answer": 10301
        },
        {
            "input": 679,
            "answer": 727
        },
    ]
}
