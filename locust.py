from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)
    host = "http://20.232.41.73:5000"  

    @task
    def invoke_microservice(self):
        self.client.get("/numericalintegralservice/0.0/3.14")
