from locust import HttpUser, task, between, constant

headers = {
    'authority': 'btntbw73c9.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-419,es;q=0.9',
    # Already added when you pass json=
    # 'content-type': 'application/json',
    'origin': 'http://localhost:3000',
    'referer': 'http://localhost:3000/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

json_data = {
    'starId': '4',
    'userId': '4',
}

# response = requests.post('https://btntbw73c9.execute-api.us-east-1.amazonaws.com/Prod/addfan', headers=headers, json=json_data)

# params = {
#     "userId": "qa-1",
#     "starId": "qa-1"
# }

headers2 = {
    'authority': 'btntbw73c9.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-419,es;q=0.9',
    'origin': 'http://localhost:3000',
    'referer': 'http://localhost:3000/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = {
    'starId': '1',
    'userId': '1',
}

class Request(HttpUser):
    host = "https://btntbw73c9.execute-api.us-east-1.amazonaws.com/Prod"
    wait_time = between(1, 5)

    @task
    def position(self):
        self.client.get("/queueposition?",  params=params, headers=headers2)

    @task
    def addfan(self):
        self.client.post('/addfan', headers=headers, json=json_data)

    @task
    def processqueue(self):
        self.client.post("/processqueue", headers=headers, json=json_data)

    @task
    def clearqueue(self):
        self.client.post("/clearqueue", headers=headers, json=json_data)

    @task
    def enableQueue(self):
        self.client.post("/enableQueue", headers=headers, json=json_data)

    # @task
    # def createUser(self):
    #     self.client.post("/api/users/", data='''{
    #         "name": "morpheus",
    #         "job": "leader",
    #         "id": "946",
    #         "createdAt": "2022-09-30T20:17:22.110Z"
    #     }''')


'''https://btntbw73c9.execute-api.us-east-1.amazonaws.com/Prod/'''
'''GET queueposition?starId=${starId}&userId=${userId}'''
'''POST /addfan
{
      "starId": starId,
      "userId": userId
    }'''

'''POST /processqueue
{
      "starId": starId
    } sacar usuario'''


'''POST /clearqueue
{
      "starId": starId
    }'''

'''POST /enableQueue
{
      "starId": starId
    } iniciar la cola'''


# los ides son cualquiera no hay validaciones
