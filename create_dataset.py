import os

import mediapipe as np
import cv2
import matplotlib.pylplot as plt # type: ignore


DATA_DIR = './data'

for dir_in os.listdir(DATA_DIR):
 for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        img = cv2.inread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        plt.figure()
        plt.inshow(img_rgb)
        
plt.show()