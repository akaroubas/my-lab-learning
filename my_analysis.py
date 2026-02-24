import numpy as np
import os
import time
   
# Simulate some computation
print(f"Starting analysis on {os.uname().nodename}")
data = np.random.randn(1000, 100)
result = np.linalg.svd(data)
print(f"Analysis completed! Singular values shape: {result[1].shape}")
   
# Save results
np.save('results.npy', result[1])
print("Results saved to results.npy")    
