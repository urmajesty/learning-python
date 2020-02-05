#the variable is being assigned
types_of_people = 10

# the variable is being called and assigned to x
x = f"There are {types_of_people} types of people."

#some of the variables are being assigned and others are being called
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#all of the variables are being called
print(x)
print(y)

#The variables are being printed in different format
print(f"I said: {x}")
print(f"I also said: '{y}'")


# False was assigned to hilarious 
hilarious = False

# the variable in joke_evaluation wasnt defined.
joke_evaluation = "Isn't that joke so funny?! {}"

#hilarious was passed in when the joke_evaluation was called.
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# strings being assigned then printed to the console
print(w + e)

#study drill --Break it... I tried removing the "f" and it wouldn't pass in the assignments.