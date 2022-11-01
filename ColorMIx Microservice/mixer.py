from random import randrange
import time

# retreive first color 
f = open('define_color.txt', 'r')
color1 = f.read()
f.close()
print("Colors are mixing...")
# convert string data into a RGB data type 

if color1 == "red":
    first_color = (255,0,0)
elif color1 == "orange":
    first_color = (255,87,51)
elif color1 == "yellow":
   first_color = (255,255,0)
elif color1 == "green":
    first_color = (0,100,0)
elif color1 == "blue":
    first_color = (0,0,255)
elif color1 == "purple":
        first_color = (230,230,250)
elif color1 == "pink":
        first_color = (255, 192, 203)
elif color1 == "white":
    first_color = (255,255,255)
elif color1 == "black":
    first_color = (0,0,0)


time.sleep(4.0)

# retrieve second color
f = open('define_color.txt', 'r')
color2 = f.read()
f.close()

# convert to RGB
if color2 == "red":
    second_color = (255,0,0)
elif color2 == "orange":
    second_color = (255,87,51)
elif color2 == "yellow":
    second_color = (255,255,0)
elif color2 == "green":
    second_color = (0,100,0)
elif color2 == "blue":
    second_color = (0,0,255)
elif color2 == "purple":
    second_color = (230,230,250)
elif color2 == "pink":
    second_color = (255, 192, 203)
elif color2 == "white":
    second_color = (255,255,255)
elif color2 == "black":
    second_color = (0,0,0)

# random small number to create a variance in the color of the planet, if the user uses this more than once
varietyA = randrange(0,15)
varietyB = randrange(0,15)
varietyC = randrange(0,15)

# determine the blend of the R, G, B color integers, not to go over 255 or the upper limit of RGB number
R = ((first_color[0] + second_color[0]) // 2 )
if R + varietyA <= 255:
    R = R + varietyA

G = ((first_color[1] + second_color[1]) // 2 )
if G + varietyB <= 255:
    G = G + varietyB

B = ((first_color[2] + second_color[2]) // 2 )
if B + varietyC <= 255: 
    B =  B + varietyC

# determine one new color with a blend of the two, RGB style
rgbColor = (R, G, B)

# send the RGB format to a txt file and back to main
f = open('rgb.txt', 'w')
f.writelines(f"{rgbColor}")
f.close()


# transfer the RGB to HEX
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

hexColor = rgb_to_hex(rgbColor)

# send the HEX format to a txt file and back to main
f = open('hex.txt', 'w')
f.writelines(f"{hexColor}")
f.close()

