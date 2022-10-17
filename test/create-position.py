from locust import HttpUser, SequentialTaskSet, task, between

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

json_data = {
    'starId': '1',
    'userId': '4',
}


class Queue(SequentialTaskSet):
    @task
    def advance(self):
        for id in range(1,4):
            self.client.post("/processqueue", headers=headers,
                             json={'starId': '3'})
            self.user.environment.runner.stop()
    @task
    def position(self):
        self.client.get("/queueposition?",  params={'starId': '3'}, headers=headers)

class Initialized(SequentialTaskSet):

    @task
    def enable(self):
        for id in range(1,4):
            self.client.post("/enableQueue", headers=headers,
                             json={'starId': id})

    @task
    def addfan(self):
        for id in [1, 2, 3, 4, 5]:
            for id2 in range(1,4):
                self.client.post('/addfan', headers=headers, json={
                    'starId': id2,
                    'userId': id
                })

    tasks = [Queue]


class Request(HttpUser):
    host = "https://btntbw73c9.execute-api.us-east-1.amazonaws.com/develop"
    wait_time = between(1, 5)
    tasks = [Initialized]
