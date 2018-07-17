import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
def animate(i):
    pullData = open("lfinal.txt","r").read()
    pullData1 = open("rfinal.txt","r").read() 
    dataArray = pullData.split('\n')
    dataArray1 = pullData1.split('\n')
    xar = []
    yar = []
    xar1 = []
    yar1 = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xar.append(float(x))
            yar.append(float(y))
    for eachLine in dataArray1:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xar1.append(float(x))
            yar1.append(float(y))
    ax1.clear()
    ax1.plot(xar,yar)
    ax2.clear()
    ax2.plot(xar1,yar1, color = 'r') 

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
