import sqlite3, os, time

def print_color(message, color) -> None:
    """
    coloring the massage to print
    :param message: massage to color
    :param color: what color
    :return: None
    """
    match color:
        case "red":
            COLOR = '\033[31m'
            RESET = '\033[0m'
        case "blue":
            COLOR = '\033[34m'
            RESET = '\033[0m'
        case "green":
            COLOR = '\033[32m'
            RESET = '\033[0m'
        case "yellow":
            COLOR = '\033[33m'
            RESET = '\033[0m'
        case "orange":
            COLOR = '\033[38;5;214m'
            RESET = '\033[0m'
    print(f"{COLOR}{message}{RESET}")

def create_db(file_name) -> None:
    """
    asks for file name for creation if not exist
    :param file_name:
    :return: None
    """
    if os.path.exists(file_name):
        os.remove(file_name)
        print("\033[34mFile exist, removed and created new\033[0m")
    else:
        conn = sqlite3.connect(file_name)
        conn.close()

def execute_modify_query(cursor, conn, query, params = None) -> None:
    """
    database modification
    :param cursor: query execution
    :param conn: commit in database
    :param query: execution query
    :param params: None/parameters
    :return: None
    """
    try:
        if params:
            cursor.execute(query, params) # with parameters
        else:
            cursor.execute(query) # without parameters
        conn.commit()
    except sqlite3.IntegrityError as e:
        print_color(f"Integrity Error: {e}", "red")
    except sqlite3.Error as e:
        print_color(f"Database Error: {e}", "red")
    except Exception as e:
        print_color(f"Unexpected error {e}", "red")

def execute_read_query(cursor, query) -> list:
    """
    fetching data from database and returns list with fetched data
    :param cursor: query execution
    :return: list
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    result: list = [dict(row) for row in rows]
    return result

def garage_options() -> int:
    """
    bringing the options to the user to select service
    :return: int
    """
    print_color("Pick from options: ", "blue")
    print("1. New car registration for treatment\n"
          "2. End of treatment\n"
          "3. Take car out of garage\n"
          "4. Check for garage load\n"
          "5. Exit")
    try:
        user_pick: int = int(input("What is your service? "))
        return user_pick
    except ValueError:
        print_color("Invalid input, try again with numbers only.", "red")
        time.sleep(3)

# option 1
def new_car(cursor, conn) -> None:
    """
    getting info from the user and inserting it to the database
    :param cursor: query execution
    :param conn: commit in database
    :return: None
    """
    while True:
        print_color("-" * 25, "blue")
        print("New car register details:")
        car_number: int = int(input("Car number: "))
        # if car exist in database - print oops message
        if execute_read_query(cursor, f"SELECT * FROM GARAGE WHERE car_number like '{car_number}';"):
            print_color("Oops, the car is already registered", "orange")
            time.sleep(1)
            print_color("You back to options page in 3 seconds...", "yellow")
            time.sleep(3)
            break
        car_problem: str = input("Car problem: ")
        owner_ph: int = int(input("Owner phone number: "))
        owner_ph: str = str(owner_ph)[:3] + "-" + str(owner_ph)[3::] # adding "-" after the third number
        # ----- insert query
        insert_query = f"INSERT INTO garage (car_number, car_problem, owner_ph) VALUES (?, ?, ?);"
        execute_modify_query(cursor, conn, insert_query, (car_number, car_problem, owner_ph))
        print_color(f"Car number {car_number} inserted successfully", "blue")
        time.sleep(1)
        print_color("You back to options page in 3 second...", "green")
        time.sleep(3)
        break

# option 2
def end_of_treatment(cursor, conn) -> None:
    """
    accepting the end of treatment of a car by car number
    or
    checking if already finished the treatment
    True(1) - Finished
    False(0) - Not finished
    :param cursor: query execution
    :param conn: commit in database
    :return: None
    """
    while True:
        print_color("-" * 25, "blue")
        try:
            car_number: int = int(input("Car Number: "))
        except ValueError:
            print_color("Invalid number, Try again with numbers only!", "red")
        check_car_result: list = execute_read_query(cursor, f"SELECT * FROM garage WHERE car_number LIKE {car_number};")
        if check_car_result:
            if check_car_result[0]["fixed"] == 0:
                update_query = f"UPDATE garage SET fixed = 1 WHERE car_number LIKE {car_number};"
                execute_modify_query(cursor, conn, update_query)
                print_color(f"Car number {car_number} updated", "blue")
                time.sleep(1)
            else:
                print_color(f"Car number {car_number} already finished treatment", "blue")
                time.sleep(1)
        else:
            print_color(f"Car number {car_number} not in the garage.", "orange")
            time.sleep(1)
        break
    print_color("You back to option page in 3 seconds...", "green")
    time.sleep(3) # delaying the function to let the user get the message

# option 3
def out_of_garage(cursor, conn) -> None:
    """
    checking if the car is out of the garage
    if the car is not in the garage, deleting its row from the database
    :param cursor: query execution
    :param conn: commit in database
    :return: None
    """
    while True:
        print_color("-" * 25, "blue")
        try:
            car_number: int = int(input("Car number: "))
        except ValueError:
            print_color("Invalid number, Try again with numbers only!", "red")
        check_car_result: list = execute_read_query(cursor, f"SELECT * FROM garage WHERE car_number LIKE {car_number};")
        if check_car_result:
            if check_car_result[0]["fixed"] == 1:
                car_out: str = input("Car is out of garage[Y/N]? ").capitalize()
                while True:
                    if car_out == "Y":
                        delete_car_query = f"DELETE FROM garage WHERE car_number LIKE {car_number}"
                        execute_modify_query(cursor, conn, delete_car_query)
                        owner_ph = check_car_result[0]["owner_ph"]
                        print_color(f"Contact car number {car_number} owner:\nPhone number: {owner_ph}", "blue")
                        break
                    elif car_out == "N":
                        print_color("Take the car out of garage first.", "orange")
                        break
                    else:
                        print_color("Invalid input, try Y for Yes or N for No!", "red")
            else:
                print_color(f"Car number {car_number} is not finished treatment yet.", "yellow")
        else:
            print_color(f"Car number {car_number} is not in the garage.", "red")
        break
    time.sleep(2)
    print_color("You back to option page in 3 seconds...", "green")
    time.sleep(3)

# option 4
def check_garage_load(cursor) -> None:
    """
    checking how many cars are not finished treatment and bringging the amount to the user
    :param cursor: query execution
    :return: None
    """
    print_color("-" * 25, "blue")
    load_result: int = len(execute_read_query(cursor, "SELECT * FROM garage WHERE fixed LIKE 0"))
    print_color(f"Garage load: {load_result} cars in queue", "yellow")
    time.sleep(2)
    print_color("You back to option in 3 seconds...", "green")
    time.sleep(3)

# option 5
def exit_program() -> bool:
    """
    when user want to exit, it will ask the user if he sure,
    if he is so he exits the program,
    if not sure, he will sent back to options page
    :return: bool
    """
    while True:
        flag: bool = True
        user_input: str = input("Are you sure you want to exit[Y/N]? ").capitalize()
        if user_input == "Y":
            print_color("The program will close in 3 seconds...", "blue")
            time.sleep(3)
            return flag
        elif user_input == "N":
            print_color("You back to option page in 3 seconds...", "green")
            time.sleep(3)
            flag = False
            return flag
        else:
            print_color("Invalid input, try Y for Yes or N for No!", "red")
