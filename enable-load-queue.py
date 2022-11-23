import random
from listname.openCSV import listName
from locust import HttpLocust, HttpUser, SequentialTaskSet, TaskSet, task, between
from locust.exception import StopUser

headers = {
    'authority': 'btntbw73c9.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer 12345',
    'origin': 'http://react-demo-aws-starkix.s3-website-us-east-1.amazonaws.com',
    'referer': 'http://react-demo-aws-starkix.s3-website-us-east-1.amazonaws.com/',
    'sec-ch-ua': '"Chromium";v="106", "Microsoft Edge";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
}

value = [1, 2, 3, 4, 5]
value2 = []
name = listName()
band = True


class Fan(SequentialTaskSet):
    @task
    def addfan(self):
        for i in range(1, 50):
            self.client.post('/addfan', headers=headers, json={
                'starId': random.choice(value2),
                'userId': random.choice(name)
            })
        raise StopUser()


class Initialized(SequentialTaskSet):

    def on_start(self):
        if len(value) > 0:
            self.ran = random.choice(value)
            value2.append(self.ran)
            value.remove(self.ran)
            self.band = band

            # print(f'vlue {value}')

    @task
    def enable(self):

        if value != []:
            self.client.post("/enableQueue", headers=headers,
                             json={'starId': self.ran})
        else:
            if self.band:
                self.client.post("/enableQueue", headers=headers,
                                 json={'starId': self.ran})
        self.band = False

    wait_time = between(5, 15)
    tasks = [Fan]


class Request(HttpUser):
    host = "https://btntbw73c9.execute-api.us-east-1.amazonaws.com/develop"
    wait_time = between(10, 15)
    tasks = [Initialized]
