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
    def __init__(self, name, dpi, email, rating, address, jobs_finished, rating_sum):
        super().__init__(name,dpi,email, rating)
        self.address = address
        self.jobs_finished = jobs_finished
        self.rating_sum = rating_sum

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @property
    def jobs_finished(self):
        return self._jobs_finished

    @jobs_finished.setter
    def jobs_finished(self, jobs_finished):
        self._jobs_finished = jobs_finished

    @property
    def rating_sum(self):
        return self._rating_sum

    @rating_sum.setter
    def rating_sum(self, rating_sum):
        self._rating_sum = rating_sum

    def show_information(self):
        print("Nombre:", self.name)
        print("DPI:", self.dpi)
        print("Correo:", self.email)
        print("Dirección:", self.address)

class Worker(Person):
    def __init__(self, name, dpi, email, rating, job_type, reviews, status, rating_sum):
        super().__init__(name,dpi,email, rating)
        self.job_type = job_type
        self.reviews = reviews
        self.status = status
        self.rating_sum = rating_sum

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

    @property
    def rating_sum(self):
        return self._rating_sum

    @rating_sum.setter
    def rating_sum(self, rating_sum):
        self._rating_sum = rating_sum

    def show_information(self):
        print("Nombre: ", self.name)
        print("DPI: ", self.dpi)
        print("Correo: ", self.email)
        print("Tipo de trabajo: ", self.job_type)
        print("Reseñas: ", self.reviews)
        print("Estado: ", self.status)

class Service:
    def __init__(self, customer,worker,job_type, description):
        self.customer = customer
        self.worker = worker
        self.job_type = job_type
        self.description = description

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        self._customer=customer

    @property
    def worker(self):
        return self._worker

    @worker.setter
    def worker(self, worker):
        self._worker = worker

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

    def show_information(self):
        return f"Trabajo para: {self.customer.name}, Tipo de trabajo: {self.job_type}, Descripción: {self.description}"


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
        address=input("Ingrese su dirección: ")
        if len(address)>=5:
            break
        else:
            print("Error dirección incorrecta, vuela a intentarlo")
    new_customer = Customer(name,dpi,email,-1,address, 0, 0)
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

    new_worker=Worker(name,dpi,email,-1,work,[], "Disponible", 0)
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
            customer_found=None
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
                                    counter=1
                                    isAvailable=False
                                    worker_found=None
                                    available_workers = []
                                    for w in workers:
                                        if w.job_type=="Plomería" and w.status=="Disponible":
                                            print(f"{counter} -- Nombre: {w.name}")
                                            available_workers.append(w)
                                            counter += 1
                                            isAvailable = True
                                    if isAvailable==False:
                                        print("No hay plomeros disponibles.")
                                        return
                                    else:
                                        while True:
                                            choice=int(input("Seleccione un trabajador: "))
                                            if choice>=1 and choice<=len(available_workers):
                                                worker_found = available_workers[choice-1]
                                                worker_found.status="Ocupado"
                                                break
                                            else:
                                                print("Opción incorrecta, vuelva a intentarlo.")
                            case 2:
                                if electricians.size()==0:
                                    print("No hay electricistas registrados.")
                                    return
                                else:
                                    work="Electricidad"
                                    counter = 1
                                    isAvailable = False
                                    worker_found = None
                                    available_workers = []
                                    for w in workers:
                                        if w.job_type == "Electricidad" and w.status == "Disponible":
                                            print(f"{counter} -- Nombre: {w.name}")
                                            available_workers.append(w)
                                            counter += 1
                                            isAvailable = True
                                    if isAvailable == False:
                                        print("No hay electricistas disponibles.")
                                        return
                                    else:
                                        while True:
                                            choice = int(input("Seleccione un trabajador: "))
                                            if choice >= 1 and choice <= len(available_workers):
                                                worker_found = available_workers[choice - 1]
                                                worker_found.status = "Ocupado"
                                                break
                                            else:
                                                print("Opción incorrecta, vuelva a intentarlo.")
                            case 3:
                                if builders.size()==0:
                                    print("No hay constructores registrados.")
                                    return
                                else:
                                    work="Construcción"
                                    counter = 1
                                    isAvailable = False
                                    worker_found = None
                                    available_workers = []
                                    for w in workers:
                                        if w.job_type == "Construcción" and w.status == "Disponible":
                                            print(f"{counter} -- Nombre: {w.name}")
                                            available_workers.append(w)
                                            counter += 1
                                            isAvailable = True
                                    if isAvailable == False:
                                        print("No hay constructores disponibles.")
                                        return
                                    else:
                                        while True:
                                            choice = int(input("Seleccione un trabajador: "))
                                            if choice >= 1 and choice <= len(available_workers):
                                                worker_found = available_workers[choice - 1]
                                                worker_found.status = "Ocupado"
                                                break
                                            else:
                                                print("Opción incorrecta, vuelva a intentarlo.")
                            case 4:
                                if it_professionals.size()==0:
                                    print("No hay técnicos informáticos registrados.")
                                    return
                                else:
                                    work="Técnicos informáticos"
                                    counter = 1
                                    isAvailable = False
                                    worker_found = None
                                    available_workers = []
                                    for w in workers:
                                        if w.job_type == "Técnicos informáticos" and w.status == "Disponible":
                                            print(f"{counter} -- Nombre: {w.name}")
                                            available_workers.append(w)
                                            counter += 1
                                            isAvailable = True
                                    if isAvailable == False:
                                        print("No hay técnicos informáticos disponibles.")
                                        return
                                    else:
                                        while True:
                                            choice = int(input("Seleccione un trabajador: "))
                                            if choice >= 1 and choice <= len(available_workers):
                                                worker_found = available_workers[choice - 1]
                                                worker_found.status = "Ocupado"
                                                break
                                            else:
                                                print("Opción incorrecta, vuelva a intentarlo.")
                            case 5:
                                print("Volviendo al menú principal...")
                                return
                            case _:
                                print("Opción incorrecta, vuelva a intentarlo")
                                continue # este continue forza al ciclo a reiniciar
                        while True:
                            description=input("Describa su problema: ")
                            if len(description)>=5:
                                break
                            else:
                                print("Descripción incorrecta, vuelva a intentarlo")
                        new_service= Service(customer_found,worker_found,work,description)
                        jobs.enqueue(new_service)
                        print("Servicio registrado correctamente.")
                        return
                else:
                    print("El cliente no existe")
            else:
                print("DPI incorrecto, vuelva a intentarlo")

def show_next_job():
    if jobs.size() == 0:
        print("No hay trabajos pendientes.")
    else:
        next_service = jobs.peek_left()
        print(next_service.show_information())

def show_all_jobs():
    if jobs.size() == 0:
        print("No hay trabajos pendientes.")
    else:
        for job in jobs.items:
            print("------------------------------\n")
            print(job.show_information())
            print("------------------------------\n")

def finish_job():
    if jobs.size() == 0:
        print("No hay trabajos pendientes.")
    else:
        counter = 1
        for job in jobs.items:
            print("------------------------------\n")
            print(f"Trabajo número {counter}: ")
            print(job.show_information())
            print("------------------------------\n")
            counter += 1
        choice = int(input("Selecciona el trabajo concluido: "))
        if choice > jobs.size() or choice < 1:
            print("Opción invalida.")
            return
        else:
            worker_dpi = jobs.items[choice-1].worker.dpi
            customer_dpi = jobs.items[choice-1].customer.dpi
            for worker in workers:
                if worker.dpi == worker_dpi:
                    review = input("Deja una reseña de por lo menos una palabra: ")
                    worker.reviews.append(review)
                    if worker.rating == -1:
                        worker.rating = 0
                    job_rating = int(input("¿Qué calificación se le da al trabajo del trabajador? (0 - 5)"))
                    worker.rating_sum += job_rating
                    worker.rating = worker.rating_sum / len(worker.reviews)
                    worker.status = "Disponible"
                    break
            for customer in customers:
                if customer.dpi == customer_dpi:
                    if customer.rating == -1:
                        customer.rating = 0
                    customer.jobs_finished += 1
                    customer.rating_sum += int(input("¿Qué calificación se le da al cliente?"))
                    customer.rating = customer.rating_sum / customer.jobs_finished
                    break
            del jobs.items[choice - 1]

def show_customer_ratings():
    if len(customers) == 0:
        print("No hay clientes registrados.")
    else:
        for customer in customers:
            print("------------------------------\n")
            print(f"Cliente: {customer.name}\n")
            if customer.rating == -1:
                print("Sin calificación")
            else:
                print(f"Calificación: {customer.rating}\n")
            print(f"------------------------------\n")

def show_worker_ratings():
    if len(workers) == 0:
        print("No hay trabajadores registrados.")
    else:
        for worker in workers:
            print(f"Trabajador: {worker.name}\n")
            print(f"Servicio: {worker.job_type}\n")
            if worker.rating == -1:
                pass
                print("Sin calificación")
            else:
                print(f"Calificación: {worker.rating}")
            print("\tReseñas")
            if len(worker.reviews) ==0:
                print("No hay reseñas")
            else:
                for review in worker.reviews:
                    print(" - ", review)
            print("------------------------------")

def delete_customer():
    while True:
        dpi = input(f"Ingresa el DPI del cliente a eliminar: \n"
                    f"Ingresa 0 para salir.\n")
        if dpi == "0":
            return
        counter = 0
        found = False
        for customer in customers:
            if customer.dpi == dpi:
                found = True
                del customers[counter]
                print("Cliente eliminado correctamente.")
                return
            counter += 1
        if found == False:
            print("DPI no existe.")

def delete_worker():
    while True:
        dpi = input(f"Ingresa el DPI del trabajador a eliminar: \n"
                    f"Ingresa 0 para salir.\n")
        if dpi == "0":
            return
        counter = 0
        found = False
        for worker in workers:
            if worker.dpi == dpi:
                found = True
                counter_2 = 0
                for plumber in plumbers.items:
                    if dpi == plumber.dpi:
                        del plumbers.items[counter_2]
                        break
                    counter_2 += 1
                counter_2 = 0
                for electrician in electricians.items:
                    if dpi == electrician.dpi:
                        del electricians.items[counter_2]
                        break
                    counter_2 += 1
                counter_2 = 0
                for builder in builders.items:
                    if dpi == builder.dpi:
                        del builders.items[counter_2]
                        break
                    counter_2 += 1
                counter_2 = 0
                for it_professional in it_professionals.items:
                    if dpi == it_professional.dpi:
                        del it_professionals.items[counter_2]
                        break
                    counter_2 += 1
                del workers[counter]
                print("Trabajador eliminado correctamente.")
                return
            counter += 1
        if found == False:
            print("DPI no existe.")


while True:
    choice = input(f"---- Técnico Exprés ---\n"
                   f"1. Registrar usuario o servicio\n" 
                   f"2. Consultar cola de servicios\n"
                   f"3. Ver calificaciones y reseñas\n"
                   f"4. Eliminar usuario\n"
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
                        registers_customers()
                    case "2":
                        registers_workers()
                    case "3":
                        register_services()
                    case "4":
                        break
                    case _:
                        print("Error, está opción no existe")
        case "2":
            while True:
                choice = input(f"1. Consultar el siguiente trabajo a concluir\n"
                               f"2. Consultar todos los trabajos pendientes\n"
                               f"3. Concluir trabajo\n"
                               f"4. Regresar\n")
                match choice:
                    case "1":
                        show_next_job()
                    case "2":
                        show_all_jobs()
                    case "3":
                        finish_job()
                    case "4":
                        break
                    case _:
                        print("Opción inválida.")

        case "3":
            while True:
                choice = input(f"CALIFICACIONES Y RESEÑAS\n"
                               f"1. Ver calificaciones de clientes\n"
                               f"2. Ver calificaciones y reseñas de trabajadores\n"
                               f"3. Volver al menú principal\n")
                match choice:
                    case "1":
                        show_customer_ratings()
                    case "2":
                        show_worker_ratings()
                    case "3":
                        break
                    case _:
                        print("Opción incorrecta vuelva a intentarlo")
        case "4":
            while True:
                choice = input(f"1. Eliminar cliente\n"
                               f"2. Eliminar trabajador\n"
                               f"3. Volver al menú principal\n")
                match choice:
                    case "1":
                        delete_customer()
                    case "2":
                        delete_worker()
                    case "3":
                        break
                    case _:
                        print("Opción inválida.")
        case "5":
            print("¡Hasta la próxima!")
            break
        case _:
            print("Opción inválida.")
            #