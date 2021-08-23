from PlotnelsonRules import *
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
from matplotlib.lines import Line2D
import time



"""
Plot the real-time timeseries
(under built)
"""


class Scope:
    def __init__(self, ax, maxt=225, dt=2):
        self.ax = ax
        self.dt = dt
        self.maxt = maxt
        # self.mean = np.mean([ax])
        self.tdata = [0]
        self.ydata = [0]
        self.line = Line2D(self.tdata, self.ydata)
        self.ax.add_line(self.line)
        self.ax.set_ylim(0, 60)
        self.ax.set_xlim(0, self.maxt)

    def update(self, y,origin):
        lastt = self.tdata[-1]
        if lastt > self.tdata[0] + self.maxt:  # reset the arrays
            self.tdata = [self.tdata[-1]]
            self.ydata = [self.ydata[-1]]
            self.ax.set_xlim(self.tdata[0], self.tdata[0] + self.maxt)
            self.ax.figure.canvas.draw()

        t = self.tdata[-1] + self.dt
        self.tdata.append(t)
        self.ydata.append(y)
        self.line.set_data(self.tdata, self.ydata)
        # plot mean
        text_offset = 70
        mean = np.mean(origin[0])
        sigma = np.std(origin[0])

        ax.axhline(mean, color='r', linestyle='--', alpha=0.5)
        ax.annotate('$\overline{x}$', xy=(len(origin[0]), mean), textcoords=('offset points'),xytext=(text_offset, 0), fontsize=9)
        sigma_range = np.arange(1,4)
        for i in range(len(sigma_range)):
            ax.axhline(mean + (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
            ax.axhline(mean - (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
            ax.annotate('%s $\sigma$' % sigma_range[i], xy=(len(origin[0]), mean + (sigma_range[i] * sigma)),
                        textcoords=('offset points'),
                        xytext=(text_offset, 0), fontsize=8)
            ax.annotate('-%s $\sigma$' % sigma_range[i],
                        xy=(len(origin[0]), mean - (sigma_range[i] * sigma)),
                        textcoords=('offset points'),
                        xytext=(text_offset, 0), fontsize=8)
        return self.line,        



def drawchart(self, origin):
    """Plot RawData"""
    text_offset = 70
    mean = np.mean(self, origin[0])
    sigma = np.std(self, origin[0])
    # mean = np.mean(self, origin)
    # sigma = np.std(self, origin)
    # print("###",[mean,sigma])
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(self, origin, color='blue', linewidth=1.5)

    # plot mean
    ax1.axhline(mean, color='r', linestyle='--', alpha=0.5)
    ax1.annotate('$\overline{x}$', xy=(len(self, origin), mean), textcoords=('offset points'),
                xytext=(text_offset, 0), fontsize=18)

    # plot 1-3 standard deviations
    sigma_range = np.arange(1,4)
    for i in range(len(sigma_range)):
        ax1.axhline(mean + (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
        ax1.axhline(mean - (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
        ax1.annotate('%s $\sigma$' % sigma_range[i], xy=(len(self, origin), mean + (sigma_range[i] * sigma)),
                    textcoords=('offset points'),
                    xytext=(text_offset, 0), fontsize=18)
        ax1.annotate('-%s $\sigma$' % sigma_range[i],
                    xy=(len(self, origin), mean - (sigma_range[i] * sigma)),
                    textcoords=('offset points'),
                    xytext=(text_offset, 0), fontsize=18)
    # plt.show()
    plt.savefig('static/img/classicialcc.png')
    return


def emitter(self,object):
    while True:
        for i in range(len(object[0])):
            time.sleep(0.001)
            if (object[0][i] >= 2* self.mean):
                yield object[0][i]
                print(f'System Pause because of out of boundary:',object[0][i])
                time.sleep(100)
            yield object[0][i]
            
    # while True:
        # for i,j in enumerate(object[0]):
        #     time.sleep(0.01)
        #     yield object[0][i]
    #     for index, row in df.iterrows():
    #         yield object[row][index]
            

fig, ax = plt.subplots()
# fig = plt.figure(figsize=(20, 10))


# ax = fig.add_subplot(1, 1, 1)
# ax.plot(origin[0], color='blue', linewidth=1.5)


# plot 1-3 standard deviations

# # plt.show()
# plt.savefig('static/classicialcc.png')

scope = Scope(ax)
# pass a generator in "emitter" to produce data for the update func
ani = animation.FuncAnimation(fig, scope.update, emitter(object), interval=50, blit=True)

plt.show()
