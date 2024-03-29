"""
Run or generate a day script for advent of code.

Usage:

python main.py [year] [day] [part]

When value is not provided, it will default to the latest used values.
"""


import os
import sys
import requests
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()


script = """from {this_module} import get_input

__info = [{year}, {day}, {part}]

def main():
    data = get_input(*__info)
    data = \"""\""".split("\\n")
    
    for line in data[:-1]:
        print(line)


if __name__ == "{new_module}":
    main()
"""


def generate_scripts(year: str, day: str):
    print("Creating...")

    path = f"{year}/day_{day}"
    if not os.path.exists(path):
        os.makedirs(path)

    def make(part):
        with open(f"{path}/part_{part}.py", "w") as f:
            f.write(
                script.format(
                    year=year,
                    day=day,
                    part=part,
                    this_module=__name__.split("_")[2],
                    new_module=f"{year}.day_{day}.part_{part}",
                )
            )

    make("1")
    make("2")

    with open(f"{year}/day_{day}/part_1_output.txt", "a"):
        ...

    with open(f"{year}/day_{day}/part_2_output.txt", "a"):
        ...

    print(f"Created new workspace for year: {year}, day: {day}.")


def main():
    args = sys.argv

    try:
        with open("latest.txt", "r") as f:
            defaults = f.read().split(",")

    except FileNotFoundError:
        with open("latest.txt", "a"):
            ...
        defaults = ["2021", "1", "1"]

    year = args[1] if len(args) > 1 else defaults[0]
    day = args[2] if len(args) > 2 else defaults[1]
    part = args[3] if len(args) > 3 else "1" if len(args) > 2 else defaults[2]

    my_file = Path(os.getcwd(), f"{year}/day_{day}/part_1.py")

    if my_file.is_file():
        __import__(name=f"{year}.day_{day}.part_{part}")

    else:
        generate_scripts(year, day)

    with open("latest.txt", "w") as f:
        defaults = ",".join([year, day, part])
        f.write(defaults)


def get_input(year: int, day: int, _, split_enter: bool = True):
    try:
        with open(f"{year}/day_{day}/input.txt", "r") as f:
            data = f.read()
            if split_enter:
                data = data.split("\n")
            return data
    except FileNotFoundError:
        ...

    token = os.getenv("TOKEN")
    if not token:
        with open(".env", "a") as f:
            f.write("\nTOKEN=")

        msg = "Please set your AoC session token (found in cookie 'session') as 'TOKEN=<token>' in the .env file (I created one for you)"
        raise Exception(msg)

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": token}
    )

    if response.status_code == 404:
        msg = "Input does not exist!"
        raise Exception(msg)

    assert response.status_code == 200, "Something went wrong, is your token outdated?"

    with open(f"{year}/day_{day}/input.txt", "w") as f:
        f.write(response.text)

    return response.text


def store_output(
    data: any, year: int, day: int, part: int, array_to_enter: bool = False
):
    if array_to_enter:
        data = "\n".join(data)

    path = f"{year}/day_{day}/part_{part}_output.txt"

    with open(path, "w") as f:
        f.write(str(data))

    print(f"Output: {path} == {str(data)[:100]}...")


__all__ = ["get_input"]


if __name__ == "__main__":
    main()
