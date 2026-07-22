from collections import deque

class Person:
    def __init__(self, name, dpi, email, rating):
        self.name = name
        self.dpi = dpi
        self.email = email
        self.rating = rating

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) >= 3:
            self._name = name
        else:
            print("Nombre incorrecto")

    @property
    def dpi(self):
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        if len(dpi)==13:
            self._dpi = dpi
        else:
            print("DPI incorrecto")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if '@' in email:
            self._email = email
        else:
            print("Correo incorrecto")

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating

    def show_information(self):
        print("Nombre:", self.name)
        print("DPI:", self.dpi)
        print("Correo:", self.email)

class User(Person):
    def __init__(self, name, dpi, email, rating, address):
        super().__init__(name,dpi,email, rating)
        self.address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    def show_information(self):
        print("Nombre:", self.name)
        print("DPI:", self.dpi)
        print("Correo:", self.email)
        print("Dirección:", self.address)

class Worker(Person):
    def __init__(self, name, dpi, email, job_type, rating, reviews):
        super().__init__(name,dpi,email, rating)
        self.job_type = job_type
        self.reviews = reviews

    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        if len(job_type)>=3:
            self._job_type = type
        else:
            print("Tipo de trabajo incorrecto")

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    def show_information(self):
        print("Nombre:", self.name)
        print("DPI:", self.dpi)
        print("Correo:", self.email)
        print("Tipo de trabajo:", self.type)
        print("Reseñas:", self.reviews)

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
    def size(self):
        return len(self.items)

class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def peek_left(self):
        if len(self.items) > 0:
            return self.items[0]
        else:
            return None

    def dequeue(self):
        if len(self.items) > 0:
            return self.items.popleft()
        else:
            return None

    def size(self):
        return len(self.items)