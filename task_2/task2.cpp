
#include <iostream>
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

float func(float arg) { return arg * arg; }

// float pre_intergrete(float start, float end, float n) { float h, n, intergal
// }

// int intergrete(int number, int n) {
//   int h, b, a;
//   int sub_a, sub_b;
//   int finally;
//   h = (b - a) / 2；
// }

// int main(int argc, char **argv) {
//   MPI_Status status;
//   MPI_Init(NULL, NULL);
//   int size, rank;
//   MPI_Comm_size(MPI_COMM_WORLD, &size);
//   MPI_Comm_rank(MPI_COMM_WORLD, &rank);
//   MPI_Finalize();
// }
int main() { printf("%f", func(2)); }
