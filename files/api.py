import requests


class api:
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


