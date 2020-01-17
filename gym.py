
print("Hello! My name is Jim. Welcome to the gym")
print("Please answer yes or no to the following questions: ")


questions =["Are you under 14 years old?",
            "Do you want to use the sauna?",
            "Are you a student?",
            "Are you a woman?",
            "Are you a man?"]

price = ["Sorry, i can't let you in.",
         "The price is 1500",
         "The price is 300",
         "The price is 500",
         "The price is 750"]

for i in range(0, len(questions) + 1):
    print(questions[i])
    print("\n")
    x = input()
    x = x.lower()
    while x != "no" and x != "yes":
        print("Please only answer with yes or no!")
        print(questions[i])
        x = input()
        x = x.lower()
    print("\n")
    if x == "yes":
        print(price[i])
        print("Here is your ticket: ")
        print('''  
| | (_)    | |      | |  
| |_ _  ___| | _____| |_ 
| __| |/ __| |/ / _ \ __|
| |_| | (__|   <  __/ |_ 
 \__|_|\___|_|\_\___|\__| 
 ''')
        exit()
