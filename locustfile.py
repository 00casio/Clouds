from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def invoke_microservice(self):
        self.client.get("/api/http_trigger?lower=0.0&upper=1000")
