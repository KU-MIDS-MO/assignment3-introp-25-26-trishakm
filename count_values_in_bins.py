import numpy as np

def count_values_in_bins(data, bin_edges):
    
    data = np.array(data, dtype = float)
    bin_edges = np.array(bin_edges, dtype = float)
    
    B = len(bin_edges) - 1
    counts = np.zeros(B, dtype = int)
    
    for x in data:
        if x < bin_edges[0] or x > bin_edges[-1]:
            continue
        
        for b in range (B):
            left = bin_edges[b]
            right = bin_edges[b+1]
            
            if b==B-1:
                if x >= left and x<=right:
                    counts[b] +=1
                    break
            
            else:
                if x>=left and x<right:
                    counts[b] += 1
                    break
                
    return counts
    pass

data = np.array ([1.2, 2.2, 5.3, 6.4, 5.0])
bin_edges = np.array ([1,2,3,4,5])

print (count_values_in_bins(data, bin_edges))


#2) count_values_in_bins(data, bin_edges)
 #  We want to count how many values fall into each numeric bin.
  # - data is a 1-D NumPy array of numbers.
   #- bin_edges is a 1-D NumPy array of length B+1, strictly increasing.
   #These edges define B bins:
    #  Bin 0: [bin_edges[0], bin_edges[1])
     # Bin 1: [bin_edges[1], bin_edges[2])
      #...
      #Bin B-2: [bin_edges[B-2], bin_edges[B-1])
      #Bin B-1: [bin_edges[B-1], bin_edges[B]]   (last bin is inclusive on the right)
 #  Values outside [bin_edges[0], bin_edges[-1]] are ignored.
  # Return a 1-D NumPy array of length B with the counts per bin.