PLACEHOLDER="[name]"

with open("Input/Names/invited_names.txt") as names:
    # names=names.readlines()-->returns a list of lines with '\n'
    names=names.read().splitlines()
    
with open("Input/Letters/starting_letter.txt") as letter:
    contents=letter.read()
    for name in names:
        new_letter=contents.replace(PLACEHOLDER,name)
        with open(f"Output/ReadyToSend/letter_for_{name}.txt",mode="w") as completed_letter:
            # For each name a letter_for_name.txt file is generated 
            completed_letter.write(new_letter)
