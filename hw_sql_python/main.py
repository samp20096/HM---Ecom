import utils, sqlite3

file_name = "garage_db.db"

utils.create_db(file_name) # creating the db

conn = sqlite3.connect(file_name) #file connector
conn.row_factory = sqlite3.Row # column access
cursor = conn.cursor() # cursor for execute

# ------ table create query
create_table_query = """
CREATE TABLE garage (
    fix_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_number TEXT UNIQUE NOT NULL, 
    car_problem TEXT NOT NULL, 
    fixed BOOLEAN DEFAULT FALSE, 
    owner_ph TEXT NOT NULL
);
"""
utils.execute_modify_query(cursor, conn, create_table_query)

# ------- insert to garage table query
insert_query = """
INSERT INTO garage (car_number, car_problem, fixed, owner_ph) VALUES
('23', 'Engine overheating after long drives', TRUE, '555-1023'),
('34', 'Brake pads worn out, needs replacement', TRUE, '555-1034'),
('30', 'Check engine light on, possible sensor issue', TRUE, '555-1030'),
('24', 'Battery drains overnight, needs diagnosis', FALSE, '555-1024'),
('3', 'Strange noise from suspension when turning', FALSE, '555-1003');
"""
utils.execute_modify_query(cursor, conn, insert_query)

# -------- main script

while True:
    user_pick = utils.garage_options()

    if user_pick == 1:
        utils.new_car(cursor, conn)
        continue
    elif user_pick == 2:
        utils.end_of_treatment(cursor, conn)
        continue
    elif user_pick == 3:
        utils.out_of_garage(cursor, conn)
        continue
    elif user_pick == 4:
        utils.check_garage_load(cursor)
        continue
    elif user_pick == 5:
        flag_check: bool = utils.exit_program()
        if flag_check:
            break
        else:
            continue
    else:
        utils.print_color("Invalid input, pick from options!", "red")
        continue