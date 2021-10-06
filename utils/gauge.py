# from api.specBound import check_lsl_usl
from utils.PlotnelsonRules import *
import numpy as np
import pandas as pd

class Gauge():
    def __init__(self, points,LSLlst,USLlst,measureAmount,stdValue): #good,defect,
        # super().__init__(points,good,defect,LSLlst,USLlst,measureAmount,stdValue)
        self.points = points
        # self.good = good 
        # self.defect = defect
        self.LSLlst = LSLlst
        self.USLlst = USLlst
        self.measureAmount = measureAmount
        self.stdValue = stdValue
    
    def __repr__(self):
        return f"SpcMeasurePointConfigUUID:{self.points,self.LSLlst,self.USLlst,self.measureAmount,self.stdValue}."

    def stats(points,LSLlst,USLlst,measureAmount,stdValue): #good,defect,
        # points = pd.read_csv(points)
        # print('print(points)',points)
        points = [ float(i) for i in enumerate(points.split(','))]
        print('print(::::)',points)
        # [dict([i, int(x)] for i, x in b.items()) for b in list]
        df = np.array([LSLlst,USLlst,measureAmount,stdValue]).astype(float)#,index=integer_array) ##good,defect,
        Target = df[-1]
        # good = df[0]
        # defect = df[1]
        LSLlst = df[0]
        USLlst = df[1]
        good = []
        defect = []
        measureAmount = df[2]
        USL = Target + USLlst
        LSL = Target - LSLlst
        LCL = (LSL + Target)/2
        UCL = (USL + Target)/2
        rangespec = USL - LSL
        totalNum = len(points)
        for i in points: 
            if (i > USL) or (i < LSL) :
                defect.append(i)
            else:
                good.append(i)
        
        goodRate = len(good) / totalNum

        ngroup = int(len(df))/int(measureAmount)
        if (ngroup.is_integer() == False):
            cpkarr = np.array_split(points[::-1],len(points)//measureAmount) #revserve to split coz the array_split method
            cpkarrMEAN = [np.mean(i) for i in cpkarr]
            sigmaCpk = np.std(cpkarrMEAN,ddof=1) #pd.std() >>> //(n)
        else:
            cpkarr = np.array_split(points,ngroup)
            cpkarrMEAN = [np.mean(i) for i in cpkarr]
            sigmaCpk = np.std(cpkarrMEAN,ddof=1) # numpy standard deviation >>> //(n-1)
        cp_mean = np.mean(points)
        sigmaPpk = np.std(points,ddof=1)
 
        assert sigmaPpk != 0
        assert sigmaCpk != 0
        if (sigmaCpk == 0) or (sigmaPpk == 0):
            raise Exception('SigmAomaly')
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
        CPR = sigmaPpk, sigmaCpk, len(good), totalNum, goodRate ,USL,LSL,UCL,LCL,cp_mean,Target ,rangespec, Cpu, Cpl, Cp, Ck, Cpk, Ppk
        keys = ["sigma","groupSigma","good","totalNum","goodRate","USL","LSL","UCL","LCL","overallMean","target","range","Cpu","Cpl","Cp","Ck","Cpk","Ppk"]
        capability = dict(zip(keys, CPR))
        ### Reference :https://en.wikipedia.org/wiki/Process_performance_index
        return capability # total 17 + 2
    
    def nelson(points, lsl, usl):
        points = [ float(i) for i in points.split(',')]
        nelsonBool = apply_rules(original=points) # markup points after rules verified
        specs = checkspec(pts=points, lsl=float(lsl), usl=float(usl))
        # print(specs)
        # nelsonBool = nelsonBool.append(check_lsl_usl)
        df_list = nelsonBool.values.tolist()
        # print(df_list)
        """
        Another parsing method requires to be mentioned.
         NelsonContext = pd.DataFrame()
         for j in range(len(NelsonCol)):
             NelsonContext[NelsonCol[j]] = [item[j] for item in df_list]
        """
        data = [item[0] for item in df_list]
        rule1 = [item[1] for item in df_list]
        rule2 = [item[2] for item in df_list]
        rule3 = [item[3] for item in df_list]
        rule4 = [item[4] for item in df_list]
        rule5 = [item[5] for item in df_list]
        rule6 = [item[6] for item in df_list]
        rule7 = [item[7] for item in df_list]
        rule8 = [item[8] for item in df_list]
        NelsonCol = ["data","rule1","rule2","rule3","rule4","rule5","rule6","rule7","rule8","specs"]
        columnValue = [data,rule1 ,rule2,rule3,rule4,rule5,rule6,rule7,rule8,specs]
        NelsonContext = dict(zip(NelsonCol,columnValue))
        print('NelsonContext', NelsonContext)
        # NelsonContext = json.loads(NelsonContext.to_json(orient="split"))
        return NelsonContext
