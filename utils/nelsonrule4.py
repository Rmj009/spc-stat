import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



"""
Read csv Examples 
# df = pd.read_csv('workbook_name.csv', sep=',',header=0); nmp = df.to_numpy() ;data = nmp[:,11]#; data = pd.DataFrame(nmp[:,11])
1. entrypoint def(nelsonrule4) 
2. pipeline to assign_datum , check the rules by violations(restRule1~4)
3. Draw the 3sigma (plotAxlines) and save fig in statics/img = 'static/nelson_chart.png'

P.S. the draw which as a substitue to gauge.nelson()
"""
############################
############################
############################
def rando():
    theNum = np.random.randint(low = 7.5, high = 15 , size = 195)
    return theNum
############################
############################
############################

def checkLSLUSL(obj, USL, LSL):
    for i in range(len(obj)):
        if i >= USL:
            print('USL')
        elif i <= LSL:
            print('LSL')

def testRule1(obj,newNum, mean, sd):

    sigUp = mean + sd*3
    sigDown = mean - sd*3
    code = (newNum > sigUp) or (newNum < sigDown)
    
    obj['format_1'] = np.append(obj['format_1'],code)
    print('obj[sss]',code)
    return 

def testRule2(obj, newNum, mean, sd):
    twoSigUp = mean + sd*2
    twoSigDown = mean - sd*2
    temp_clipped = obj['all_vals'][-2:]
    temp_clipped = np.append(temp_clipped,newNum)
    above2 = temp_clipped > twoSigUp
    below2 = temp_clipped < twoSigDown
    code = (above2.sum(axis=0) >= 2) or (below2.sum(axis=0) >= 2)
    obj['format_2'] = np.append(obj['format_2'],code)
    return

def testRule3(obj, newNum, mean, sd):
    oneSigUp = mean + sd
    oneSigDown = mean - sd
    temp_clipped = obj['all_vals'][-5:]
    temp_clipped = np.append(temp_clipped,newNum)
    above1 = temp_clipped > oneSigUp
    below1 = temp_clipped < oneSigDown
    code = (above1.sum(axis=0) >= 4) or (below1.sum(axis=0) >= 4)
    obj['format_3'] = np.append(obj['format_3'],code)
    return

def testRule4(obj, newNum, mean):
    temp_clipped = obj['all_vals'][-8:]
    temp_clipped = np.append(temp_clipped,newNum)
    above = temp_clipped > mean
    below = temp_clipped < mean
    code = (above.sum(axis=0) >= 9) or (below.sum(axis=0) >= 9)
    obj['format_4'] = np.append(obj['format_4'],code)
    return

def violations(obj,datum):
    # print('violations',obj)
    theMean = np.mean(obj['all_vals'])
    sd = np.std(obj['all_vals'])
    testRule1(obj,datum, theMean, sd)
    testRule2(obj,datum, theMean, sd)
    testRule3(obj,datum, theMean, sd)
    testRule4(obj,datum, theMean)

    return
    
def assign_datum(obj,datum):  # datum = None
    # print('violations \n',obj)
    # if(datum is None):
    #     datum = rando()
    # datum = obj['all_vals'][1:100]
    violations(obj,datum)
    obj['all_vals'] = np.append(obj['all_vals'],datum)
    return

#Return the value's index if rule has been violated.  This is used for formatting.

def format_arr(trendObj,rule):
    rule_arr = 'format_' + str(rule)
    print('rule_arr',rule_arr)
    aa=[index for index,val in enumerate(trendObj[rule_arr]) if val]
    print('.....',aa)
    return [index for index,val in enumerate(trendObj[rule_arr]) if val]

def plotAxlines(array):
    theMean = np.mean(array)
    sd = np.std(array)
    colors = ['black','green','violet','red']
    for level,color in enumerate(colors):
        upper = theMean + sd*level
        lower = theMean - sd*level
        plt.axhline(y=upper, linewidth=2, color=color)
        plt.axhline(y=lower, linewidth=2, color=color)
    return

def NelsonRules2(points,Target,LSL,USL):
    # print(LSL,USL)
    points = [float(i) for i in points.split(',')]
    Target = float(Target)
    trendObj = {'all_vals': points,'format_1': np.zeros(len(points)),'format_2': np.zeros(len(points)),'format_3': np.zeros(len(points)),'format_4': np.zeros(len(points))}
    assign_datum(obj = (trendObj), datum = Target)
    # pd_trendObj = pd.DataFrame(trendObj) #, columns = [alphabets[name] for name in range(len(trendObj))], index = [i for i  in range(len(ptV)+1)] )
    # print(',,,',[index for index,val in enumerate(trendObj['format_1']) if val])
    # print(pd_trendObj)
    mark = 10.5
    plt.figure(figsize=(20,10))
    plt.legend()
    plt.plot(trendObj['all_vals'], color='red',markevery=format_arr(trendObj,rule = 1), ls="", marker='s',mfc = 'none', mec='red', label="Rule1", markersize=mark*1.5)
    plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(trendObj,rule = 2), ls="", marker='o', mfc='none',mec='blue',label="Rule2", markersize=mark*1)
    plt.plot(trendObj['all_vals'], color='brown',markevery=format_arr(trendObj,rule = 3), ls="", marker='o', mfc='none',mec='brown',label="Rule3", markersize=mark*1.5)
    plt.plot(trendObj['all_vals'], color='blue',markevery=format_arr(trendObj,rule = 4), ls="", marker='s', mfc='none',mec='green',label="Rule4", markersize=mark*1.0)
    plt.plot(trendObj['all_vals'], color='#81B5CB', ls="", marker=".", markersize=mark)
    plotAxlines(trendObj['all_vals'])
    plt.ylim(0,max(points)+np.std(points,ddof=1))
    plt.savefig('static/nelson_chart.png')
    plt.show()



# alphabets = [chr(i) for i in range(ord('A'),ord('Z')+1)]






# # # g = sns.relplot(x = 'all_vals', y = 'format_1', data = trendObj, kind="line")
# # # g.fig.autofmt_xdate()
# # # # # plotQuery()
# plt.show()