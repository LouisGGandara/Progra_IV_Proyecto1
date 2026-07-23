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

class Customer(Person):
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
    def __init__(self, name, dpi, email, rating, job_type, reviews, status):
        super().__init__(name,dpi,email, rating)
        self.job_type = job_type
        self.reviews = reviews
        self.status = status

    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        if len(job_type)>=3:
            self._job_type = job_type
        else:
            print("Tipo de trabajo incorrecto")

    @property
    def reviews(self):
        return self._reviews

    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    def show_information(self):
        print("Nombre:", self.name)
        print("DPI:", self.dpi)
        print("Correo:", self.email)
        print("Tipo de trabajo:", self.job_type)
        print("Reseñas:", self.reviews)
class Service:
    def __init__(self, customer,job_type, description):
        self.customer = customer
        self.job_type = job_type
        self.description = description

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer=customer

    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        self._job_type=job_type

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) >= 5:
            self._description = description
        else:
            print("Descripción incorrecta")


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

#Agregue una lista workers, esto para la validación de los DPI'S (Para que no se repita el dpi)
customers = []
workers = []
plumbers = Stack()
electricians = Stack()
builders = Stack()
it_professionals = Stack()

def registers_customers():
    while True:
        name=input("Ingrese su nombre: ")
        if len(name)>=3:
            break
        else:
            print("Nombre incorrecto, vuela a intentarlo")
    while True:
        dpi=input("Ingrese su DPI: ")
        isDpi=False
        if len(dpi)==13:
            for c in customers:
                if c.dpi==dpi:
                    print("Error esté Dpi ya esta registrado, ingrese otro")
                    isDpi=True
                    break
            if isDpi==False:
                break
        else:
            print("El DPI debe tener exactamente 13 dígitos")
    while True:
        email=input("Ingrese su correo: ")
        if "@" in email:
            break
        else:
            print("Correo incorrecto, vuela a intentarlo")
    address=input("Ingrese su dirección: ")
    new_customer = Customer(name,dpi,email,0,address)
    customers.append(new_customer)

def registers_workers():
    while True:
        name=input("Ingrese su nombre: ")
        if len(name)>=3:
            break
        else:
            print("Nombre incorrecto, vuela a intentarlo")

    while True:
        dpi=input("Ingrese su DPI: ")
        isDpi=False
        if len(dpi)==13:
            for c in customers:
                if c.dpi==dpi:
                    isDpi=True
                    break

            if isDpi==False:
                for w in workers:
                    if w.dpi == dpi:
                        isDpi = True
                        break
            if isDpi:
                print("Error esté Dpi ya esta registrado, ingrese otro")
            else:
                break
        else:
            print("El DPI debe tener exactamente 13 dígitos")

    while True:
        email=input("Ingrese su correo: ")
        if "@" in email:
            break
        else:
            print("Correo incorrecto, vuela a intentarlo")

    while True:
        print("\t¿Qué tipo dee trabajo haces?")
        print("1. Plomería")
        print("2. Electricidad")
        print("3. Construcción")
        print("4. Técnicos informáticos")
        print("5. Volver al menú principal")
        choice = int(input("Seleccione una opción: "))
        match choice:
            case 1:
                work="Plomería"
                break
            case 2:
                work="Electricidad"
                break
            case 3:
                work="Construcción"
                break
            case 4:
                work="Técnicos informáticos"
                break
            case 5:
                print("Volviendo al menú principal...")
                return
            case _:
                print("Opción incorrecta, vuelva a intentarlo")

    new_worker=Worker(name,dpi,email,0,work,[], "Disponible")
    workers.append(new_worker)

    if work =="Plomería":
        plumbers.push(new_worker)
    elif work =="Electricidad":
        electricians.push(new_worker)
    elif work =="Construcción":
        builders.push(new_worker)
    elif work=="Técnicos informáticos":
        it_professionals.push(new_worker)

jobs = Queue()

def register_services():
    if len(customers)==0:
        print("No hay clientes registrados.")
        return
    else:
        while True:
            dpi = input("Ingrese su DPI: ")
            isDpi = False
            if len(dpi) == 13:
                for c in customers:
                    if c.dpi == dpi:
                        customer_found=c
                        isDpi = True
                        break
                if isDpi:
                    while True:
                        print("\t¿Qué servicio necesita?")
                        print("1. Plomería")
                        print("2. Electricidad")
                        print("3. Construcción")
                        print("4. Técnicos informáticos")
                        print("5. Volver al menú principal")
                        choice = int(input("Seleccione una opción: "))
                        match choice:
                            case 1:
                                if plumbers.size()==0:
                                    print("No hay plomeros registrados.")
                                    return
                                else:
                                    work="Plomería"
                                    break
                            case 2:
                                if electricians.size()==0:
                                    print("No hay electricistas registrados.")
                                    return
                                else:
                                    work="Electricidad"
                                    break
                            case 3:
                                if builders.size()==0:
                                    print("No hay constructores registrados.")
                                    return
                                else:
                                    work="Construcción"
                                    break
                            case 4:
                                if it_professionals.size()==0:
                                    print("No hay técnicos informáticos registrados.")
                                    return
                                else:
                                    work="Técnicos informáticos"
                                    break
                            case 5:
                                print("Volviendo al menú principal...")
                                return
                            case _:
                                print("Opción incorrecta, vuelva a intentarlo")
                    while True:
                        description=input("Describa su problema: ")
                        if len(description)>=5:
                            break
                        else:
                            print("Descripción incorrecta, vuelva a intentarlo")
                    new_service= Service(customer_found,work,description)
                    jobs.enqueue(new_service)
                    print("Servicio registrado correctamente.")
                    break
                else:
                    print("El cliente no existe")
            else:
                print("DPI incorrecto, vuelva a intentarlo")
while True:
    choice = input(f"---- Técnico Exprés ---\n"
                   f"1. Registrar usuario o servicio\n" 
                   # submenu de clientes y trabajadores
                   f"2. Consultar cola de servicios\n"
                   # submenu de consultar siguiente trabajo y cola entera
                   f"3. Ver calificaciones y reseñas\n"
                   # submenu de reseñas de plomeros, electricistas, etc...
                   # también opción de ver los trabajadores top 3 de cualquier tipo.
                   f"4. Eliminar usuario\n"
                   # submenu de clientes y trabajadores
                   f"5. Salir\n")

    match choice:
        case "1":
            while True:
                choice = input(f"REGISTRAR:\n"
                               f"1. Cliente\n"
                               f"2. Trabajador\n"
                               f"3. Servicio pedido\n"
                               f"4. Volver al menú principal\n")
                match choice:
                    case "1":
                        #Ya quedo lista la función de registrar cliente
                        registers_customers()
                    case "2":
                        #Ya quedo lista la función de registrar trabajador
                        registers_workers()
                    case "3":
                        #Ya quedo lista la función de registrar servicio.
                        register_services()
                    case "4":
                        break
                    case _:
                        print("Error, está opción no existe")
                # funciones afuera de menú para ejecutar según opción (3 funciones mínimo)
        case "2":
            while True:
                choice = input(f"1. Consultar el siguiente trabajo a concluir\n"
                               f"2. Consultar todos los trabajos pendientes\n")
                # funciones afuera de menú para ejecutar según opción (2 funciones mínimo, ya existe por lo menos el peek_left)
        case "3":
            while True:
                choice = input(f"\n")
                # esto no tengo tan claro cómo debe de ser el flujo...
        case "4":
            while True:
                choice = input(f"1. Eliminar cliente\n"
                               f"2. Eliminar trabajador\n")
        case "5":
            print("¡Hasta la próxima!")
            break
        case _:
            print("Opción inválida.")
