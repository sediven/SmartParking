from datetime import datetime
from math import ceil


class Car(object):
    __inTime = False
    __owner = False
    __carId = False
    __outTime = False
    __w = False
    __k = False

    def __init__(self, __carId, __owner, __inTime, __outTime):
        self.__carId = __carId
        self.__owner = __owner
        self.__inTime = __inTime
        self.__outTime = __outTime

    def getTimeInside(self):
        d1 = datetime.strptime(self.__inTime, "%Y-%m-%d %H:%M:%S")
        d2 = datetime.strptime(self.__outTime, "%Y-%m-%d %H:%M:%S")
        return ceil(abs((d2 - d1)).seconds / 3600.0)

    def getOwner(self):
        return self.__owner

    def getCarId(self):
        return self.__carId

    def getPlace(self):
        return (self.__w, self.__k)

    def parkCar(self, w, k):
        self.__w = w
        self.__k = k

    def takeCar(self):
        self.__w = -1
        self.__k = -1

    def changeOutTime(self, time):
        self.__outTime = time

    def changeInTime(self, time):
        self.__inTime = time