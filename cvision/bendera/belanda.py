import numpy as np
import cv2
import pandas as pd

height = 150
width = 225

flag = np.zeros((height, width, 3), dtype=np.uint8)

stripe_height = height // 3

flag[:stripe_height, :] = [0, 0, 255]  

flag[stripe_height:2*stripe_height, :] = [255, 255, 255] 

flag[2*stripe_height:, :] = [255, 0, 0]  

df_flag = pd.DataFrame(flag.reshape(-1, 3), columns=['B', 'G', 'R'])
print(df_flag.head()) 

cv2.imwrite('belanda.png', flag)

cv2.imshow("timnas pusat/belanda", flag)
cv2.waitKey(0)
cv2.destroyAllWindows()
