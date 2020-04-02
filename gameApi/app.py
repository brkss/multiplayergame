import requests


class Api:
    def __init__(self, url, name):
        self.URL = url
        self.name = name

    def sendData(self, index, x, y, shoot=False, bx=0, by=0):
        data = {"name": self.name, "index": index, "x": x, "y": y, "shoot": shoot, "bx": bx, "by": by}
        resp = requests.post(self.URL + '/b', data=data)
        return resp.text

    def getData(self):
        rq = requests.get(url=self.URL + "/g/" + self.name)
        resp = rq.json()
        return [resp[0]['index'], resp[0]['x'], resp[0]['y'], resp[0]['shoot'], resp[0]['bx'], resp[0]['by']]

    def quit(self):
        requests.get(url=self.URL + "/q/"+self.name)
        return 1



api = Api('http://localhost:3000',"Brahim")
print(api.sendData(7,200,200))

api2 = Api('http://localhost:3000',"Player")
print(api2.sendData(7,200,200,False,-1,-1))

for i in range(10):
    if i == 3 :
        api2.sendData(7,200,200,True,0,1)
    elif i == 7 :
        api2.sendData(7,200,200,False,150,120)
    print(api.getData())


api.quit()
