devicelist = ["PC", "Phone", "Ipad", "Tablet",]
health = int(100)

device = input("What device are you playing on?", devicelist)
name = input("Welcome", device, "user", "What is your name?")

print(name, "You are being chased by zombies. The zombies are closing in on you, but you have three options. You can choose to run, fight, or hide")

decision = input("What will you do. run, fight, or hide?")

if decision == "run":
    print("You widened the distance between you and the zombies.")
    print("Health:", health)

    decision2 = input("What will you do. run, fight, or hide")

    if decision2 == "run":
        print("You exerted too much energy. Eventually the zombies caught up, and you perished. ")
        health2 = health - 100
        print("Health:", health2)
        ending = print("Better luck next time!")

    if decision2 == "fight":
        print("You could not handle the sheer amount of zombies. You gave a valiant effort.")
        health2 = health - 100
        print("Health:", health2)
        ending = print("At least you made it this far!")
        
    if decision2 == "hide":
        print("You were not detected by the zombies. Good work.")
        print("Health:", health)


        


elif decision == "fight": 
    print("There were too many zombies to fight off. You died an honorable death. R.I.P")
    health2 = health - 100
    print("Health:", health2)


elif decision == "hide": 
    print("You successfully hid from the zombies")
    print("Health:", health)


else:
    print("Invalid decision. You died because you waited for the zombies to catch up")
    health2 = health - 100
    print(health2)
    ending = print("Game Over!")



