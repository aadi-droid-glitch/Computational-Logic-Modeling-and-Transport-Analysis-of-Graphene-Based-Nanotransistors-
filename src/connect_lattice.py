import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

# 1. Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",     # <--- Change this
    password="root", # <--- Change this
    database="graphene_sim_db"
)
cursor = db.cursor()

# 2. Fetch Data using your confirmed column names
cursor.execute("SELECT x_coord, y_coord, atom_type FROM lattice_coordinates")
rows = cursor.fetchall()

x_coords = [r[0] for r in rows]
y_coords = [r[1] for r in rows]
sublattices = [r[2] for r in rows]
points = np.array(list(zip(x_coords, y_coords)))

# 3. Define variables BEFORE the loop (Fixes the NameError)
dist_min = 0.5  
dist_max = 1.6  

plt.figure(figsize=(8, 8))

# 4. Draw the Bonds (The Lines)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = np.linalg.norm(points[i] - points[j])
        
        # Check distance and ensure they are different types (A vs B)
        if dist_min < d < dist_max and sublattices[i] != sublattices[j]:
            plt.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], 
                     color='black', alpha=0.3, linewidth=1.5, zorder=1)

# 5. Draw the Atoms
for i in range(len(points)):
    dot_color = 'blue' if sublattices[i] == 'A' else 'red'
    plt.scatter(points[i][0], points[i][1], c=dot_color, s=100, edgecolors='black', zorder=2)

plt.title("Graphene Lattice: Connected Topology")
plt.gca().set_aspect('equal', adjustable='box')
plt.savefig("graphene_mesh.png")
print("Success! Mesh image saved as graphene_mesh.png")
plt.show()

cursor.close()
db.close()