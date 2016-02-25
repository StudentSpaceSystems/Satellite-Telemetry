
from scipy import misc
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib

def makeGray(images):

    for im in images:
        image = misc.imread(im) #saves image as image
        print image.shape #prints tuple of information about image
        print image[0][0]

        #plt.imshow(image) #load
        #plt.show()  # show the window
        grey = np.zeros((image.shape[0],image.shape[1])) #initialize an empty array with the dimensions of the image
        greys = []
        for row in range(image.shape[0]): #cycle through each row
            for col in range(image.shape[1]):
                grey[row][col]= np.average(image[row][col])



        plt.imshow(grey, cmap = matplotlib.cm.Greys_r) #allows you to visualize greyscale image

        plt.show() #shows grayscale image

    print 'done'

