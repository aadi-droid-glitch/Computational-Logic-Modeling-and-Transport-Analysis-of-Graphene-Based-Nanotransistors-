import mysql.connector

# 1. SETUP THE CONNECTION
# Replace 'your_password' with your actual MySQL password
db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="root",
    database="graphene_sim_db"
)
cursor = db.cursor()

# 2. CREATE THE TABLE (If it doesn't exist)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS lattice_coordinates (
        id INT AUTO_INCREMENT PRIMARY KEY,
        atom_type VARCHAR(1),
        x_coord FLOAT,
        y_coord FLOAT
    )
""")

# 3. THE CALCULATION & EXPORT LOOP
rows, cols = 4, 4
for i in range(rows):
    for j in range(cols):
        # Calculate Sub-lattice A (Blue dots)
        ax, ay = (i * 3 + (j % 2) * 1.5, j * 0.866)
        
        # Calculate Sub-lattice B (Red dots)
        bx, by = (ax + 1, ay)

        # 4. SEND TO DATABASE
        query = "INSERT INTO lattice_coordinates (atom_type, x_coord, y_coord) VALUES (%s, %s, %s)"
        
        cursor.execute(query, ("A", ax, ay)) # Insert Atom A
        cursor.execute(query, ("B", bx, by)) # Insert Atom B

# 5. LOCK IT IN
db.commit()
print(f"Success! {rows * cols * 2} points exported to MySQL.")

cursor.close()
db.close()