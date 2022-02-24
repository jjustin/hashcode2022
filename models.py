from typing import List, Dict


class Skill:
    def __init__(self, name: str, level: int) -> None:
        self.name = name
        self.level = level

    def __str__(self) -> str:
        return f"{self.name}-{self.level}"


class Contributor:
    def __init__(self, name: str, skills: List[Skill]) -> None:
        self.name = name
        self.skills: Dict[str, Skill] = {}
        for skill in skills:
            self.skills[skill.name] = skill
        self.free_after = 0

    def __str__(self) -> str:
        skills_string = ', '.join([str(x) for x in self.skills])
        return f"{self.name}: {skills_string}"

    def is_free(self, today):
        return today > self.free_after or self.free_after == 0

    def increase_skill(self, skill_name: str) -> Skill:
        if skill_name in self.skills:
            self.skills[skill_name].level += 1
        else:
            self.skills[skill_name] = Skill(skill_name, 1)
        return self.skills[skill_name]


class Project:
    def __init__(self, name: str, skills: List[Skill], needs_days: int, best_before: int, score_worth: int,   n_roles: int) -> None:
        self.name = name
        self.skills = skills
        self.best_before = best_before
        self.needs_days = needs_days
        self.score_worth = score_worth
        self.n_roles = n_roles

        self.contributors: List[Contributor] = []
        self.done = False

    def __lt__(self, other):
        return self.needs_days < other.needs_days

    def __str__(self) -> str:
        return f"{self.name} {self.n_roles}"

    def is_doable_before_deadline(self, today):
        return today + self.needs_days < self.best_before + (self.score_worth/2)
