
# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image, ImageSequence
import image
from PIL import GifImagePlugin
import time

filename = "sample5"

imageObject = Image.open("./" + filename + ".gif")
num_frames = imageObject.n_frames

print(imageObject.is_animated)
print(imageObject.n_frames)

 
def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue) 
 
# Save individual frames from the loaded animated GIF file
i=0
for frame in ImageSequence.Iterator(imageObject):
    frame.save("./tempOutput/gif-webp-"+str(i)+".webp",format = "WebP", lossless = True)
    i += 1    




        
            







#write the whole python code here so that the output file is fully ready to run
outputFile = open("./translatedAnimations/" + filename + "_code.py", "w")

# Simple test for NeoPixels on Raspberry Pi
outputFile.write("import time \n")
outputFile.write("import board \n")
outputFile.write("import neopixel\n")
outputFile.write("import random\n\n")
outputFile.write("# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18\n")
outputFile.write("# NeoPixels must be connected to D10, D12, D18 or D21 to work.\n")
outputFile.write("pixel_pin = board.D18 \n")

outputFile.write("# The number of NeoPixels\n")
outputFile.write("num_pixels = 1024 \n")

outputFile.write("# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!\n" )
outputFile.write("# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW. \n")
outputFile.write("ORDER = neopixel.GRB \n")

outputFile.write("pixels = neopixel.NeoPixel( pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER ) \n\n")



outputFile.write("frames = []\n")


canvas = image.ImageWin(32,32,"Animation")
frames = []   #list. Each item in this list is another list (a current frame)
# Then, open each image one at a time and record pixel array information
for i in range(imageObject.n_frames):
    currentImage = image.Image("./tempOutput/gif-webp-"+str(i)+".webp")
    currentImage.draw(canvas)
    

    #grab pixel RGB data for the current frame
    cur_frame = []  #another list, holds 32 "column" lists
    outputFile.write("cur_frame = []\n")
    for x in range(currentImage.get_width()):
        column = [] #list of 32 RGB triplets (one per row)
        outputFile.write("column = []\n")
        for y in range(currentImage.get_height()):
            current_pixel = currentImage.get_pixel(x,y)
            column.append(current_pixel)
            outputFile.write("column.append([" + str(current_pixel.get_red()) +","+ str(current_pixel.get_green()) +","+str(current_pixel.get_blue())+"])\n")
        cur_frame.append(column)
        outputFile.write("cur_frame.append(column)\n")
    outputFile.write("frames.append(cur_frame)\n")
    frames.append(cur_frame)
    




 
outputFile.write("def find_pixel(x,y):\n")
outputFile.write("     end_location=0\n")
outputFile.write("     if x < 8:   #outside left column\n")
outputFile.write("         if y%2==0: #even row\n")
outputFile.write("             end_location= y*8 + (7-x) \n")
outputFile.write("         else:\n")
outputFile.write("             end_location = y*8 + x\n")
outputFile.write("     elif x < 16:  #inside left column\n")
outputFile.write("         if y%2==0: #even row\n")
outputFile.write("             end_location= (31-y)*8 + (7-x%8)+ 256\n")
outputFile.write("         else:\n")
outputFile.write("             end_location = (31-y)*8 + x%8  + 256\n")
outputFile.write("     elif x < 24:  #inside right column\n")
outputFile.write("         if y%2==0: #even row\n")
outputFile.write("             end_location= y*8 + (7-x%8) + 512\n")
outputFile.write("         else:\n")
outputFile.write("             end_location = y*8 + (x%8) + 512\n")
outputFile.write("     else:    #outside right column\n")
outputFile.write("         if y%2==0: #even row\n")
outputFile.write("             end_location= (31-y)*8 + (7-x%8)+ 768\n")
outputFile.write("         else:\n")
outputFile.write("             end_location = (31-y)*8 + x%8 + 768\n")
outputFile.write("     return end_location\n")
outputFile.write("     \n")
outputFile.write("def set_pixel_c(x,y,r,g,b):\n")
outputFile.write("     pixels[find_pixel(x,y)] = (r,g,b)\n")
outputFile.write("     \n")
outputFile.write(" \n")

outputFile.write("pixels.fill((0, 0, 0))\n")
outputFile.write("counter = 0\n")
outputFile.write("while True:\n")
outputFile.write("    for f in frames:\n")
outputFile.write("        for x in range(len(f)):\n")
outputFile.write("            col = f[x]\n")
outputFile.write("            for y in range(len(col)):\n")
outputFile.write("                pixel = col[y]\n")
outputFile.write("                r = pixel[0]\n")
outputFile.write("                g = pixel[1]\n")
outputFile.write("                b = pixel[2]\n")
outputFile.write("                set_pixel_c(x,y,r,g,b)\n")
outputFile.write("        pixels.show()      \n")
outputFile.write("        time.sleep(0.02)\n")


outputFile.close()