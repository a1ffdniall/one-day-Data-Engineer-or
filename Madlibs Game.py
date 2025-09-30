#Madlibs game
#This is a simple madlibs game that prompts the user for various types of words 
#and then generates a funny story using those words.

print("Welcome to the Madlibs Game!")
print("Please provide the following words:")

adjective1 = input("Enter an adjective (a describing word): ")
noun1 = input("Enter a noun (person): ")
adjective2 = input("Enter another adjective (a describing word): ")
verb1 = input("Enter a verb ending with 'ing' (action word): ")
adjective3 = input("Enter one more adjective (a describing word): ")

print("\nHere's your funny story:\n")
story = f"Once upon a time, there was a {adjective1} {noun1} who loved {verb1}. "\
        f"One day, he found a/an {adjective2} treasure chest filled with {adjective3} jewels. "\
        "And he lived happily ever after!\n"
print(story)