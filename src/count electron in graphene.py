import mysql.connector
import numpy as np

# 1. Database Connection
db = mysql.connector.connect( host="localhost", user="root", password="root", database="graphene_sim_db")
cursor = db.cursor()

# 2. Fetch coordinates and types
cursor.execute("SELECT id, x_coord, y_coord, atom_type FROM lattice_coordinates")
rows = cursor.fetchall()

ids = [r[0] for r in rows]
points = np.array([(r[1], r[2]) for r in rows])
types = [r[3] for r in rows]

# 3. Connection Counter Logic
dist_min, dist_max = 0.5, 1.6
print(f"--- Graphene Integrity Report ---")
errors = 0

for i in range(len(points)):
    connections = 0
    for j in range(len(points)):
        if i == j: continue
        
        d = np.linalg.norm(points[i] - points[j])
        # Check if they are neighbors and different types
        if dist_min < d < dist_max and types[i] != types[j]:
            connections += 1
    
    if connections != 3:
        # Note: Edge atoms will naturally have fewer than 3
        print(f"Atom ID {ids[i]} ({types[i]}): {connections} connections (Potential Edge/Defect)")
        if connections == 0: errors += 1
    else:
        # Optional: uncomment to see every atom's success
        # print(f"Atom ID {ids[i]}: OK")
        pass

print(f"---------------------------------")
print(f"Lattice Check Complete. {errors} isolated atoms found.")
db.close()