#include <iostream>
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <vector>

using namespace std;
int main(int argc, char **argv) {

  int value = 0;
  int i;
  MPI_Status status;

  MPI_Init(NULL, NULL);

  int size;
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  int rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  int a[3][5] = {{0, 1, 2, 3, 4}, {5, 6, 7, 8, 9}, {10, 11, 12, 13, 14}};

  int n_data = sizeof(a) / sizeof(a[0]);
  int n_row = sizeof(a[rank - 1]) / sizeof(int);
  if (sizeof(a) < size - 1) {

    size = n_data - 1;
    /* code */
  }
  if (rank == 0) {

    int **a;
    a = (int **)malloc((size - 1) * sizeof(int *));
    for (int i = 0; i < n_data; i++) {

      int receive_count = 0;
      MPI_Probe(MPI_ANY_SOURCE, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
      // printf("the probe source is %d\n",status.MPI_SOURCE);
      // printf("the prossess %d is already \n",status.MPI_SOURCE);
      MPI_Get_count(&status, MPI_INT, &receive_count);
      int *number_buf = (int *)malloc(sizeof(int) * receive_count);
      MPI_Recv(number_buf, receive_count, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG,
               MPI_COMM_WORLD, &status);
      for (int i = 0; i < receive_count; ++i) {
        a[status.MPI_SOURCE] = number_buf;
        printf("[%d] ", number_buf[i]);
      }
      printf("\n");

      free(number_buf);
    }

    free(a);
  } else {
    if (rank < n_data + 1) {
      printf("send %d value***************", rank - 1);

      for (int i = 0; i < n_row; ++i) {
        printf("%d ", a[rank - 1][i]);
      }
      printf("\n");
      MPI_Send(a[rank - 1], n_row, MPI_INT, 0, 99, MPI_COMM_WORLD);
    }
  }

  MPI_Finalize();
}
