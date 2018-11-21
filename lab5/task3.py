import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


image = mpimg.imread('sobaka.png')
imgplot = plt.imshow(image)
arr = np.asarray(image)
plt.show()


I_red = image.copy()
I_red[:, :, 1] = 0
I_red[:, :, 2] = 0
plt.imshow(I_red)
plt.show()
I_green = image.copy()
I_green[:, :, 0] = 0
I_green[:, :, 2] = 0
plt.imshow(I_green)
plt.show()
I_blue = image.copy()
I_blue[:, :, 0] = 0
I_blue[:, :, 1] = 0
plt.imshow(I_blue)
plt.show()


plt.gray()
lum_img = image[:,:,0]
plt.imshow(lum_img)
plt.show()
plt.imshow(lum_img, clim=(0.2, 0.9))
plt.show()