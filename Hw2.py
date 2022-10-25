from PIL import Image
from collections import Counter
import numpy as np

Input = Image.open('input.png')
input_arr = np.array(Input)

w, h = Input.size
q0, qk = 0, 255
prob = (qk - q0) / (w * h) 

temp_arr = input_arr.flatten()
H = Counter(temp_arr)
maxi = max(H) + 1

p_sum = 0
for i in range(maxi):
    p_sum += H[i]
    H[i] = p_sum

for i in range(h):
    for j in range(w):
        if input_arr[i][j] == 0 or input_arr[i][j] == 255:
            continue

        input_arr[i][j] = prob * H[input_arr[i][j]]

output_arr = np.uint8(input_arr)
output = Image.fromarray(output_arr)
output.save('output.png')

    