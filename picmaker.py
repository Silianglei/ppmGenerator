from random import seed
from random import randint

def main():
    seed(2)
    output = "P3\n500 500\n255\n"
    for i in range(20):
        a = randint(0,256)
        b = randint(0,256)
        c = randint(0,256)
        for j in range(25000):
            if j % 20 > 10:
                output += str(a) + " " + str(b) + " " + str(c)
                output += "\n"
            if j % 20 > 15:
                output += "0 255 0"
                output += "\n"
            else:
                output += "0 0 255"
                output += "\n"
    f = open("pic.ppm", "w+")
    f.write(output)
    f.close()

main()
