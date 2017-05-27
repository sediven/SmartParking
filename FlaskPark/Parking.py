from ParkingSpace import Space

class Parking(object):
    def __init__(self, rows, colums):
        self.rows = rows
        self.colums = colums
        self.parkingPlaces = [[Space('w' + str(w) + 'k' + str(k)) for k in range(colums)] for w in range(rows)]

        self.buildRoades()
        self.orderPlaces()

    def getParkingStatus(self):
        wynik = 0
        for i in self.orderedPlaces.values():
            wynik += len(i)
        return wynik

    def getTab(self):
        return [[str(e.getSpaceStatus()) for e in row] for row in self.parkingPlaces]

    def printMe(self):
        s = [[str(e.getSpaceStatus()) for e in row] for row in self.parkingPlaces]
        # lens = [max(map(len, col)) for col in zip(*s)]
        # fmt = ''.join('{{:{}}}'.format(x) for x in lens)
        # table = [fmt.format(*row) for row in s]
        return s

    def buildRoades(self):
        for row in range(self.rows):
            for col in range(1, self.colums, 3):
                self.parkingPlaces[row][col].makeRoad()
        for i in self.parkingPlaces[0]:
            i.makeRoad()

    def orderPlaces(self):
        self.orderedPlaces = {}
        for row in range(self.rows):
            for col in range(self.colums):
                if self.parkingPlaces[row][col].checkIfCanPark():
                    try:
                        self.orderedPlaces[row + col].append((row, col))
                    except:
                        self.orderedPlaces[row + col] = [(row, col)]

    def parkCar(self, car):
        place = self.findPlace(car)
        self.parkingPlaces[place[0]][place[1]].parkCar(car)
        car.parkCar(*place)
        return self.findRoad((0, 0), place)

    def takeCar(self, car):

        row, col = place = car.getPlace()
        spot = self.parkingPlaces[row][col]
        if spot.checkCarId(car.getCarId()) and spot.checkOwner(car.getOwner()):
            spot.leaveCar()
            return self.findRoad((0, 0), place, wjazd=False)

    def findPlace(self, car):
        time_inside = car.getTimeInside()
        print
        time_inside
        if time_inside >= 8:
            place = self.findEndPlace()
        elif time_inside >= 4:
            place = self.findMiddlePlace()
        else:
            place = self.findClosePlace()
        return place

    def findClosePlace(self):
        for i in self.orderedPlaces.keys():
            if not len(self.orderedPlaces[i]):
                self.orderedPlaces.pop(i)
            else:
                return self.orderedPlaces[i].pop()
        return False

    def findMiddlePlace(self):
        lista = self.orderedPlaces.keys()
        for i in lista[len(lista) / 3:]:
            if not len(self.orderedPlaces[i]):
                self.orderedPlaces.pop(i)
            else:
                return self.orderedPlaces[i].pop()
        return self.findClosePlace()

    def findFarPlace(self):
        lista = self.orderedPlaces.keys()
        for i in lista[::-1]:
            if not len(self.orderedPlaces[i]):
                self.orderedPlaces.pop(i)
            else:
                return self.orderedPlaces[i].pop()
        return False

    def findRoad(self, begin, end, wjazd=True):
        """idziemy od enda (pola naszego samochodzu) znajdujemy wyjazd pkt 0,0"""
        wierszA, kolA = begin
        wierszB, kolB = end
        lista = []
        lista.append(end)
        kolR = kolB - 1 if self.parkingPlaces[wierszB][kolB - 1].isRoad() else kolB + 1 if self.parkingPlaces[wierszB][
            kolB + 1].isRoad() else False
        for i in range(wierszB, -1, -1):
            lista.append((i, kolR))
        for i in range(kolR - 1, -1, -1):
            lista.append((0, i))

        if wjazd:
            lista = lista[::-1]
        return lista
