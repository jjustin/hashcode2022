from models import Skill, Contributer, Project


def read_inputs(filename="input_data/a_an_example.in.txt"):
    """Reads the inputs and instantiates objects"""
    f = open(filename, "r")
    num_contributors, num_projects = map(int, f.readline().split(" "))

    # Create contributors
    contributors = []
    for i in range(num_contributors):
        contributor_params = f.readline().split(" ")
        contributor_name = contributor_params[0]
        num_skills = int(contributor_params[1])

        skills = []
        for j in range(num_skills):
            skill_params = f.readline().split(" ")
            skill_name = skill_params[0]
            skill_level = int(skill_params[1])
            skill = Skill(skill_name, skill_level)
            skills.append(skill)

        contributer = Contributer(contributor_name, skills)
        contributors.append(contributer)

    # Create projects
    projects = []
    for i in range(num_projects):
        project_name, di, si, bi, ri = f.readline().split(" ")
        n_roles = int(ri)
        needs_days = int(di)
        best_before = int(bi)
        score_worth = int(si)

        # Roles in project
        skills = []
        for j in range(n_roles):
            skill_params = f.readline().split(" ")
            skill_name = skill_params[0]
            skill_level = int(skill_params[1])
            skill = Skill(skill_name, skill_level)
            skills.append(skill)

        project = Project(project_name, skills, needs_days,
                          best_before, score_worth, n_roles)
        projects.append(project)

    f.close()

    return contributors, projects


def write_outputs(output, filename="output_data/output.txt"):
    """Writes the outputs into the correct format"""
    f = open(filename, "w")
    f.write(output)
    f.close()


if __name__ == '__main__':
    c, p = read_inputs()
    for i in c:
        print(i)
    for i in p:
        print(i)
