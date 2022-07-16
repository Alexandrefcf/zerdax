import numpy as np
def set_kernels(angles):
    a0 = np.array([
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 1, 1, 1, 1],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          ], dtype='uint8').T
    a4 = np.array([
          [1, 0, 0, 0, 0],
          [0, 1, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 1],
          ], dtype='uint8').T
    a5 = np.array([
          [0, 0, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 1, 0, 0, 0],
          [1, 0, 0, 0, 0],
          ], dtype='uint8').T
    a9 = np.array([
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0],
          ], dtype='uint8').T

    k0 = np.zeros((angles.shape[0], 5, 5), dtype='uint8')
    i = 0
    for angle in angles:
        if abs(angle - 0.0) <= 22.5:
            k0[i,:,:] = a0
        elif abs(angle - 45.5) <= 22.5:
            k0[i,:,:] = a5
        elif abs(angle + 45.0) <= 22.5:
            k0[i,:,:] = a4
        elif abs(angle - 90) <= 22.5:
            k0[i,:,:] = a9
        elif abs(angle + 90) <= 22.5:
            k0[i,:,:] = a9
        else:
            k0[i,:,:] = a0
        i += 1

    print("k:", k0)
    return k0
