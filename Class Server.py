class Server:
    def __init__(self, hostname, status, cpu_usage):
        self.hostname = hostname
        self.status = status
        self.cpu_usage = cpu_usage

    def boot(self):
        self.status = "Running"
        print(f"{self.hostname} is booting")

    def shutdown(self):
        self.status = "Off"
        print(f"{self.hostname} is shutting down")

    def increase_load(self):
        self.cpu_usage += 10
        print(f"CPU Usage: {self.cpu_usage}%")

    def display_status(self):
        return f"Hostname: {self.hostname}, Status: {self.status}, CPU Usage: {self.cpu_usage}%"


Server1 = Server("Server01", "Off", 20)
print(Server1.display_status())

Server1.boot()
print(Server1.display_status())

Server1.increase_load()
print(Server1.display_status())

Server1.shutdown()
print(Server1.display_status())