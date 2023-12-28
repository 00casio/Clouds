from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "http://localhost:5000"  # Update this with your microservice's base URL

    @task
    def invoke_microservice(self):
        self.client.get("/numericalintegralservice/0.0/3.14")
