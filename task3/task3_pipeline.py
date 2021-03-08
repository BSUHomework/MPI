#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: soliva
@Site: 
@file: task3_pipeline.py
@time: 2021/2/4
@desc:
'''
import numpy as np
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# if rank == 0:
#     data = 10 + rank
#     send_req = comm.isend(data, dest=1)
#     send_req.wait()
# else:
#     data = rank * 10  # Data pre-calculation
#     recv_req = comm.irecv(source=rank - 1)
#     recv_data = recv_req.wait()
#     data = recv_data + data  # Get the transmitted data and merge them
#     print("this is rank {} result {}".format(rank, data))
#     if rank < size - 1:
#         send_second_req = comm.isend(data, dest=rank + 1)
#         send_second_req.wait()


# _2d_array =[
#     [0,3,4,5,1,2,3],
#     [1,3,4,1,2,3,4]
#             ]
# np.zeros([5,5])
'''

int a[N1][N2];

  for (i = 1;i<N1; i++)

      for (j = 0;j<N2; j++)

           a[i][j] = a[i-1][j]+1;
'''
N1=4
N2=4
for i in range(size):
    for j in range(N2):
        pass