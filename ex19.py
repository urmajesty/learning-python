def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#WHY DO ONLY SOME PRINT LINES HAVE TO BE INDENTED?
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# import random
# def add_num(num1, num2):
#     print(num1 + num2)

# add_num(4, 5)

# x = 4
# y = 5
# add_num(x, y)

# add_num(2 + 2, 1 + 4)

# add_num(2.4, 3.3)

# print(round((2.4 + 3.3), 1))