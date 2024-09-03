#Start

birthyear1: int = int(input("What is your year of birth? : "))

birthyear2: int = int(input("What is your year of birth? "))

age: int = 2024 - birthyear1
age2: int = 2024 - birthyear2

if birthyear1 < birthyear2:
    print("The older is: ", "\n", birthyear1, "-", age, "\n", birthyear2, "-", age2)
elif birthyear2 < birthyear1:
    print("The older is: ", "\n", birthyear2,"-", age2, "\n", birthyear1, "-", age)
else:
    print("You at the same age! ", "\n", birthyear1,"-", age, "\n", birthyear2, "-", age2)

# Same as bigger num because they got the same script to different job

#End