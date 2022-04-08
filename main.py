from locust import HttpUser, between, task
import requests
import random


# r = requests.post('http://sbarportal.ru/api/search', json=body, params={"text": "Газпром"})
# print(r)



class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    host = "https://fa91-194-85-115-170.ngrok.io/"

    @task
    def miliesearche(self):
        rtext = ["Газ", "Строительная", "Газпром", "Аксиома", "Зазекс", "Кашапова", "ТОТ", "Запрос" ]
        body = {"page": 1, "page_size": 10, "autocomplete": True}
        self.client. post('api/search', json=body, params={"text": random.choice(rtext)})

