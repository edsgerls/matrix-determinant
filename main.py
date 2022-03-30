import math
from math import nan
import random
import numpy as np


def check_matrix(A):

    m, n = np.shape(A)
    stop = False
    perm_count = 0

    # First, ensure there is no zero row or column
    for i in range(n):
        if np.allclose(A[i, :],np.zeros((n,n))):
            stop = True
            break
    for j in range(n):
        if np.allclose(A[:, j], np.zeros((n, n))):
            stop = True
            break

    # Second, ensure A.diagonal does not contain a single zero
    if not stop:
        # ~ (Todos en la diag son TRUE?), si supera 500 permutaciones, es que no existe cfg de la matrix que lo permita
        while not np.all(A.diagonal()) and perm_count < 500:       #TODO podrias buscar que indice en la diag es cero y ese hacerle swap
            idx = random.randint(1, n - 1)  # FIXED: We cannot select index 0, so choose from  1 to n-1
            A[[0, idx]] = A[[idx, 0]]  # Swap row 0 with row idx
            perm_count += 1

    return stop, perm_count


def main():

    A = np.array([[0,2,5,4],[1,0,-1,3],[0,0,0,-1],[2,3,5,0]], dtype=float)
    A = np.array([[0, 0, 0, 0], [1, 0, -1, 3], [0, 0, 0, -1], [2, 3, 5, 0]], dtype=float)
    print(A)
    m, n = np.shape(A)

    det_val = nan

    stop, perm_count = check_matrix(A)

    print(A)

    # Find an upper triangular matrix using gaussian elimination and a pivot different from one
    if m == n and not stop:
        # Forma escalonada reducida por renglones (TODO: se requiere pivote parcial?)
        for j in range(n):  # Watchout! Up to m2, not n2

            print('j:', j)
            # TIP 1: Generar la secuencia sin el elemento de la diag donde i=j
            idx = [number for number in range(n) if number > j]  # > j for aun upper triangular matrix
            print(idx)

            # TIP 2: Saca ese bloque afuera, al cabo solo se usa una vez
            # First step: ensure the diag element is 1 (we are only sure that j = i, so you can use j instead)
            pivot_row = A[j, :]

            for i in idx:
                print('i:', i)

                print('pivot_row=', pivot_row)
                print('Make zero')
                if not np.allclose(A[i, j],0):
                    coeff = (-1) * A[i, j]/pivot_row[j]
                    A[i, :] = A[i, :] + coeff * pivot_row
                else:
                    print('Element is already a zero')

                print('A=\n', A)
                print('idx a final:', idx)

                # Check if ith-row has only zeros
                if np.allclose(A[i, :],np.zeros(np.shape(A[i, :]))):
                    print('Zeros row')
                    det_val = 0
                    stop = True
                    break
                else:
                    print('Everything is OK')

            if stop:
                break


        print(A)
        # Double check we have indeed a triangular matrix at this point
        if not stop:
            diag_elems = A.diagonal()
            det_val = math.pow(-1,perm_count)
            print('Permutations count =', perm_count)
            for elem in diag_elems:
                det_val = det_val*elem

    else:
        det_val = 0


    print('Determinant = ', det_val)




if __name__ == '__main__':
    main()
