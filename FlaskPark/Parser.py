import json
from Car import Car

class ParserInput(object):
    """ parsujemy liste wydarzeń które dostaliśmy
        format wydarzeń
        Zarzadzamy wydarzeniami
    """

    def __init__(self, lines):
        self.lines = lines

    def giveMeJson(self, dictionary):
        return json.dumps(dictionary, sort_keys=True, separators=(',', ': '))

    # def giveMeDict(self, stringi):
    #     return json.loads(stringi)

    def orderByDate(self, dic):
        return sorted(dic.items(), key=lambda x: x[1]['dataNow'])

    def manageCars(self):
        cars = []
        for i in self.dictLines:
            i = i[1]
            idk = i['car']['carId']
            owner = i['car']['owner']
            if i['typ'] == 'in':
                out = i['car']['dataOut']
                inp = i['dataNow']
            elif i['typ'] == 'out':
                inp = i['car']['dataIn']
                out = i['dataNow']
            cars.append(Car(idk, owner, inp, out))
        return cars

    def parseMyLines(self):
        self.dictLines = self.orderByDate(self.lines)


    def doNextEvent(self):
        event = self.dictLines.pop(0)
        try:
            ind = event[1]['car']['dataIn']
            return (0,event)
        except:
            out =  event[1]['car']['dataOut']
            return (1, event)

    def getNextEvent(self):
        return self.dictLines.__getitem__(0)[1]['dataNow']