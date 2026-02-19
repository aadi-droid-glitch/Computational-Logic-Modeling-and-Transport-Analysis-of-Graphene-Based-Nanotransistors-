import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="****",
    database="graphene_sim_db"
)
cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS lattice_coordinates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        atom_type VARCHAR(1),
        x_coord FLOAT,
        y_coord FLOAT
    )
""")

rows, cols = 4, 4
for i in range(rows):
    for j in range(cols):
     
        ax, ay = (i * 3 + (j % 2) * 1.5, j * 0.866)
        
      
        bx, by = (ax + 1, ay)
    
       
        query = "INSERT INTO lattice_coordinates (atom_type, x_coord, y_coord) VALUES (%s, %s, %s)"
        
        cursor.execute(query, ("A", ax, ay)) # Insert Atom A
        cursor.execute(query, ("B", bx, by)) # Insert Atom B


db.commit()
print(f"Success! {rows * cols * 2} points exported to MySQL.")

cursor.close()
db.close()
