
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

#定义init_func,给定初始信息
def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,

#定义func,用来反复调用的函数
def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # 跟随自变量的增加更新y值
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

from matplotlib.animation import HTMLWriter
mywriter = HTMLWriter(fps=60)
ani.save('./myAnimation.html',writer=mywriter)
