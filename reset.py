import sqlite3

# Connect to the database
conn = sqlite3.connect('facility_manager.db')

# Create a cursor object
cursor = conn.cursor()

# Drop the issues table if it exists
cursor.execute("DROP TABLE IF EXISTS maintenance;")

# Commit and close the connection
conn.commit()
conn.close()


