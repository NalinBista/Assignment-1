import mysql.connector
import hashlib

# Set up the connection parameters
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'student_management_system',
    'auth_plugin': 'mysql_native_password',
    'raise_on_warnings': True
}

try:
    # Establish a connection to the MySQL server
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Connected to MySQL database')

    # Perform database operations here

    # Create a cursor object
    cursor = conn.cursor()

    # Hashing the password using SHA-1
    password = "admin"
    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    # Data to be inserted
    data_to_insert = ('AD10000', 'admin', hashed_password, 'superadmin')

    # SQL statement for insertion
    insert_query = "INSERT INTO `login_details` VALUES (%s, %s, %s, %s)"

    # Execute the insertion
    cursor.execute(insert_query, data_to_insert)

    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

    print("Data inserted successfully into login_details table!")

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('MySQL connection closed')
