import mysql.connector
import numpy as np
import pandas as pd

# 1. Database Connection
db = mysql.connector.connect(host="localhost", user="root", password="root", database="graphene_sim_db")
cursor = db.cursor()

# 2. Fetch Data
cursor.execute("SELECT x_coord, y_coord, atom_type FROM lattice_coordinates")
rows = cursor.fetchall()
points = np.array([(r[0], r[1]) for r in rows])
types = [r[2] for r in rows]

# 3. Build the Matrix
n = len(points)
matrix = np.zeros((n, n))
dist_min, dist_max = 0.5, 1.6

for i in range(n):
    for j in range(n):
        if i == j: continue
        d = np.linalg.norm(points[i] - points[j])
        if dist_min < d < dist_max and types[i] != types[j]:
            matrix[i][j] = 1

# 4. Save to CSV
df = pd.DataFrame(matrix)
df.to_csv("../docs/adjacency_matrix.csv", index=False)
print("Simulation Data Finalized: Adjacency Matrix saved to /docs.")
db.close()