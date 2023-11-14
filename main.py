import os


default_data = """from input import req

def get_input():
    return req({}, {})


def main():
    ...


if __name__ == "__main__":
    main()
    
"""


def main(data: str):
    print("Generating a new folder...")
    
    year = input("The year: ")
    day = input("The day: ")

    print("Creating...")

    if not os.path.exists(year):
        os.makedirs(year)
        
    path = f"{year}/day_{day}"
    if not os.path.exists(path):
        os.makedirs(path)

    with open(f"{path}/part_1.py", "w") as f:
        data = data.format(year, day)
        f.write(data)

    with open(f"{path}/part_2.py", "w") as f:
        data = data.format(year, day)
        f.write(data)

    print("Finished.")


if __name__ == "__main__":
    main(default_data)

