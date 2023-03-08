import matplotlib.pyplot as plt


"""
Members: Artacho, Cristopher Ian
         Billena, Dhominick John
         Torre, Jephone Issiah Jireh
"""

"""
Formula for the Brensenham's Line Algorithm: Source: Wolfram Alpha
    m = dx / dy
    c = 1
    x = x            # The value of x increments and affects the value of y
    y = mx + c       # The value of y is affected by the slope of m * x the c is the value which influences the increment of the value

Formula for the DDA Line's Algorithm Midpoint
    midpoint = x = (x1 + x2) / 2 #Finding the locaition of the middle point of the xlines
               y = (y1 + y2) / 2 #Finding the location of the middle for the ylines
"""


plt.title("Mid Point Line Assignment") #title for the plot/graph
plt.xlabel("Horizontal Axis") #name for the x coordinate
plt.ylabel("Vertical Axis") #name for the y coordinate

def DDALine(x1, y1, x2, y2, color, color_midpoint): #function
    dx = x2 - x1 
    dy = y2 - y1
    x3 = (x1 + x2) /2 #coordinates for the midpoint on the horizontal axis
    y3 = (y1 + y2) /2 #coordinates for the midpoint on the vertical axis
    
    #calculate steps required for generating pixels 

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy) #will take the value of dx if ds is more than dy. Otherwise, will take the value of dy

    #calculate increment in x and y for each steps

    Xinc = float(dx / steps)
    Yinc = float(dy / steps)

    for i in range(0, int(steps + 1)):
        #draw pixels 
        plt.plot (int(x1), int(y1), color) #plots first the looped coordinates of x and y
        plt.plot (x3, y3, color_midpoint) #plot for the midpoint's location
        x1 += Xinc
        y1 +=Yinc 

    plt.show()

def brensenham(x1, y1, x2, y2, color):
    # midx = (x1 + x2) / 2
    # midy = (y1 + y2) / 2
    m = (y2 - y1) / (x2 - x1)
    c = 1

    for x in range(x1, x2 + 1): #Increase the value of the second because it is rounded?
        y = round(m*x + c) 
        plt.plot(int(x), int(y), color)
        # plt.plot(int(midx), int(midy), 'b.') #Having errors after defining the midpoint of the line in brensenham

    plt.show()

def main():

        x1 = int(input("Enter X1: "))
        y1 = int(input("Enter Y1: "))
        x2 = int(input("Enter X2: "))
        y2 = int(input("Enter Y2: "))
        color = "r." #red color for the plotted line
        color_midpoint = "b." #the color of the midpoint will be blue
        DDALine (x1, y1, x2, y2, color, color_midpoint)
        brensenham(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()


