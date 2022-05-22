from os import read
import re

"""
Make Me A Video Game!

I the majestic and purple Scott have colored JB's laughing sister and plan to steal her tickled arrows!

What are a gorilla and backpacking butterfly to do? Before you can help Betty, you'll have to collect the silly tests and striped jackets that open up the 44 worlds connected to Wilson's' Lair. There are 3 leaves and 4 swords in the game, along with hundreds of other goodies for you to find.

"""

default_path = "assets/make_me_a_video_game_template.txt"

welcome = """
Welcome to python madlib."\"
You will be asked a series of questions to play the game
"""


def read_template(path=default_path):
    madlib = ""
    with open(path) as f:
        madlib = f.read()
        print("Wrong file or file path")
    return madlib


def parse_template(raw=read_template()):
    c = list(re.split(r"[{}]", raw))
    cleaned_txt = []
    parts = []
    for a in c:
        if "adjective" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "noun" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "first name" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "past tense verb" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "num" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "large animal" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "small animal" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        elif "girl's name" in a.lower():
            parts.append(a)
            cleaned_txt.append("{}")
        else:
            cleaned_txt.append(a)
    return ["".join(cleaned_txt), tuple(parts)]


def get_user_input(raw=read_template()):
    parse_template()
    c = list(re.split(r"[{}]", raw))
    b = []
    for a in c:
        if "adjective" in a.lower():
            d = input("Enter an adjective: ")
            b.append(d)
        elif "noun" in a.lower():
            d = input("Enter a noun: ")
            b.append(d)
        elif "first name" in a.lower():
            d = input("Enter a first name: ")
            b.append(d)
        elif "past tense verb" in a.lower():
            d = input("Enter a past tense verb: ")
            b.append(d)
        elif "num" in a.lower():
            d = input("Enter a number (1-50): ")
            b.append(d)
        elif "large animal" in a.lower():
            d = input("Enter a large animal: ")
            b.append(d)
        elif "small animal" in a.lower():
            d = input("Enter a small animal ")
            b.append(d)
        elif "girl's name" in a.lower():
            d = input("Enter a small animal ")
            b.append(d)
    return b


def merge(file, usr_input):
    return file.format(*usr_input)


if __name__ == "__main__":
    print(merge(parse_template()[0], tuple(get_user_input())))
