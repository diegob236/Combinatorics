# Combinatorics
----
##### A collection of Python scripts that solve combinatorics problems.
This repository contains some Python scripts to do various tasks, as described below.

Contents:
1. [Erdos-Gallai](#erdos-gallai)
2. [Numnine](#numnine)

## Erdos-Gallai
----
The Erdos-Gallai theorem is used to find whether a series of numbers is a valid degree sequence. The algorithm is as shown:

![\sum^{k}_{i=1}d_i\leq k(k-1)+ \sum^n_{i=k+1} \min(d_i,k)](https://wikimedia.org/api/rest_v1/media/math/render/svg/febd8dee6050a0cf792cff9442935b36db434db8)

`erdosgallai.py` takes a series of nonnegative numbers separated by spaces as its arguments.
It then runs the algorithm to find whether they are a valid degree sequence or not.

## Numnine
----
`numnine.py` counts how many numbers in a specified range contain the digit 9. This range is between 0 and 10^n - 1, where n
is the argument provided. For example, entering 3 as an argument will count numbers from 0 to 999.  
(Soon to be updated to allow for all digits, not just 9!)
