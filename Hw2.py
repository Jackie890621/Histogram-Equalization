from PIL import Image
from collections import Counter
import numpy as np
import sys

def histogram_equalization(q0, qk, target, w, h):
    prob = (qk - q0) / (w * h)

    temp = target.flatten()
    H = Counter(temp)
    maxi = max(H) + 1

    p_sum = 0
    for i in range(maxi):
        p_sum += H[i]
        H[i] = p_sum

    for i in range(h):
        for j in range(w):
            if target[i][j] == 0 or target[i][j] == 255:
                continue

            target[i][j] = prob * H[target[i][j]]

    return np.uint8(target)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('You should select input')
        sys.exit()

    Input = Image.open(sys.argv[1])
    input_arr = np.array(Input)
    w, h = Input.size

    output_arr = histogram_equalization(0, 255, input_arr, w, h)
    output = Image.fromarray(output_arr)
    output.save('output.png')

    