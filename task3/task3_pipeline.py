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

if __name__ == '__main__':
    '''


    int a[N1][N2];

      for (i = 1;i<N1; i++)

          for (j = 0;j<N2; j++)

               a[i][j] = a[i-1][j]+1;
    '''

    if rank == 0:
        a = np.zeros([4, 4],dtype=np.int)
        a[0] = [0, 3, 4, 5]
        send_a_req = comm.isend(a, dest=1)  # at 0 proc send 0 array a  to 1 proc
        send_a_req.wait()
        for j in range(len(a[0])):  # send subarray b[0...4]  to 1 proc
            send_req = comm.Isend([a[0][j],MPI.INT], dest=1, tag=j)
            # send_req.wait()

    else:

        recv_req = comm.irecv(source=rank - 1)
        a = recv_req.wait()
        print("recv a:\n", a)
        recv_data = np.zeros(1,dtype=np.int)
        request = comm.Irecv([recv_data,MPI.INT],source=rank - 1, tag=0)
        for j in range(len(a[0]+1)):

            request.Wait()

            a[rank][j] = recv_data[0] + 1

            print(f"compute a[{a[rank][j]}]:", rank, j)
            request = comm.Irecv([recv_data,MPI.INT],source=rank - 1, tag=j+1)
        if rank < size - 1:
            send_a_second_req = comm.isend(a, dest=rank + 1)
            send_a_second_req.wait()
            for j in range(len(a[0])):
                # send_second_req = comm.isend(a[rank][j], dest=rank + 1, tag=j)
                send_second_req = comm.Isend([a[rank][j], MPI.INT], dest=rank + 1, tag=j)


    
    
