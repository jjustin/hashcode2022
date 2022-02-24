from typing import List


class Skill:
    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level


class Contributer:
    def __init__(self, name: str, skills: List[Skill]) -> None:
        self.name = name
        self.skills = skills
        self.free_after = 0


class Project:
    def __init__(self, name: str, skills: List[Skill], needs_days: int, best_before: int, score_worth: int,   n_roles: int) -> None:
        self.name = name
        self.skills = skills
        self.best_before = best_before
        self.needs_days = needs_days
        self.score_worth = score_worth
        self.n_roles = n_roles