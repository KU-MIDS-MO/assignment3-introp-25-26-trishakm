import numpy as np

def moving_average(signal, window_size):
    
    signal = np.array(signal, dtype = float)
    n = len(signal)
    result = np.zeros (n, dtype = float)
    k = (window_size-1)//2
    
    for i in range (n):
        left = max(0,i-k)
        right = min(n-1, i+k)
        
        total = 0
        count = 0
    
        for j in range (left, right+1):
            total += signal[j]
            count +=1
            
        result[i] = total / count
        
    return result
    
    pass

signal = ([10, 20, 30, 40, 50])
print(moving_average(signal, 3))

#3) moving_average(signal, window_size)
#   We want to smooth a 1-D NumPy array using a centered moving average.
#   - signal is a 1-D NumPy array of numbers
 #  - window_size is a positive odd integer (1, 3, 5,...).
  # Let k = (window_size - 1) // 2
  # For each index i, consider the indices from max(0, i-k) to min(n-1, i+k),
  # where n is the length of signal, and take the average of those values.
  # Return a new 1-D NumPy array of floats with the same length as signal.