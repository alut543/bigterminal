import time
import random

print(" 👤 Idiotic Terminal 👤 ")
print("\n")
print("\n")
print("Would you like to install the Idiotic Terminal? (y/n)")
time.sleep(3)
downloadline = input("> ")
if downloadline == "y":
    print("What is your username?")
    usernameline = input("> ")
    
    while True:
        cmdline = input("root@" + usernameline + "> ")
        if cmdline == "help":
            print("A star next to a command indicates that the command is disabled. (*)")
            print("\n")
            print("help - Shows the available commands.")
            print("rps - Opens a rock paper scissors game.")
            print("convo - Opens a quick convo")
            print("dice - Opens a quick dice game (you can use this for board games if you dont have a dice lmao)")
            print("calc or calculator - if you are trying to solve simple equations")
            print("echo - Directly copies what you say. ")
            print("*survey - starts a small survey")
            print("*restart - Restarts CMD.")
        elif cmdline == "rps":
            print("You are in a rock, paper, scissors game.")
            print("Choose your action. (rock, paper, scissors)")
            rpsline = input("> ")
            if rpsline == "rock":
                print("You chose rock.")
                print("AI is thinking...")
                time.sleep(3)
                list = ["Rock.", "Paper.", "Scissors."]
                print("AI Chose " + random.choice(list))
            elif rpsline == "paper":
                print("You chose paper.")
                print("AI is thinking...")
                time.sleep(3)
                list = ["Rock.", "Paper.", "Scissors."]
                print("AI Chose " + random.choice(list))
            elif rpsline == "scissors":
                print("You Chose Scissors.")
                print("AI is thinking...")
                time.sleep(3)
                list = ["Rock.", "Paper.", "Scissors."]
                print("AI Chose " + random.choice(list))
        elif cmdline == "convo":
            greetinglist = ["Hello, how are you?", "What's good?", "How are you?"]
            print(random.choice(greetinglist))
            responsehowareyou = input("(Good, Bad, Ok) > ")
            if responsehowareyou == "Bad":
                responsewhylist = ["Why?, What's wrong?", "Is something wrong? You can tell me."]
                print(random.choice(responsewhylist))
                respondto = input("> ")
                responsewhateveritislist = ["Well whatever it is, forget about it. It will become better in the future", "Whatever it is, i don't care bro."]
                print(random.choice(responsewhateveritislist))
            elif responsehowareyou == "Ok":
                responsewhylist = ["Why?, What's wrong?", "Is something wrong? You can tell me."]
                print(random.choice(responsewhylist))
                respondto = input("> ")
                responsewhateveritislist = ["Well whatever it is, forget about it. It will become better in the future", "Whatever it is, i don't care bro."]
                print(random.choice(responsewhateveritislist))
            elif responsehowareyou == "Good":
                print("Well it's great to hear that, since this idiot doesn't want to waste time making a whole convo, he wont do the rest.")
        elif cmdline == "dice":
            list = ["1", "2", "3", "4", "5", "6"]
            print("You rolled a " + random.choice(list))
        elif cmdline == "calc":
            print("Calculator:")
            calcline = input ("> ")
            if calcline == "addition":
                setnumaddfirst = int(input("Enter your first number > "))
                setnumaddsecond = int(input("Enter your second number. > "))
                time.sleep(2)
                print(setnumaddfirst + setnumaddsecond)
            elif calcline == "addition":
                setnumsubfirst = int(input("Enter your first number. > "))
                setnumsubsecond = int(input("Enter your second number. > "))
                time.sleep(2)
                print(setnumsubfirst - setnumaddsecond)
            elif calcline == "multiplication":
                setnummultfirst = int(input("Enter your first number > "))
                setnummultsecond = int(input("Enter your second number > "))
                time.sleep(2)
                print(setnummultfirst * setnummultsecond)
            elif calcline == "divison":
                setnumdivfirst = int(input("Enter your first number > "))
                setnumdivsecond = int(input("Enter your second number > "))
                print(setnumdivfirst / setnumdivsecond)            
        elif cmdline == "echo":
            print("Type in what you want the computer to say.")
            copy = input("> ")
            print(copy)
        elif cmdline == "restart":
            print("This command is disabled, future updates are made to the teriminal, please try again after the title of the Idiotic terminal has a VX.X next to it.")
        elif cmdline == "survey":
            print("This command is disabled, future updates are made to the teriminal, please try again after the title of the Idiotic terminal has a VX.X next to it.")
        else:
            print("Sorry, such command doesn't exist in our ciricullum. Please type help for help.")
