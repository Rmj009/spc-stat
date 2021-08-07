# from app import app
from flask import request
from ..utils.gauge import Gauge

def GormToCPR(app):
    @app.route("/v1/capability-new", methods=['GET'])
    def CPR():
        points = request.args.get('points')
        usllst = request.args.get('USL') 
        lsllst = request.args.get('LSL')
        goodlst = request.args.get('good')
        defectlst = request.args.get('defect')
        measureAmount = request.args.get('measureAmount') #measureAmount
        stdValue = request.args.get('stdValue')
        try:
            if (points == None) or (len(points) == 0):
                result = 'PointsInvaild'
                return result, 400
            elif (usllst == None) or (len(usllst) == 0):
                result = 'USLInvaild'
                return result, 400
            elif (lsllst == None) or (len(lsllst) == 0):
                result = 'LSLInvaild'
                return result, 400
            elif (goodlst == None) or (len(goodlst) == 0):
                result = 'GOODInvaild'
                return result, 400
            elif (defectlst == None) or (len(defectlst) == 0):
                result = 'DefectInvaild'
                return result, 400
            elif (measureAmount == None) or (len(measureAmount) == 0):
                result = 'measureAmountInvaild'
                return result, 400
            elif (stdValue == None) or (len(stdValue) == 0):
                result = 'StdValueInvaild'
                return result, 400
            else:
                # GormResult = [points,[goodlst],[defectlst],[lsllst],[usllst],[measureAmount],[stdValue]]
                # CapabilityCol = ["points","goodlst","defectlst","lsllst","usllst","measureAmount","stdValue"]
                # GormResults = dict(zip(CapabilityCol, GormResult))
                result = Gauge.stats(points,goodlst,defectlst,lsllst,usllst,measureAmount,stdValue)
                return result, 200
        except Exception as errors:
            print('error',errors)
            return 'CalcFail', 500