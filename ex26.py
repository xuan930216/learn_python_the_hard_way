from sys import argv

# print("How old are you?", end=" ")
# age = input()
# print("How tall are you?", end = " ")
# tall = input()
# print("How much do you weight?", end = " ")
# weight = input()

# print(f"So, you are {age} old, {tall} tall and {weight} heavy.")
# script, filename = argv
# text = open(filename)
# print(f"Here's your file: {filename}")
# print(text.read())

# print("Type the filename again:")
# file_again = input("> ")

# txt_again = open(file_again)

# print(txt_again.read())

# print('Let\'s practice everything.')
# print("""You\'d need to know \'bout escapes 
#       with \\ that do \n newlines and \t tabs.
#     """)

# poem = """
# \tThe lovely world
# with logic so firmly planted
# cannot discern \n the needs of love
# nor comprehend passion from intuition
# and requires an explanation
# \n\t\twhere there is none.
# """

# print("--------------")
# print(poem)
# print("--------------")

# five = 10 -2 -3
# print(f"This should be five: {five}")

# def secret_formula(started):
#     jelly_beans = started * 500
#     jars = jelly_beans / 1000
#     crates = jars / 100
#     return jelly_beans, jars, crates

# star_point = 10000
# beans, jars, crates = secret_formula(star_point)
# print("we'd have {} beans, {} jars, and {} crates".format(beans,jars,crates))

people = 20
cates = 30
dogs = 15


if people < cates:
    print("Too many cats! The world is doomed!") 

if people > cates:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")
