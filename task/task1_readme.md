## Gather data

## install

Step1 install python3 for anaconda

Then install openmpi

Step2 used pip install mpi4py

## introduction 

The purpose of this task is to collect information about each process and output a matrix, which is arranged by rank id



## Main Code

```python
data_main = comm.gather(data, root=0)
if __name__ == "__main__":


    if comm_rank==0:
        #create a matrix for receiving data range by rank id

        print("rank:{} Receiving {}".format(comm_rank, data))
        print("input:\n",all_data)
        new_data = list(filter(None,data_main))
        new = np.matrix(new_data)
        print("output:\n",new)

    else:
        print("rank:{} Receiving {}".format(comm_rank,data))
```

## output	

```shell
# soliva @ solivadeMacBook-Pro in ~/Desktop/Homework/MPI/work [9:55:43]
$ mpirun -np 5 python message_collect.py
rank:1 Receiving [5, 6, 7, 8, 9]
rank:3 Receiving [15, 16, 17, 18, 19]
rank:4 Receiving None
rank:2 Receiving [10, 11, 12, 13, 14]
rank:0 Receiving [0, 1, 2, 3, 4]
input:
 [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]
output:
 [[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
```

