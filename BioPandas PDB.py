import biopandas.pdb
import numpy as np
# Load PDB file
pdb_file_path = 'For_Protein/PDB_Files/1qht.pdb'
biopdb = biopandas.pdb.PandasPdb().read_pdb(pdb_file_path)

# Display basic information about the PDB file
print("PDB Header:")
print(biopdb.df['ATOM'].head(10))

# Access specific information about atoms
print("\nAtom Information:")
print("Atom Names:", biopdb.df['ATOM']['atom_name'].head())
print("Residue Names:", biopdb.df['ATOM']['residue_name'].head())
print("Coordinates:")
print(biopdb.df['ATOM'][['x_coord', 'y_coord', 'z_coord']].head())

# Calculate and display the center of mass
coordinates = biopdb.df['ATOM'][['x_coord', 'y_coord', 'z_coord']].values
center_of_mass = np.mean(coordinates, axis=0)
print("\nCenter of Mass:")
print(center_of_mass)