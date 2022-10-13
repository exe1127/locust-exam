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

# response = requests.post('https://btntbw73c9.execute-api.us-east-1.amazonaws.com/Prod/addfan', headers=headers, json=json_data)

# params = {
#     "userId": "qa-1",
#     "starId": "qa-1"
# }

headers2 = {
    'authority': 'btntbw73c9.execute-api.us-east-1.amazonaws.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'es-419,es;q=0.9',
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
# class Queue(SequentialTaskSet):
#     @task
#     def advance(self):
#         self.client.post("/processqueue", headers=headers,json={'starId': '1'})
                         
class Initialized(SequentialTaskSet):

    @task
    def enable(self):
        self.client.post("/enableQueue", headers=headers, json={'starId': '3'})

    @task
    def addfan(self):
        for id in [1,2,3,4,5]:
            self.client.post('/addfan', headers=headers, json={
            'starId': '3',
            'userId': id
        })

    # @task
    # def position(self):
    #     self.client.get("/queueposition?",  params=json_data, headers=headers)

    # tasks = [Queue]


class Request(HttpUser):
    host = "https://btntbw73c9.execute-api.us-east-1.amazonaws.com/develop"

    tasks = [Initialized]

    wait_time = between(1, 5)

    # @task
    # def clearqueue(self):
    #     self.client.post("/clearqueue", headers=headers, json={'starId': '1',})

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
