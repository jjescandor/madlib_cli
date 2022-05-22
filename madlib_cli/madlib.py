from os import read
import re
from pathlib import Path
import os

"""
Make Me A Video Game!

I the majestic and purple Scott have colored JB's laughing sister and plan to steal her tickled arrows!

What are a gorilla and backpacking butterfly to do? Before you can help Betty, you'll have to collect the silly tests and striped jackets that open up the 44 worlds connected to Wilson's' Lair. There are 3 leaves and 4 swords in the game, along with hundreds of other goodies for you to find.

"""

default_path = "assets/make_me_a_video_game_template.txt"

welcome = """
Welcome to python madlib.\n
You will be asked a series of questions to play the game
"""

def read_template(path=default_path):
    madlib = ""
    if not os.path.isfile(path):
        raise FileNotFoundError
    else:
        with open(path) as f:
            madlib = f.read()
    return madlib


def parse_template(raw=read_template()):
    pattern = r'\{[^}]*\}'
    pattern_two = r'{([^}]*)}'
    cleaned_txt = re.sub(pattern, "{}", raw)
    parts = tuple(re.findall(pattern_two, raw))
    return [cleaned_txt, parts]


def get_user_input(raw=read_template()):
    usr_answers = []
    parts = parse_template(raw)[1]
    for part in parts:
        prompt = input(f"Enter {part}: ")
        usr_answers.append(prompt)
    return usr_answers


def merge(file, usr_input):
    return file.format(*usr_input)


def write_file(file):
    path_name = "assets/user_file.txt"
    with open(path_name, "w") as f:
        f.write(file)
        path = Path(path_name)
        save_file = path.is_file()
        print(f"File saved to disk: {   save_file}")
    try:
        with open(path_name) as f:
            f.read()
    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    print(welcome)
    new_file = merge(parse_template()[0], tuple(get_user_input()))
    print('*'*10)
    print(new_file)
    print('*'*10)
    write_file(new_file)
