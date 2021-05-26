import time 
import board 
import neopixel
import random

FILENAME = "sample5_hex.anim"
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18 
# The number of NeoPixels
num_pixels = 1024 
# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW. 
ORDER = neopixel.GRB 
pixels = neopixel.NeoPixel( pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER ) 

data = open("./anims/" + FILENAME, "r")
n_frames = int(data.readline())

frames = []
for a in range(n_frames):
    cur_frame = []
    for i in range(32):
        row = data.readline()
        row = row.split(" ")
        cur_row = []
        for j in range(32):
            col = row[j]
            cur_row.append(col)
        cur_frame.append(cur_row)
    frames.append(cur_frame)


def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def find_pixel(x,y):
     end_location=0
     if x < 8:   #outside left column
         if y%2==0: #even row
             end_location= y*8 + (7-x) 
         else:
             end_location = y*8 + x
     elif x < 16:  #inside left column
         if y%2==0: #even row
             end_location= (31-y)*8 + (7-x%8)+ 256
         else:
             end_location = (31-y)*8 + x%8  + 256
     elif x < 24:  #inside right column
         if y%2==0: #even row
             end_location= y*8 + (7-x%8) + 512
         else:
             end_location = y*8 + (x%8) + 512
     else:    #outside right column
         if y%2==0: #even row
             end_location= (31-y)*8 + (7-x%8)+ 768
         else:
             end_location = (31-y)*8 + x%8 + 768
     return end_location
     
def set_pixel_c(x,y,r,g,b):
     pixels[find_pixel(x,y)] = (r,g,b)
     
 
pixels.fill((0, 0, 0))
counter = 0
while True:
    for f in frames:
        for x in range(len(f)):
            col = f[x]
            for y in range(len(col)):
                pixel = col[y]
                pixel = hex_to_rgb(pixel)
                set_pixel_c(x,y,pixel[0],pixel[1],pixel[2])
        pixels.show()      
        time.sleep(0.02)
