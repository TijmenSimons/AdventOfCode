import requests


def req(year: int | str, day: int | str):
    response = requests.get(f"https://adventofcode.com/{str(year)}/day/{str(day)}/input")

    assert response.status_code == 200

    return response.json()
