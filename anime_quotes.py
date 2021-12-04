import random

quotes = [
    "{verb1} the anger swelling inside you nFighting the boundary till you {verb2} through \n{adjective} in your soul there is no {noun} \nSo make yourself the one they all fear",
    "{verb1} something that no one else {verb2} is a {adjective} thing. You can’t talk to anyone about it. No one will understand you. {noun}’ll be alone.",
]


def get_random_quote(quotes):
    random_index = random.randint(0, len(quotes))
    quote = quotes[random_index]
    return quote
