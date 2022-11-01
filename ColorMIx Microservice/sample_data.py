# from data given by the user they can pick two colors to blend for their planet
import time

color1 = "red"
color2 = "blue"


print("Sending colors...")

# use txt files to transfer back and forth data with the microservice py
f = open('define_color.txt', 'w')
f.write(f"{color1}")
f.close()

time.sleep(2.0)

f = open('define_color.txt', 'w')
f.write(f"{color2}")
f.close()

time.sleep(4.0)

f = open('rgb.txt', 'r')
rgb = f.read()
f.close()
print("New RGB Mix: ", rgb)

time.sleep(4.0)

f = open('hex.txt', 'r')
hex = f.read()
f.close()
print("New HEX Mix: ", hex)



