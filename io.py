def read_inputs(filename="input_data/a_an_example.in.txt"):
    """Reads the inputs and instantiates objects"""
    f = open(filename, "r")
    num_contributors, num_projects = map(int, f.readline().split(" "))
    
    # Create contributors
    contributors = []
    for i in range(num_contributors):
        contributor_params = f.readline().split(" ")
        name = contributor_params[0]
        num_skills = int(contributor_params[1])

        for j in range(num_skills):
            skill_params = f.readline().split(" ")
            skill = skill_params[0]
            skill_level = int(skill_params[1])

        #contributors.append()
    
    f.close()


def write_outputs(filename="input_data/a_an_example.in.txt"):
    """Writes the outputs into the correct format"""
    f = open(filename, "r")
    num_contributors, num_projects = map(int, f.readline().split(" "))
    
    # Create contributors
    contributors = []
    for i in range(num_contributors):
        contributor_params = f.readline().split(" ")
        name = contributor_params[0]
        num_skills = int(contributor_params[1])

        for j in range(num_skills):
            skill_params = f.readline().split(" ")
            skill = skill_params[0]
            skill_level = int(skill_params[1])

        #contributors.append()


if __name__ == '__main__':
    read_inputs()