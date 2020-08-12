import numpy as np

def obtain_vertical(str):
    mat = np.array([list(s) for s in str])
    #transposicion
    return ["".join(s) for s in mat.T]

def oblique_to_horizontal(mat):
    oblique = []
    n_range = np.shape(mat)[0]
    for i in range(n_range):
        new_arr = np.diagonal(mat, i).tolist()
        oblique = add_higher(oblique, new_arr)
        if i != 0:
            new_arr = np.diagonal(mat, -i).tolist()
            oblique = add_higher(oblique, new_arr)
    return ["".join(s) for s in oblique]


def add_higher(oblique, new_arr):
    if len(new_arr) >= 4:
        oblique.append(new_arr)
    return oblique


def inv_oblique_to_horizontal(mat):
    mat = np.fliplr(mat)
    return oblique_to_horizontal(mat)