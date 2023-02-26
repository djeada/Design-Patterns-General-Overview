'''
In this example, there is a Subject abstract class that defines the interface for the RealSubject class that does the actual work. The Proxy class acts as a wrapper around the RealSubject object and intercepts requests to it. The Proxy class checks if the client has access to the RealSubject object and logs the time of the request.

When the client makes a request through the Proxy object, it first checks if the client has access to the RealSubject object. If the access check passes, the request is forwarded to the RealSubject object to handle. The Proxy object also logs the time of the request.
'''

from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self):
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    proxy.request()

