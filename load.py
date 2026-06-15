import sqlite3
from config import DB_NAME


def load_to_db(df):

    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS characters(
                       id INTEGER PRIMARY KEY,
                       name TEXT,
                       status TEXT,
                       species TEXT,
                       origin TEXT
                       )
                       """)
        

        for _, row in df.iterrows():

            sql = """INSERT INTO characters(id,name,status,species,origin)
            VALUES (?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET
            name = excluded.name,
            status = excluded.status,
            species = excluded.species,
            origin = excluded.origin"""

            # This executes INSIDE the loop, passing the 5 variables safely
            cursor.execute(sql, (
                row['id'], 
                row['name'], 
                row['status'], 
                row['species'], 
                row['origin']
            ))
        conn.commit()

    except sqlite3.Error as e:
        print(f"DATABASE ERROR : {e}")

    finally:
        cursor.close()
        conn.close()