# SPDX-License-Identifier: BSD-3-Clause

from tilthenightends import Levelup, LevelupOptions, Vector, Team, Towards
import random

useful_levelup_options = {
    "evelyn": [  # Magic Wand
        LevelupOptions.player_health,
        LevelupOptions.player_speed,
        LevelupOptions.weapon_health,
        LevelupOptions.weapon_cooldown,
        LevelupOptions.weapon_damage,
        LevelupOptions.weapon_size,
        LevelupOptions.weapon_speed,
        LevelupOptions.weapon_longevity,
    ],
    "theron": [  # Garlic
        LevelupOptions.player_health,
        LevelupOptions.player_speed,
        LevelupOptions.weapon_damage,
        LevelupOptions.weapon_size,
    ],
    "alaric": [  # Fireball
        LevelupOptions.player_health,
        LevelupOptions.player_speed,
        LevelupOptions.weapon_health,
        LevelupOptions.weapon_cooldown,
        LevelupOptions.weapon_damage,
        LevelupOptions.weapon_size,
    ],
    "isolde": [  # Holy Water
        LevelupOptions.player_health,
        LevelupOptions.player_speed,
        LevelupOptions.weapon_cooldown,
        LevelupOptions.weapon_damage,
        LevelupOptions.weapon_size,
    ],
    "selene": [  # Mine
        LevelupOptions.player_health,
        LevelupOptions.player_speed,
        LevelupOptions.weapon_cooldown,
        LevelupOptions.weapon_damage,
        LevelupOptions.weapon_size,
        LevelupOptions.weapon_health,
        LevelupOptions.weapon_longevity,
    ],
}


class Brain:
    def __init__(self):
        pass

    def levelup(self, t: float, info: dict, players: dict) -> Levelup:
        alive_players = {p:player for p, player in players.items() if player.health > 0}
        current_player = random.choice(list(alive_players.keys()))
        option = random.choice(useful_levelup_options[current_player])
        return Levelup(current_player, option)

class GoToDifferent5Directions:
    def __init__(self, hero: str, direction: int):
        self.hero = hero
        self.direction = direction

    def run(self, t, dt, monsters, players, pickups) -> Vector | Towards | None:
        match self.direction:
            case 0:
                return Towards(100_000, 100_000)
            case 1:
                return Towards(-100_000, 100_000)
            case 2:
                return Towards(100_000, -100_000)
            case 3:
                return Towards(-100_000, -100_000)
            case 4:
                return Towards(0, 0)
            case _:
                raise ValueError

team = Team(
    players=[
        GoToDifferent5Directions(hero="isolde", direction=0),
        GoToDifferent5Directions(hero="theron", direction=1),
        GoToDifferent5Directions(hero="alaric", direction=2),
        GoToDifferent5Directions(hero="selene", direction=3),
        GoToDifferent5Directions(hero="evelyn", direction=4),
    ],
    strategist=Brain(),
)
