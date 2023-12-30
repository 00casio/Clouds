from locust import HttpUser, task

class QuickstartUser(HttpUser):
    @task
    def invoke_microservice(self):
        self.client.get("/numericalintegralservice/0.0/3.14")
