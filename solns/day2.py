import re

from functools import reduce
from operator import mul
from typing import Mapping

with open("./inputs/day2.txt", "r") as f:
    data = f.read().splitlines()


def part1() -> None:
    rbg = re.compile("(\d+) (red|blue|green)")

    def validate_counter(mapping: Mapping[str, int]) -> bool:
        MAX_RED = 12
        MAX_GREEN = 13
        MAX_BLUE = 14

        return all(
            [
                mapping["red"] <= MAX_RED,
                mapping["blue"] <= MAX_BLUE,
                mapping["green"] <= MAX_GREEN,
            ]
        )

    possible_games = []

    for line in data:
        game_id, combos = line.split(": ")
        game_data = combos.split("; ")

        current_values: dict[str, int] = {}
        for subset in game_data:
            matches = rbg.findall(subset)
            new_values = {k: int(v) for v, k in matches}
            for k, v in new_values.items():
                val = current_values.get(k, 0)
                current_values[k] = max(v, val)

        if validate_counter(current_values):
            possible_games.append(int(game_id.strip("Game ")))

    print((f"{sum(possible_games)=}"))  # 2683


def part2() -> None:
    rbg = re.compile("(\d+) (red|blue|green)")

    powers = []
    for line in data:
        _, combos = line.split(": ")
        game_data = combos.split("; ")

        current_values: dict[str, int] = {}
        for subset in game_data:
            matches = rbg.findall(subset)
            new_values = {k: int(v) for v, k in matches}

            for k, v in new_values.items():
                current_values[k] = (
                    v
                    if (curr_val := current_values.get(k)) is None
                    else max(v, curr_val)
                )

        power_value = reduce(mul, current_values.values())
        powers.append(power_value)

    print(f"{sum(powers)=}")  # 49710
