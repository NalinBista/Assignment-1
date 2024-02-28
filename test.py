import mysql.connector

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

except mysql.connector.Error as e:
    print(f"Error connecting to MySQL: {e}")

finally:
    # Close the connection
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print('MySQL connection closed')
