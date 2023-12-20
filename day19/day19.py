def parse_workflow(workflow):
    name, rules = workflow[:-1].split("{")
    rules = [tuple(rule.split(":")) for rule in rules.split(",")]

    return name, rules

def parse_part(part):
    return {attr.split("=")[0]: int(attr.split("=")[1]) for attr in part[1:-1].split(",")}

def apply_rule(part, rule):
    attrib = rule[0][0]
    sign = rule[0][1]
    value = int(rule[0][2:])

    if sign == "<" and part[attrib] < value:
        return rule[1]
    elif sign == ">" and part[attrib] > value:
        return rule[1]

def process_part(part, workflow_name):
    for rule in workflows[workflow_name][:-1]:
        next = apply_rule(part, rule)
        if next and next == "A":
            return True
        elif next and next == "R":
            return False
        elif next:
            return process_part(part, next)
            
    next = workflows[workflow_name][-1][0]
    if next == "A":
        return True
    elif next == "R":
        return False
    else:
        return process_part(part, next)

if __name__ == "__main__":
    with open("day19.txt", "r") as f:
        workflows, parts = f.read().split("\n\n")
        workflows = {parse_workflow(workflow)[0]: parse_workflow(workflow)[1] for workflow in workflows.split("\n")}
        parts = [parse_part(part) for part in parts.split("\n")]

    accepted = [part for part in parts if process_part(part, "in")]
    print(f"Part 1: {sum([sum(part.values()) for part in accepted])}")