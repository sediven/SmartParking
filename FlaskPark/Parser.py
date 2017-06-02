import json
from Car import Car

class ParserInput(object):
    """ parsujemy liste wydarzeń które dostaliśmy
        format wydarzeń
        Zarzadzamy wydarzeniami
    """
    cars = []
    def __init__(self, lines):
        self.lines = lines
        self.parseMyLines()
        self.manageCars()

    def giveMeJson(self, dictionary):
        return json.dumps(dictionary, sort_keys=True, separators=(',', ': '))

    def orderByDate(self, dic):
        return sorted(dic.items(), key=lambda x: x[1]['dataNow'])

    def manageCars(self):
        for i in self.dictLines:
            i = i[1]
            idk = i['car']['carId']
            owner = i['car']['owner']
            if i['typ'] == 'in':
                out = i['car']['dataOut']
                inp = i['dataNow']
                self.cars.append(Car(idk, owner, inp, out))


    def parseMyLines(self):
        self.dictLines = self.orderByDate(self.lines)


    def doNextEvent(self):
        event = self.dictLines.pop(0)
        try:
            #ma out znaczy że wjeżdża z przewidywaną data wyjazdu
            ind = event[1]['car']['dataOut']
            return (0,event)
        except:
            out = event[1]['dataNow']
            return (1, event)

    def getNextEvent(self):
        try:
            return self.dictLines.__getitem__(0)[1]['dataNow']
        except:
            return False