import cv2
import numpy as np
import matplotlib.pyplot as plt


image_path = 'a.png'  
# Read the color image using OpenCV
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to read the image from {image_path}")
else:
    # Define the filter/filtre
    filtre = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    # Apply the filter to the color image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i, j] = np.matmul(image[i][j], filtre)
  

    # Display the filtered image
    plt.subplot(1, 1, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Resultant Image after Applying Filter")

    plt.tight_layout()
    plt.show()
