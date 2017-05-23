class Space:
    __isCarParked = False
    __carOwner = False
    __carId = False

    def __init__(self, spaceId):
        '''
        Constructor
        '''
        self.__isRoad = False
        self.__isCarParked = False
        self.__spaceId = spaceId
        self.__carOwner = False
        self__carId = False

    def getSpaceStatus(self):
        return 'R' if self.__isRoad else 'O' if self.__isCarParked else "F"

    def makeRoad(self):
        self.__isRoad = True

    def isRoad(self):
        return self.__isRoad

    def parkCar(self, car):
        '''
        The method is to set the park-car-flag to true to execute the action of parking
        '''

        self.__isCarParked = True
        self.__carOwner = car.getOwner()
        self.__carId = car.getCarId()

    def checkCarId(self, cId):
        return self.__carId == cId

    def checkOwner(self, name):
        return self.__carOwner == name

    def leaveCar(self):
        '''
        The method for cars leaving
        '''
        self.__isCarParked = False
        self.__carOwner = False
        self.__carId = False

    def checkIfCanPark(self):
        '''
        The method is to check if the space has a car parking here
        '''
        return (not self.__isCarParked) and (not self.__isRoad)