#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: task4_fox_arg.py
@time: 2021/2/5
@desc:
'''
from mpi4py import MPI
import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[1, 2, 3], [4, 5, 6]])
c = b.transpose()
print(a, b)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sqrtsize = np.sqrt(size)

def send_block_AB():
    for i in range(0,size):
        