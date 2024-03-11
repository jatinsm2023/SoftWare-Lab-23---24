import numpy as np
import cv2
import matplotlib.pyplot as plt

def Plot_Instensity_Diagram(filename):
    original = cv2.imread(filename)
    if original is None:
        print('Could not open or find the image:', filename)
        exit(0)
    
    X = np.mean(original, axis=2, dtype=int).astype(np.uint8)
    
    plt.hist(X.flatten(), bins=range(0,256), color='blue', alpha= 0.7)
    plt.title("Pixel Intensity Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()
    
    
Plot_Instensity_Diagram('a.png')