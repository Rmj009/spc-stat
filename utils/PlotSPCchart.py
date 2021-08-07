import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def drawchart1(datapoints):
        #---------invoke western------------
        # datapoints = valuelst
        trendObj = {'all_vals': datapoints,'format_1': np.zeros(len(datapoints)),'format_2': np.zeros(len(datapoints)),'format_3': np.zeros(len(datapoints)),'format_4': np.zeros(len(datapoints))}
        print("pppppppppp",trendObj['all_vals'])
        # assign_datum(obj = trendObj, datum = 10)
        def format_arr(rule):
            rule_arr = 'format_' + str(rule)
            return [index for index,val in enumerate(trendObj[rule_arr]) if val]
        def plotAxlines(array):
            theMean = np.mean(array)
            sd = np.std(array)
            colors = ['black','green','violet','red']
            for level,color in enumerate(colors):
                upper = theMean + sd*level
                lower = theMean - sd*level
                plt.axhline(y=upper, linewidth=0.5, color=color)
                plt.axhline(y=lower, linewidth=0.5, color=color)
            return
        mark = 3.5
        plt.figure(figsize=(60,30))
        plt.plot(trendObj['all_vals'], color='red',markevery=format_arr(1), ls="", marker='s',mfc = 'none', mec='red', label="Rule1", markersize=mark*1.5)
        plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(2), ls="", marker='o', mfc='none',mec='blue',label="Rule2", markersize=mark*1)
        plt.plot(trendObj['all_vals'], color='brown',markevery=format_arr(3), ls="", marker='o', mfc='none',mec='brown',label="Rule3", markersize=mark*1.5)
        plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(4), ls="", marker='s', mfc='none',mec='green',label="Rule4", markersize=mark*1.0)
        plt.plot(trendObj['all_vals'], color='#81B5CB', ls="", marker=".", markersize=mark)
        plotAxlines(trendObj['all_vals'])
        plt.legend()
        plt.ylim(0,25)
        # # plt.plot(datapoints)
        # plt.savefig('static/img/control-chart.png')
        # # g = sns.relplot(x = 'all_vals', y = 'format_1', data = trendObj, kind="line")
        # # g.fig.autofmt_xdate()
        plt.show()

def drawchart2(original):
    """Plot RawData"""
    text_offset = 70
    mean = np.mean(original)
    sigma = np.std(original)
    # print("###",[mean,sigma])
    fig = plt.figure(figsize=(20, 10))
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(original, color='blue', linewidth=1.5)

    # plot mean
    ax1.axhline(mean, color='r', linestyle='--', alpha=0.5)
    ax1.annotate('$\overline{x}$', xy=(len(original), mean), textcoords=('offset points'),
                xytext=(text_offset, 0), fontsize=18)

    # plot 1-3 standard deviations
    sigma_range = np.arange(1,4)
    for i in range(len(sigma_range)):
        ax1.axhline(mean + (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
        ax1.axhline(mean - (sigma_range[i] * sigma), color='black', linestyle='-', alpha=(i+1)/10)
        ax1.annotate('%s $\sigma$' % sigma_range[i], xy=(len(original), mean + (sigma_range[i] * sigma)),
                    textcoords=('offset points'),
                    xytext=(text_offset, 0), fontsize=18)
        ax1.annotate('-%s $\sigma$' % sigma_range[i],
                    xy=(len(original), mean - (sigma_range[i] * sigma)),
                    textcoords=('offset points'),
                    xytext=(text_offset, 0), fontsize=18)
    # plt.show()
    plt.savefig('static/img/classicialcc.png')
    return
