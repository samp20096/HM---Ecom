# Start

while True:
    f_num: int = int(input("First number: "))
    s_num: int = int(input("Second number: "))
    t_num: int = int(input("Third number: "))

    is_in_range = (0 <= f_num <= 10) and (10 <= s_num <= 60) and (60 <= t_num <= 100)
    dive = (f_num + s_num + t_num) / 3

    if s_num == dive and is_in_range == True:
        print(f"The diversion is: {dive}")
        break
    else:
        print("Invalid input, try again!")

# End
