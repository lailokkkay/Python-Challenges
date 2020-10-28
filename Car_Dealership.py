import datetime

class CarRecord:
    def __init__(instance, VehicleID, Registration, DateOfRegistration, EngineSize, PurchasePrice):
        instance.VehicleID = VehicleID
        instance.Registration = Registration
        instance.DateOfRegistration = DateOfRegistration
        instance.EngineSize = EngineSize
        instance.PurchasePrice = PurchasePrice

carDealership = []

carA = CarRecord("1234i2902h3", "wqerwrf", datetime.datetime(2001,3,12), 325, 89235)
carDealership.append(carA)
carB = CarRecord('190jd0923', "osjdaf", datetime.datetime(1901,7,20), 2546346, 3456)
carDealership.append(carB)
carC = CarRecord('sfoin90385', "bvkcna", datetime.datetime(2401,1,2), 84590, 0)
carDealership.append(carC)
