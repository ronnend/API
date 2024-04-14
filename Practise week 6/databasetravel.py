import sqlite3
import time


def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn, conn.cursor()


def create_bookings_table(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    id INTEGER PRIMARY KEY,
                    client_name TEXT,
                    hotel_name TEXT,
                    check_in_date INTEGER,
                    check_out_date INTEGER,
                    created_at INTEGER
                    )''')
    print("Bookings table created successfully.")


def insert_booking(cursor, client_name, hotel_name, check_in_date, check_out_date):
    cursor.execute('''SELECT id FROM bookings 
                    WHERE client_name = ? AND hotel_name = ? AND check_in_date = ? AND check_out_date = ?''', 
                   (client_name, hotel_name, check_in_date, check_out_date))
    existing_booking = cursor.fetchone()
    
    if not existing_booking:
        created_at = int(time.time())
        cursor.execute('''INSERT INTO bookings (client_name, hotel_name, check_in_date, check_out_date, created_at)
                        VALUES (?, ?, ?, ?, ?)''', (client_name, hotel_name, check_in_date, check_out_date, created_at))
        print("New booking inserted successfully.")
    else:
        print("Booking already exists.")

def get_bookings_current_year(cursor):
    current_year = time.localtime().tm_year
    cursor.execute('''SELECT * FROM bookings 
                    WHERE strftime('%Y', datetime(check_in_date, 'unixepoch')) = ?''', (str(current_year),))
    return cursor.fetchall()

def search_bookings_by_client(cursor, client_name):
    cursor.execute('''SELECT * FROM bookings 
                    WHERE client_name LIKE ?''', ('%' + client_name + '%',))
    return cursor.fetchall()


db_file = "travel_booking_system.db"


conn, cursor = create_connection(db_file)

create_bookings_table(cursor)


insert_booking(cursor, "John Doe", "Hotel ABC", int(time.time()), int(time.time()) + 86400 * 3)  # 3 days from now

print("Retrieving bookings for the current year...")
bookings_current_year = get_bookings_current_year(cursor)
for booking in bookings_current_year:
    print(booking)


search_query = input("Enter client name to search bookings (type 'exit' to quit): ")
if search_query.lower() == 'exit':
    print("Exiting the program...")
else:
    search_results = search_bookings_by_client(cursor, search_query)
    if search_results:
        print("Search results:")
        for booking in search_results:
            print(booking)
    else:
        print("No bookings found for the client:", search_query)


print("Closing connection to the database...")
conn.close()
