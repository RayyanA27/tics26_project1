name = input("Welcome player. What is your name?")

print(name, "You are being chased by zombies. The zombies are closing in on you, but you have three options. You can choose to run, fight, or hide")

decision = input("What will you do. run, fight, or hide?")

if decision == "run":
    print("You widened the distance between you and the zombies.")




elif decision == "fight":
    print("You hit a few of the zombies, but there were too many for you to handle. At least you had an honorable death. R.I.P")


elif decision == "hide": ("You successfully hid from the zombies")


else:
    print("Invalid decision. You died because you waited for the zombies to catch up")



