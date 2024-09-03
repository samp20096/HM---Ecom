#Start

first_num: float = float(input("Put your first number here: "))

second_num: float = float(input("Put your second number here: "))
""""
Optional: for making it always above 0
if first_num or second_num < 0:
    print("Numbers have to be above 0 !")
else:
    diff: float = first_num - second_num
"""
diff: float = first_num - second_num

print("Your difference between your number is:", diff)

#End