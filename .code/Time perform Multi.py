import numpy as np
import time


def np_array_time(number=1000):
    arr1 = np.array(list(range(number)))
    arr2 = arr1.copy()

    initial_time = time.time()

    result_array = arr1*arr2

    print("Times taken by Numpy Arrays to perform multiplication:",
          time.time() - initial_time,
          "second"),


def list_time(number=1000):
    arr1 = list(range(number))
    arr2 = arr1.copy()

    initial_time = time.time()

    result_list = [(x*y) for x, y in zip(arr1, arr2)]

    print("Times taken by List to perform multiplication:",
          time.time() - initial_time,
          "second"),


np_array_time(100000000)  # 0.09470939636230469 second
list_time(10000000)      # 0.5233652591705322 second
