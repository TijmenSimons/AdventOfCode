"""
Usage:

python main.py [year] [day] [part]

When value is not provided, it will default to the latest used values.
"""


import os
import sys
from pathlib import Path
from dotenv import load_dotenv

import requests

load_dotenv()


default_data = """from {this_module} import get_input, store_output

__info = [{year}, {day}, {part}]

def main():
    data = get_input(*__info)
    store_output(data, *__info)


if __name__ == "{new_module}":
    main()
    
"""


def generate_scripts(data: str, year: str, day: str):
    print("Creating...")

    token = os.getenv("TOKEN")
    with open(".env", "a") as f:
        f.write("\nTOKEN=")
    if not token:
        msg = "Please set your AoC session token (found in cookie 'session') as 'TOKEN=<token>' in the .env file (I created one for you)"
        raise Exception(msg)
    
    if not os.path.exists(year):
        os.makedirs(year)
        
    path = f"{year}/day_{day}"
    if not os.path.exists(path):
        os.makedirs(path)

    with open(f"{path}/part_1.py", "w") as f:
        f.write(data.format(year=year, day=day, part=1, this_module=__name__, new_module=f"{year}.day_{day}.part_1"))

    with open(f"{path}/part_2.py", "w") as f:
        f.write(data.format(year=year, day=day, part=2, this_module=__name__, new_module=f"{year}.day_{day}.part_1"))

    print(f"Created new workspace for year: {year}, day: {day}.")
    print("Getting input...")

    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={'session': token})

    assert response.status_code == 200, "Something went wrong, is your token outdated?"

    with open(f"{year}/day_{day}/input.txt", "w") as f:
        f.write(response.text)
    
    with open(f"{year}/day_{day}/part_1_output.txt", "a") as f:
        ...
    
    with open(f"{year}/day_{day}/part_2_output.txt", "a") as f:
        ...


def main(data: str):
    args = sys.argv

    try:
        with open("latest.txt", "r") as f:
            defaults = f.read().split(",")

    except FileNotFoundError:
        with open("latest.txt", "a") as f:
            ...
        defaults = ["2021", "1", "1"]
    
    year = args[1] if len(args) > 1 else defaults[0]
    day = args[2] if len(args) > 2 else defaults[1]
    part = args[3] if len(args) > 3 else "1" if len(args) > 2 else defaults[2]


    my_file = Path(os.getcwd(), f"{year}/day_{day}/part_1.py")

    if my_file.is_file():
        __import__(name=f"{year}.day_{day}.part_{part}")

    else:
        generate_scripts(data, year, day)

    with open("latest.txt", "w") as f:
        defaults = ",".join([year, day, part])
        f.write(defaults)


def get_input(year: int, day: int, _, split_enter: bool = True):
    with open(f"{year}/day_{day}/input.txt", "r") as f:
        data = f.read()
        if split_enter:
            data = data.split("\n")
        return data
    

def store_output(data: any, year: int, day: int, part: int, array_to_enter: bool = False):
    if array_to_enter:
        data = "\n".join(data)

    
    with open(f"{year}/day_{day}/part_{part}_output.txt", "w") as f:
        f.write(str(data))

__all__ = [
    "get_input"
]


if __name__ == "__main__":
    main(default_data)
