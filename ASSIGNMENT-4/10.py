import cv2
import matplotlib.pyplot as plt
import numpy as np

def draw_black_rectangle(image, top_right, bottom_left):
    new_image = image.copy()
    
    cv2.rectangle(new_image, top_right, bottom_left, (0,0,0), -1)
    return new_image

filename = 'a.png'
original = cv2.imread(filename)

if original is None:
    print('Could not open or find the image:', filename)
    exit(0)
else:
    top_right = (40,100)
    bottom_left = (70,200)
    new_image = draw_black_rectangle(original, top_right, bottom_left)
    X = np.mean(new_image, axis=2, dtype=int).astype(np.uint8)
    
    plt.subplot(1,1,1)
    plt.imshow(X, cmap='gray')
    plt.title("Image with Black Rectangle")
    
    plt.tight_layout()
    plt.show()
    
    
