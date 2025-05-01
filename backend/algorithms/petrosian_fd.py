import antropy as ant

def petrosian_fd(data):
    """
    Calcula la dimensión fractal de Petrosian, útil en análisis médico y biológico.
    :param data: Serie de datos (array numpy).
    :return: dimensión fractal Petrosian (float).
    """
    return ant.petrosian_fd(data)
