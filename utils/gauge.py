from utils.calculator import Calculator
import numpy as np


class Gauge(Calculator):
    def __init__(self, points,good,defect,LSLlst,USLlst,measureAmount,stdValue):
        super().__init__(points,good,defect,LSLlst,USLlst,measureAmount,stdValue)
        self.points = points
        self.good = good 
        self.defect = defect
        self.LSLlst = LSLlst
        self.USLlst = USLlst
        self.measureAmount = measureAmount
        self.stdValue = stdValue
    
    def __repr__(self):
        return f"SpcMeasurePointConfigUUID: {self.spmcUUID},{self.points}."

    def stats(points,good,defect,LSLlst,USLlst,measureAmount,stdValue):
        points = points.split(',')
        points = [ float(i) for i in points]
        # [dict([i, int(x)] for i, x in b.items()) for b in list]
        df = np.array([good,defect,LSLlst,USLlst,measureAmount,stdValue]).astype(float)#,index=integer_array)
        Target = df[-1]
        good = df[0]
        defect = df[1]
        LSLlst = df[2]
        USLlst = df[3]
        measureAmount = df[4]
        stdValue = df[5]
        USL = Target + USLlst
        LSL = Target - LSLlst
        LCL = (LSL + Target)/2
        UCL = (USL + Target)/2
        rangespec = USL - LSL
        print('rangespec',rangespec)
        totalNum = good + defect
        goodRate = good / totalNum

        
        ngroup = int(len(df))/int(measureAmount)
        if (ngroup.is_integer() == False):
            cpkarr = np.array_split(points[::-1],len(points)//measureAmount) #revserve to split coz the array_split method
            cpkarrMEAN = [np.mean(i) for i in cpkarr]
            sigmaCpk = np.std(cpkarrMEAN,ddof=1) #pd.std() >>> //(n)
        else:
            print('datashape[0]')
            cpkarr = np.array_split(points,ngroup)
            cpkarrMEAN = [np.mean(i) for i in cpkarr]
            sigmaCpk = np.std(cpkarrMEAN,ddof=1) # numpy standard deviation >>> //(n-1)
        cp_mean = np.mean(points)
        sigmaPpk = np.std(points,ddof=1)
        sigmaCpk = 1.33
        print('sigmaPpk',sigmaPpk)
        # Calculator.calc
        # except Exception as error:
        #     print('err',error)

        if (sigmaCpk == 0) or (sigmaPpk == 0):
            raise Exception('SigmAomaly') 
        assert sigmaPpk != 0
        assert sigmaCpk != 0

        Cp = (rangespec) / (sigmaCpk*6) 
        Ck = abs((Target - cp_mean)/ (rangespec / 2))
        Cpu = (USL - cp_mean) / (sigmaCpk*3)
        Cpl = (cp_mean - LSL) / (sigmaCpk*3)
        Cpk = np.min([Cpu,Cpl]) 
        # Cpk = abs((1-Ck)*Cp) // calculation requires to be discussed
        Ppu = (UCL - cp_mean) / (sigmaPpk*3)
        Ppl = (cp_mean - LCL) / (sigmaPpk*3)
        Ppk = np.min([Ppu,Ppl]) 
        # capability ratio
        CPR = good, totalNum, goodRate ,USL,LSL,UCL,LCL,cp_mean,Target ,rangespec, Cpu, Cpl, Cp, Ck, Cpk, Ppk
        keys = ["good","totalNum","goodRate","USL","LSL","UCL","LCL","overallMean","target","range","Cpu","Cpl","Cp","Ck","Cpk","Ppk"]
        capability = dict(zip(keys, CPR))
        print('capability::',capability)
        ### Reference :https://en.wikipedia.org/wiki/Process_performance_index
        return capability # total 17