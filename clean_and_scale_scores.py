import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    
    scores = np.array(scores, dtype = float)
    scores2 = scores.copy()
    
    if scores2.ndim == 1:   #checks dimension
        for i in range (scores2.shape[0]):  #range of length of vector
            if scores2[i] < min_score:
                scores2[i] = min_score
            elif scores2[i] > max_score:
                scores2[i] = max_score
    
    if scores2.ndim == 2:
        for i in range (scores2.shape[0]):   #gives number of rows
            for j in range (scores2.shape[1]):   #gives number of columns
                if scores2[i, j] < min_score:
                    scores2[i, j] = min_score
                elif scores2[i, j] > max_score:
                    scores2[i, j] = max_score
            
    
    scaled = (scores2 - min_score) / (max_score - min_score)
    
    return scaled
    
    pass

scores_test = np.array([[63,68,84], [92,95,96]])
print (clean_and_scale_scores(scores_test, 70,90))

#1) clean_and_scale_scores(scores, min_score, max_score)
 #  We have exam scores stored in a NumPy array (1D or 2D).
  # - First, replace all values smaler than min_score by min_score,
   #  and all values larger than max_score by max_score.
    
   #- Then linearly scale all values to the range [0, 1] using:
    #   scaled = (value - min_score) / (max_score - min_score)
   #Return a new NumPy array of floats with the same shape as scores 