import re


def part1() -> None:
    with open("./inputs/day1.txt") as f:
        data = f.read().splitlines()

    digits = [[c for c in line if c.isdigit()] for line in data]
    all_digits = [int(f"{item[0]}{item[-1]}") for item in digits]
    print(f"{sum(all_digits)=}")


def part2() -> None:
    with open("./inputs/day1.txt") as f:
        data = f.read().splitlines()

    word_value = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    pattern = "|".join([*word_value.keys(), *(str(i) for i in word_value.values())])
    pattern_lookahead = f"(?=({pattern}))"

    clean_data: list[list[str]] = [re.findall(pattern_lookahead, line) for line in data]

    def numerify(character: str) -> int:
        if character.isdigit():
            return int(character)
        return word_value[character]

    all_digits = [
        numerify(f"{item[0]}") * 10 + numerify(f"{item[-1]}") for item in clean_data
    ]

    print(f"{sum(all_digits)=}")
