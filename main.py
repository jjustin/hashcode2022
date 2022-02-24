from typing import List, Dict
import models
import hcio
import json

MAX_LEVEL = 100


def run(projects: List[models.Project], contributors: List[models.Contributor], projectwindov=3):
    out = ""
    today = 0

    skilled: Dict[str, Dict[int, List[models.Contributor]]] = {}
    for contributor in contributors:
        for skill in contributor.skills:
            if skill.name not in skilled:
                skilled[skill.name] = {}
                for i in range(0, MAX_LEVEL+1):
                    skilled[skill.name][i] = []

            skilled[skill.name][skill.level].append(contributor)
    print(skilled)
    for project in projects:
        for skill in project.skills:
            found_contributor = False
            min_level = skill.level
            if False:  # allow mentoring !! TODO
                min_level = min_level-1
            for level in range(min_level, MAX_LEVEL):
                if found_contributor:
                    break
                possible = skilled[skill.name][level]

                for tried in possible:
                    if tried.is_free(today):
                        found_contributor = True
                        project.contributors.append(tried)

            # no contributor found for this skill - skip this project
            if not found_contributor:
                break

        out += f"{project.name}\n"
        for contributor in project.contributors:
            out += contributor.name
            contributor.free_after = today + project.needs_days
        out += "\n"
    return out


if __name__ == "__main__":
    for filename in [
        "a_an_example"
    ]:
        contrs, projects = hcio.read_inputs(f"input_data/{filename}.in.txt")
        hcio.write_outputs(run(projects, contrs),
                           filename=f"output_data/{filename}.out.txt")
