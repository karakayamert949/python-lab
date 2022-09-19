import numpy as np

def LinSysSolType(A,B):
    rA=np.linalg.matrix_rank(A)
    aug=np.concatenate((A,B),1)
    rAug=np.linalg.matrix_rank(aug)
    if rA<rAug:
        print("there is no solution")
    else:
        if len(A[0])==rA or len(A[0])==rAug:
            print("there is unique solution")
        else:
            print("infinitely solution")
