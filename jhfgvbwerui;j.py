class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
class Appointment:
    def __init__(self, client, service, date):
        self.client = client
        self.service = service
        self.date = date
class BarberShop:
    def __init__(self):
        self.clients = []
        self.appointments = []
    def add_client(self, name, phone):
        client = Client(name, phone)
        self.clients.append(client)
        print(f"Клиент {name} добавлен!")
    def book_appointment(self, client_name, service, date):
        client = self.find_client(client_name)
        if client:
            appointment = Appointment(client, service, date)
            self.appointments.append(appointment)
            print(f"Запись на услугу '{service}' для клиента {client_name} на {date} добавлена!")
        else:
            print("Клиент не найден!")
    def find_client(self, name):
        for client in self.clients:
            if client.name == name:
                return client
        return None
    def view_appointments(self):
        if not self.appointments:
            print("Нет записей.")
            return
        for appointment in self.appointments:
            print(f"Запись: {appointment.client.name}, Услуга: {appointment.service}, Дата: {appointment.date}")
def main():
    barber_shop = BarberShop()
    while True:
        print("\nМеню:")
        print("1. Добавить клиента")
        print("2. Записать клиента на услугу")
        print("3. Просмотреть записи")
        print("4. Выход")
        choice = input("Выберите опцию: ")
        if choice == '1':
            name = input("Введите имя клиента: ")
            phone = input("Введите номер телефона клиента: ")
            barber_shop.add_client(name, phone)
        elif choice == '2':
            client_name = input("Введите имя клиента: ")
            service = input("Введите услугу: ")
            date = input("Введите дату (например, 2023-10-30): ")
            barber_shop.book_appointment(client_name, service, date)
        elif choice == '3':
            barber_shop.view_appointments()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")
if __name__ == "__main__":
    main()