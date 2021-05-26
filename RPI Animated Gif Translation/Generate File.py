
# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image, ImageSequence
import image
from PIL import GifImagePlugin
import time

filename = "zoe"

imageObject = Image.open("./" + filename + ".gif")
num_frames = imageObject.n_frames

print(imageObject.is_animated)
print(imageObject.n_frames)

 
def rgb_to_hex(pixel):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (pixel.get_red(), pixel.get_green(), pixel.get_blue()) 
 
# Save individual frames from the loaded animated GIF file
i=0
for frame in ImageSequence.Iterator(imageObject):
    frame.save("./tempOutput/gif-webp-"+str(i)+".webp",format = "WebP", lossless = True)
    i += 1    


#write the whole python code here so that the output file is fully ready to run
outputFile = open("./translatedAnimations/" + filename + "_hex.anim", "w")

# Simple test for NeoPixels on Raspberry Pi
outputFile.write(str(imageObject.n_frames) + "\n")


canvas = image.ImageWin(32,32,"Animation")
frames = []   #list. Each item in this list is another list (a current frame)
# Then, open each image one at a time and record pixel array information
for i in range(imageObject.n_frames):
    currentImage = image.Image("./tempOutput/gif-webp-"+str(i)+".webp")
    currentImage.draw(canvas)
    

    #grab pixel RGB data for the current frame
    cur_frame = []  #another list, holds 32 "column" lists
    for x in range(currentImage.get_width()):
        column = [] #list of 32 RGB triplets (one per row)
        for y in range(currentImage.get_height()):
            current_pixel = currentImage.get_pixel(x,y)
            column.append(current_pixel)
            outputFile.write(str(rgb_to_hex(current_pixel))+" ")
        cur_frame.append(column)
        outputFile.write("\n")
    frames.append(cur_frame)
    

outputFile.close()