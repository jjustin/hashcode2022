from typing import List, Dict, Tuple
import models
import hcio

MAX_LEVEL = 100
MAX_DAYS = 10000
MAX_REROLLS = 5


def run(projects: List[models.Project], contributors: List[models.Contributor], projectwindov=3):
    out = ""
    done_projects = 0

    skilled: Dict[str, Dict[int, Dict[str, models.Contributor]]] = {}
    for contributor in contributors:
        for skill in contributor.skills.values():
            if skill.name not in skilled:
                skilled[skill.name] = {}
                for i in range(0, MAX_LEVEL+1):
                    skilled[skill.name][i] = {}

            skilled[skill.name][skill.level][contributor.name] = contributor

    for today in range(0, MAX_DAYS):
        if today % 100 == 0:
            print(today)
        for project in projects:
            if project.done:
                continue
            failed = False
            used: List[Tuple[models.Contributor, models.Skill]] = []
            used_names: List[str] = []
            for skill in project.skills:
                found_contributor = False
                min_level = skill.level

                can_be_mentored = False
                for contributor, _ in used:
                    can_be_mentored = can_be_mentored or (
                        skill.name in contributor.skills and contributor.skills[skill.name].level >= skill.level)

                if can_be_mentored:
                    min_level = min_level-1
                for level in range(min_level, MAX_LEVEL+1):
                    possible = skilled[skill.name][level]

                    for contributor in possible.values():
                        if contributor.is_free(today) and contributor.name not in used_names:
                            found_contributor = True
                            project.contributors.append(contributor)
                            used.append((contributor, skill))
                            used_names.append(contributor.name)
                            break
                    if found_contributor:
                        break

                # no contributor found for this skill - skip this project
                if not found_contributor:
                    failed = True
                    project.contributors = []
                    # print(
                    #     f"no found contributror for {project.name}/{skill.name}")
                    break

            if failed:
                continue

            project.done = True
            out += f"{project.name}\n"
            for contributor, skill in used:
                out += contributor.name + " "
                contributor.free_after = today + project.needs_days

                if skill.name in contributor.skills and skill.level >= contributor.skills[skill.name].level:
                    skill = contributor.increase_skill(skill.name)
                    skilled[skill.name][skill.level][contributor.name] = contributor
                    if skill.level != 1:
                        del skilled[skill.name][skill.level -
                                                1][contributor.name]
            out += "\n"
            done_projects += 1

        projects = filter(lambda p: (not p.done), projects)
        projects = [p for p in projects]

        if len(projects) == 0:
            break
    return f"{done_projects}\n{out}"


if __name__ == "__main__":
    for filename in [
        "a_an_example",
        "b_better_start_small",
        "c_collaboration",
        "d_dense_schedule",
        "e_exceptional_skills",
        "f_find_great_mentors"
    ]:
        contrs, projects = hcio.read_inputs(f"input_data/{filename}.in.txt")
        print(filename)
        out = run(projects, contrs)
        hcio.write_outputs(out,
                           filename=f"output_data2/{filename}.out.txt")
