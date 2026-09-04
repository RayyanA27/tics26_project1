devicelist = ["PC", "Phone", "Ipad", "Tablet"]
rating = [1/3, 2/3, 3/3]
health = (100)

device = input(f"What device are you playing on?{devicelist}")
name = input(f"Welcome {device} user: What is your name?")

print([name], f"You are being chased by zombies. The zombies are closing in on you, but you have three options. You can choose to run, fight, or hide")

def health2(y):
     global health
     return health-y

decision = input("What will you do. run, fight, or hide?")

alive = True

while alive == True:


    if decision == "run":
        print("You widened the distance between you and the zombies.")
        print(f"Health:, {health}")


        decision2 = input("What will you do. run, fight, or hide?")


        if decision2 == "run":
            print("You exerted too much energy. Eventually the zombies caught up, and you perished. ")
            health = health2(100)
            print(f"Health:, {health}")
            ending = print("Better luck next time!")
            alive = False

        if decision2 == "fight":
            print("You could not handle the sheer amount of zombies. You gave a valiant effort.")
            health = health2(100)
            print(f"Health:, {health}")
            ending = print("At least you made it this far!")
            alive = False
            
        if decision2 == "hide":
            print("You were not detected by the zombies. Good work. You survived!")
            print(f"Health:, {health}")


            


    elif decision == "fight": 
        print("There were too many zombies to fight off. You died an honorable death. R.I.P")
        health = health2(100)
        print(f"Health:, {health}")
        alive = False


    elif decision == "hide": 
        print("You successfully hid from the zombies. Good work. You survived!")
        print(f"Health:, {health}")


        decision2 = input("What will you do. run, fight, or hide?")


        if decision2 == "run":
                print("You exerted too much energy. You were a warrior though!")
                health= health2(100)
                print(f"Health:, {health}")
                alive = False

        if decision2 == "fight":
                print("You fought off all of the zombies. Good work. You survived!")
                print(f"Health:, {health}")

        if decision2 == "hide":
                print("You were caught by the zombies. You can't hide forever!")
                health = health2(100)
                print(f"Health:, {health}")
                alive = False


    else:
        print("Invalid decision. You died because you waited for the zombies to catch up")
        health = health2(100)
        print(f"Health:, {health}")
        print("Game Over!")
    print(f"Out of respect for Jayden Daniels, our rating will not be out of 5. Instead it will be out of 3. Rate the game., {rating}, Thank you, {name}, for playing.")
