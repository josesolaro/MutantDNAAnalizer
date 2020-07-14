import numpy as np

def obtain_vertical(str):
    mat = np.array([list(s) for s in str])
    #transposicion
    return ["".join(s) for s in mat.T]

def oblique_to_horizontal(mat):
    oblique = []
    n_range = np.shape(mat)[0]
    for x in range(n_range):
        try:
            # recorro de forma oblicua semitriangulo superior
            row = [mat[i + x, i] for i in range(n_range - x)]
            if len(row) >= 4:
                oblique.append(row)
            # recorro de forma oblicua semitriangulo inferior
            if x > 0:
                row = [mat[i, i + x] for i in range(n_range - x)]
                if len(row) >= 4:
                    oblique.append(row)
        except:
            None
    return ["".join(s) for s in oblique]


def inv_oblique_to_horizontal(mat):
    oblique_inv = []
    n_range = np.shape(mat)[0]
    for x in range(n_range):
        try:
            # recorro de forma oblicua inversa semitriangulo superior
            row = [mat[i, n_range - i - x - 1] for i in range(n_range - x)]
            if len(row) >= 4:
                oblique_inv.append(row)
            # recorro de forma oblicua inversa semitriangulo inferior
            if x > 0:
                row = [mat[i + x, -i - 1] for i in range(n_range - x)]
                if len(row) >= 4:
                    oblique_inv.append(row)
        except:
            None
    return ["".join(s) for s in oblique_inv]