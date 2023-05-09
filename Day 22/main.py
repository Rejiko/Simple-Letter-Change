name_list = []

with open("./Input/Names/invited_names.txt") as invite_names:
    for name in invite_names:
        name_list.append(name.strip())


with open("./Input/Letters/starting_letter.txt") as letter:
    letter_contets = letter.read()

    for name in name_list:
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
            new_letter = letter_contets.replace("[name]", name)
            completed_letter.write(new_letter)