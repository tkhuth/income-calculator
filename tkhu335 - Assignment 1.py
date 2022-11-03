"""
Taiyo Khuth tkhu335
"""
import random
def generate_goal(valid_choices, n):
    """Given a string of letters and an integer value n,
    return a string containing a random selection of n characters
    selected from the letters in valid_choices"""
    goal = ""
    for i in range(0, n):
        goal += random.choice(valid_choices)    
    return goal

def display_board(header, bottom_line, goal):
    """Display the Mastermind board"""
    print(header)
    for i in range(0, 10):
        print("....||....")
    print(bottom_line)
    print(f"Goal: {goal}")


def new_board(header, body_line, bottom_line, count, goal):
    if count != 10:
        print(header)
        print(* body_line, sep="\n")
        print(bottom_line)
        print(f"Goal: {goal}")
    else:
        print(header)
        print(* body_line, sep="\n")
        print(bottom_line)


def change_board(header, body_line, code_list, bottom_line, prompt, goal, count):
    if count != 11:
        index = count - 1
        answer = checking_get_prompt(header, body_line, code_list, bottom_line, prompt, count, goal)
        code_list.append(prompt)
        body_line[index] = code_list[index] + ("||" + answer)


def get_prompt(count):
    while True:
        prompt = input(str(count) + " (roygbv): ")
        if len(prompt) == 4:
            if prompt[0] in "roygbv" and prompt[1] in "roygbv" and prompt[2] in "roygbv" and prompt[3] in "roygbv":
                return prompt
def checking_get_prompt(header, body_line, code_list, bottom_line, prompt, count, goal):
    first_index = ""
    index = count - 1
    prompt_list = list(prompt)
    for i in range(len(prompt_list)):
        if prompt_list[i] == goal[i]:
            first_index += "B"
    if len(first_index) != 4:
        value = 4 - len(first_index)
        first_index += (value * ".")
    return first_index
def main():
    """Execute the Mastermind program"""
    header = "----------\nCode||Mark\n----------"
    body_line = ["....||....", "....||....", "....||....", "....||....", "....||....",
                 "....||....", "....||....", "....||....", "....||....", "....||...."]
    bottom_line = "----------"
    code_list = []
    valid_choices = "roygbv"
    n = 4
    goal = generate_goal(valid_choices, n)
    display_board(header, bottom_line, goal)
    count = 1
    while count != 11:
        prompt = get_prompt(count)
        change_board(header,body_line, code_list, bottom_line, prompt, goal, count)
        new_board(header, body_line, bottom_line, count, goal)
        count += 1

    print("Done")

