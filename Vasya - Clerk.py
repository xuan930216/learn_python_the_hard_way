# The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollars bill. An "Avengers" ticket costs 25 dollars.

# Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

# Can Vasya sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?

# Return YES, if Vasya can sell a ticket to each person and give the change with the bills he has at hand at that moment. Otherwise return NO.

# ###Examples:

# ### Python ###

# tickets([25, 25, 50]) # => YES 
# tickets([25, 100]) 
#          # => NO. Vasya will not have enough money to give chan
def tickets(people):
    a_25  = 0
    a_50 = 0
    for i in people:
        if i == 25:
            a_25 += 1
        elif i == 50:
            a_25 -= 1
            a_50 +=1
        else:
            if a_50 == 0 and a_25>=3:
                a_25 -=3
            else:
                a_25 -=1
                a_50 -=1
        if a_25<0 or a_50<0:
            return "NO"
    return "YES"