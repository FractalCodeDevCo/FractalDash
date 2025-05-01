import numpy as np
import nolds

def box_counting_fd(data):
    """
    Calcula la dimensión fractal usando box-counting.
    :param data: Serie de datos (array numpy).
    :return: dimensión fractal (float).
    """
    return nolds.corr_dim(data, emb_dim=10)
