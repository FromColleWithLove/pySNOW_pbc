import numpy as np
from snow.misc.constants import mass
from ase.neighborlist import neighbor_list
from ase import Atoms
import os 

rescale = (1 + np.sqrt(2)) / 2

def pair_list(atoms : Atoms , cut_off: float = None) -> list:
    print("Using ase version of neighbors")
    pairs = []
    neighbors = neighbor_list("ij",atoms,cutoff=cut_off,self_interaction=False)
    for i,j in zip(neighbors[0],neighbors[1]):
        if i >= j :
            pairs.append([i, j])
    return pairs

def nearest_neighbours(atoms : Atoms, cut_off: float = None) -> list:
    print("Using ase version of neighbors")
    sqrt_2 = np.sqrt(2)
    natoms = len(atoms.positions)
    neigh = [ [] for _ in range(natoms) ]
    pairs = pair_list(atoms,cut_off)
    for p in pairs:
        neigh[p[0]].append(p[1])
        if p[0] != p[1] :
            neigh[p[1]].append(p[0])
    return neigh

def coordination_number(atoms : Atoms , cut_off : float = None ):
    print("Using ase version of neighbors")
    neigh = nearest_neighbours(atoms,cut_off)
    natoms = len(atoms.positions)
    coord_numb=[ ]
    for neighlist in neigh:
        coord_numb.append(len(neighlist))
    return neigh, coord_numb
