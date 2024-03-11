import cv2
import matplotlib.pyplot as plt
import numpy as np


def display_binarized_images(X, thresholds):

    # Display binarized images with different thresholds
    for i, threshold in enumerate(thresholds, start=2):
        binarized_image = np.where(X > threshold, 255, 0).astype(np.uint8)
        plt.subplot(2, 2, i-1)
        plt.imshow(binarized_image, cmap='binary')
        plt.title(f"Binarized (Threshold={threshold})")

    plt.tight_layout()
    plt.show()


image_path = 'a.png' 


image = cv2.imread(image_path)
X = np.mean(image, axis=2, dtype=int).astype(np.uint8)


# Display the binarized images with different thresholds
thresholds = [50, 70, 100, 150]
display_binarized_images(X, thresholds)
