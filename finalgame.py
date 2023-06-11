from random import randrange
ran = int(randrange(0, 4))
if ran == 1:
    print("What is the missing word?\nTo _ or not to _?")
    word = input("Missing word:")
    if word.lower() == "be":
        print("That's right!")
    else:
        print("That's wrong!")
if ran == 2:
    print("Where art thou _?\n What is the missing word?")
    word = input("Missing word:")
    if word.lower() == "Romeo":
        print("That's right!")
    else:
        print("That's wrong!")
if ran == 3:
    print("What is the missing word?\nAll hail _!")
    word = input("Missing word:")
    if word.lower() == "macbeth":
        print("That's right!")
    else:
        print("That's wrong!")