# SNOW_pbc

This is a rewrite of [pySNOW](https://github.com/nanoMLMS/pySNOW) that focuses more on the ASE Atoms Class.<br>
This is useful for systems with Periodic Boundary Conditions, as KDTree can only consider PBC for neighbor determination in orthogonal unit cells. 
With respect to KDTree, ASE calculator is slower, but it works with any cell : don't use this for large, non-periodic systems. 

The main changes are in neighbor calculations. The rest of the code is almost the same.
