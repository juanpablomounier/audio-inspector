"""

"""

import numpy as np

def temporal_novelty(smooth_energy):
    
    if not isinstance(smooth_energy, np.ndarray):
        raise ValueError("energy must be a numpy array.")
    
    differences = np.diff(smooth_energy, n=1)
    differences_resized = np.insert(differences,0,0)
    novelty = np.maximum(differences_resized, 0)
    if not (len(novelty) == len(smooth_energy)):
        raise ValueError("novelty array's lenght doesn't march energy array's lenght.")
    return novelty
