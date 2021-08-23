import numpy as np

"""
References: 
Douglas C. Montgomery-Introduction to statistical quality control 7th edtition-Wiley (2009)
Part III chapter 8.3, p362.-p372
"""
class Calculator(object):
    def __init__(self, spmcUUID, sequences):
        self.sequences = sequences
        self.spmcUUID = spmcUUID

    def __del__(self,object):  #1>>> cleanup the seq, 2>>> return the seq after drop point(s)
        print('drop points...')
        # dropindex = np.argwhere(max(object) or min(object))
        sequences = np.delete(object,object[1]) #specific points
        return sequences

    def __repr__(self) -> str:
        print(f"SpcMeasurePointConfigUUID: {self.spmcUUID}")
        
        return super().__repr__()

    def calc(datatables):
        try:
            datatables = datatables[datatables.valuelst != -88888888]
            # print('###Dataframe###',datatables.head(),sep='\n')
            goodNum = len(datatables['goodlst']) 
            defectNum = len(datatables[datatables.defectlst > 0])
            totalNum = goodNum + defectNum
            goodRate = goodNum / totalNum
            Target = datatables.stdValue[0]
            USL = Target + datatables['usllst'][0]
            LSL = Target - datatables['lsllst'][0]
            LCL = (LSL + Target)/2
            UCL = (USL + Target)/2
            rangespec = USL - LSL
            ngroup = int(datatables.shape[0])/int(datatables.amount[1])
            if (ngroup.is_integer() == False):
                cpkarr = datatables['valuelst'].sort_index(axis = 0,ascending = False) #coz the array_split method 
                cpkarr = np.array_split(cpkarr,datatables.shape[0]//datatables.amount[1])
                cpkarrMEAN = [np.mean(i) for i in cpkarr]
                sigmaCpk = np.std(cpkarrMEAN,ddof=1) #pd.std() >>> //(n)
            else:
                cpkarr = np.array_split(datatables['valuelst'],ngroup)
                cpkarrMEAN = [np.mean(i) for i in cpkarr]
                sigmaCpk = np.std(cpkarrMEAN,ddof=1) # numpy standard deviation >>> //(n-1)
            cp_mean = np.mean(datatables['valuelst'])
            sigmaPpk = np.std(datatables['valuelst'],ddof=1)
            if (sigmaCpk == 0) or (sigmaPpk == 0):
                raise Exception('unreasonable anomaly') 
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
            CPR = sigmaPpk, sigmaCpk, goodNum, totalNum, goodRate ,USL,LSL,UCL,LCL,cp_mean,Target ,rangespec, Cpu, Cpl, Cp, Ck, Cpk, Ppk
            keys = ["sigma","group-sigma","good","totalNum","goodRate","USL","LSL","UCL","LCL","overallMean","target","range","Cpu","Cpl","Cp","Ck","Cpk","Ppk"]
            capability = dict(zip(keys, CPR))
            ### Reference :https://en.wikipedia.org/wiki/Process_performance_index
            return capability # total 17
        except ZeroDivisionError as e:
            print('sigma zero result from variance: '+ str(e))
            print("fix infinity", None)
        except Exception as error:
            print('CALC_ERROR',error)
            return error

