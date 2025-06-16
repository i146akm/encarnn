import sqlite3

def remove_duplicates():
    conn = sqlite3.connect('db.sqlite3')
    conn.execute("""
        DELETE FROM cars
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM cars
            GROUP BY car_number
        )
    """)
    conn.commit()
    conn.close()

