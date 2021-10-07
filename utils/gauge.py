# from api.specBound import check_lsl_usl
from numpy.core.fromnumeric import partition
from utils.PlotnelsonRules import *
import numpy as np
import pandas as pd
import re

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
    def wipe_out_nan(pts):
        return [i.strip() for i in pts if bool(i and not i.isspace())]

    def sliding_chunker(original, segment_len, slide_len):
        chunks = []
        for pos in range(0, len(original), slide_len):
            chunk = np.copy(original[pos:pos + segment_len])
            if len(chunk) != segment_len:
                continue
            chunks.append(chunk)
        return chunks


    def stats(points,LSLlst,USLlst,measureAmount,stdValue): #good,defect,
        points = [i for i in (points.split(','))]
        # points = pd.DataFrame(points)
        # print('print(points)',points)
        # points = [ float(i) for i in enumerate(points.split(','))]
        # [dict([i, int(x)] for i, x in b.items()) for b in list]
        LSLlst,USLlst,measureAmount,stdValue = [ float(i) for i in (LSLlst,USLlst,measureAmount,stdValue)]
        # print('LSLlst,USLlst,measureAmount,stdValue', LSLlst,USLlst,measureAmount,stdValue)
        specification = [LSLlst,USLlst,measureAmount,stdValue]
        specificationcols = ["LSLlst","USLlst","measureAmount","stdValue"]
        df = pd.DataFrame(dict(zip(specificationcols, specification)),index= [0])
        # df = np.array([LSLlst,USLlst,measureAmount,stdValue]).astype(float)#,index=integer_array) 
        
        Target = df['stdValue'].astype('float64')
        LSLlst = df['LSLlst'].astype('float64')
        USLlst = df['USLlst'].astype('float64')
        countgooddefect = []
        measureAmount = int(df['measureAmount'])
        # print('measureAmount',measureAmount)
        USL = Target + USLlst
        LSL = Target - LSLlst
        LCL = (LSL + Target)/2
        UCL = (USL + Target)/2
        rangespec = USL - LSL
        totalNum = len(points)
        # pointslst = [list() for i in map(str,range(len(points)//measureAmount))]
        print('len(points)//measureAmount',len(points)//measureAmount)
        # points = np.array_split(points, len(points)//measureAmount)
        
        points = Gauge.sliding_chunker(points, segment_len = measureAmount, slide_len = len(points)//measureAmount )
        print('::::: \n',points)
        print(':::::: \n')
        # print(pointslst)
        print('------------------',type(USL),LSL,LCL,UCL)
        # print('aa \n',points[0])
        # trim = points[1]
        # # pp = [item.apply(lambda x: x.str.strip()) for item in trim] #item.strip(' ') x.str.strip(' ')
        # print('pppp',type(points[0][0]))
        # for item in trim:
        #     if (bool(item and not item.isspace()) == False):
        #         print('F')
            # nonenum.append(item.strip(' '))
        # print('strip\n', pp)
        pointslst = [[i.strip() for i in lst if bool(i and not i.isspace())] for lst in points] # iterate 1st_outer list, 2nd_inner list
        pointslst = [[float(i) for i in lst ] for lst in pointslst]
        print('///point_into_subgroup////', pointslst)
        # print('///point_into_subgroup////', pointslst)
        # print('aa',aa)
            # for i in item:
            #     if (bool(i and not i.isspace()) == False): # check the empty , None or blank
            #         nonenum += 1
            #         print('vvvv', type(i))
            #     else:
            #         flags = 0
            #         pointslst[flags].append(i)
            #         print('series',i)
        
        # print('len(points)',points)
        # subgroup1_num = len(points) - nonenum
        print('gooddefectcount')
        for lst in pointslst:
            for item in lst:
                if (item > USL.item() or item < LSL.item()) :
                    # print('1',item)
                    countgooddefect.append(1)
                else:
                    # print('0',item)
                    countgooddefect.append(0)
        # points = points.str.rsplit( n = measureAmount)
        
        goodRate = countgooddefect.count(0)/ totalNum
        print('///////', goodRate)
        cpkarrMEAN = [np.mean(i) for i in pointslst]
        sigmaCpk = np.std(cpkarrMEAN,ddof=1) #pd.std() >>> //(n)
        print('///////', cpkarrMEAN,sigmaCpk)

        # ngroup = len(points)/measureAmount
        # if (ngroup.is_integer() == False):
        #     cpkarr = np.array_split(points[::-1],len(points)//measureAmount) #revserve to split coz the array_split method
        #     cpkarrMEAN = [np.mean(i) for i in cpkarr]
        #     sigmaCpk = np.std(cpkarrMEAN,ddof=1) #pd.std() >>> //(n)
        # else:
        #     cpkarr = np.array_split(points,ngroup)
        #     cpkarrMEAN = [np.mean(i) for i in cpkarr]
        #     sigmaCpk = np.std(cpkarrMEAN,ddof=1) # numpy standard deviation >>> //(n-1)
        flatten_pointslst = [val for sublist in pointslst for val in sublist]
        cp_mean = np.mean(flatten_pointslst)
        sigmaPpk = np.std(flatten_pointslst,ddof=1)
 
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
        CPR = sigmaPpk, sigmaCpk, countgooddefect.count(0), totalNum, goodRate ,USL.item(),LSL.item(),UCL.item(),LCL.item(),cp_mean,Target.item() ,rangespec.item(), Cpu.item(), Cpl.item(), Cp.item(), Ck.item(), Cpk, Ppk
        keys = ["sigma","groupSigma","good","totalNum","goodRate","USL","LSL","UCL","LCL","overallMean","target","range","Cpu","Cpl","Cp","Ck","Cpk","Ppk"]
        capability = dict(zip(keys, CPR))
        print('capability',capability)
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
