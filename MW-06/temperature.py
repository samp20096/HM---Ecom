# Start

city_t_count: int = 0
count: int = 0

while count != 5:
    city_t: int = int(input("What is the temperature in your city? "))

    if -50 < city_t < 40:
        print("Your city temperature has been registered.")
        count += 1
        city_t_count += city_t
    else:
        print("Input is not in range. \nMust to be between -50 to 40 celsius! ")

t_ave = city_t_count / 5

print(f"The average of the cities temperature is: {t_ave} Celsius")

# End
