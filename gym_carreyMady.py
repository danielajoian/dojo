jim_s_questions = ["Are you under 14 years old?", "Do you intend to use the sauna?", "Are you a student?", "Are you a woman?", "Are you a man?"]

prices = ["Sorry, i can't let you in", "The price is: 1500 HUF", "The price is: 300 HUF", "The price is: 500 HUF", "The price is: 750 HUF"]

jim_jokes = ["I forgot to post on Facebook I was going to the gym. Now this whole workout was a waste of time.", 
            "If I'm not back in five minutes... just wait longer!", 
            "Somebody help me, I'm being spontaneous!", 
            "The only exercise I have done this month... is running out of money.", 
            "When Chuck Norris goes to the gym the treadmill sweats."]
print("Hello, welcome to Gym Carrey! I'm Jim.")
print("Please only answer with yes or no!")
for i in range(0, len(jim_s_questions) + 1):
    print(jim_s_questions[i])
    print("\n")
    x = input()
    x = x.lower()
    while x != "no" and x != "yes":
        print("Please only answer with yes or no!")
        print(jim_s_questions[i])
        x = input()
        x = x.lower()
    print("\n")
    print(jim_jokes[i])
    print("\n")
    if x == "yes":
        print(prices[i])
        exit()

        
    