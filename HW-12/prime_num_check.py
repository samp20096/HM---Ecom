# bigger then 1

# leaving a sheerit by dividing with 2 or 3

div: int = 2
num_list: list[int] = []
while True:
    x: int = int(input("Number: "))
    num_list.append(x)
    if x < 1:
        print(num_list)
        break
    if div <= x ** 0.5 + 1:
        if x % div != 0:
            print(f"{x} Number is prime")
