# Computational Logic Modeling and Transport Analysis of Graphene-Based Nanotransistors

## Overview
This repository hosts a theoretical review and computational study of **Graphene Field-Effect Transistors (GFETs)**. As Silicon CMOS technology approaches its physical scaling limits, 2D materials like Graphene offer a promising path forward.

## Research Objectives
* **Sub-threshold Swing Analysis:** Investigating the limits of switching efficiency.
* **1/f Noise Mitigation:** Analyzing techniques to reduce low-frequency noise in carbon-based devices.
* **Logic Gate Implementation:** Modeling the feasibility of Graphene-based NAND/NOR architectures.

## Tools Used
* **Python:** For data simulation and plotting.
* **MySQL:** For structured storage of device parameters and research data.

## Visualizations

### Simulated Honeycomb Lattice
This plot represents the two-atom basis (Sub-lattice A and B) of a Graphene sheet generated via Python.

![Graphene Lattice](honeycomb_v2.png)


## Data Management
The atomic coordinates are not just plotted; they are exported to a **MySQL database** (`graphene_sim_db`).
* **Table:** `lattice_coordinates`
* **Features:** Unique ID, Sub-lattice classification (A/B), and 2D Spatial Mapping (x, y).
* **Purpose:** To enable persistent storage for large-scale transport simulations.

![Graphene Lattice](database_proof.png)

## Phase 2: Topology and Connectivity
* Successfully implemented a **Nearest-Neighbor search** to identify atomic bonds.
* Visualized the "Hopping Paths" which represent the electron's travel route across the $\pi$-cloud.
* Validated that each Sub-lattice A (Blue) atom connects only to Sub-lattice B (Red) neighbors.

![Graphene Mesh](graphene_mesh.png)
