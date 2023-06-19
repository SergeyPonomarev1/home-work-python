# 1
#mport socket

#OST = '127.0.0.1'  # Локальный адрес
#ORT = 65432        # Выбранный порт

#ith socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#   s.bind((HOST, PORT))  # Привязываем сокет к адресу и порту
#   s.listen()            # Слушаем входящие соединения
#   print(f"Сервер запущен на {HOST}:{PORT}")
#   while True:
#       conn, addr = s.accept()  # Принимаем входящее соединение
#       with conn:
#           print(f"Подключился клиент {addr}")
#           while True:
#               data = conn.recv(1024)  # Получаем данные от клиента
#               if not data:
#                   break
#               print(f"Клиент {addr} отправил сообщение: {data.decode()}")
#               conn.sendall(data)      # Отправляем данные обратно клиенту

#Пример клиентской части:

#mport socket

#OST = '127.0.0.1'  # Адрес сервера
#ORT = 65432        # Порт сервера

#ith socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#   s.connect((HOST, PORT))  # Устанавливаем соединение с сервером
#   while True:
#       message = input("Введите сообщение: ")
#       s.sendall(message.encode())  # Отправляем сообщение на сервер
#       data = s.recv(1024)          # Получаем ответ от сервера
#       print(f"Сервер отправил ответ: {data.decode()}")


# 2

#Сервер:

import socket
import threading

class WeatherServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)

    def start_server(self):
        print("Server is listening on {host}:{port}".format(host=self.host, port=self.port))
        while True:
            # Принимаем входящее подключение и запускаем новый поток для этого клиента
            client_socket, address = self.socket.accept()
            client_thread = threading.Thread(target=self.handle_client_connection, args=(client_socket, address))
            client_thread.start()

    # Обработка запроса клиента
    def handle_client_connection(self, client_socket, address):
        print("Accepted connection from {address}".format(address=address))

        # Получаем запрос от клиента
        request = client_socket.recv(1024).decode('utf-8').strip()

        # Извлекаем из запроса страну и город
        country, city = request.split(',')

        # Отправляем клиенту погодные данные
        weather_data = self.get_weather_data(country, city)
        client_socket.sendall(weather_data.encode('utf-8'))

        client_socket.close()
        print("Connection from {address} closed.".format(address=address))

    # Чтение данных о погоде из файла
    def get_weather_data(self, country, city):
        with open('weather_data.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith("#"):
                    continue
                if line.startswith(country):
                    _, city_name, *weather_data = line.split(',')
                    if city_name == city:
                        return ','.join(weather_data)

if __name__ == '__main__':
    server = WeatherServer('127.0.0.1', 8000)
    server.start_server()


#Клиент:

import socket

class WeatherClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def get_weather(self, country, city):
        # Отправляем запрос на сервер
        request = "{country},{city}".format(country=country, city=city)
        self.socket.sendall(request.encode('utf-8'))

        # Получаем ответ от сервера
        response = self.socket.recv(1024).decode('utf-8').strip()
        return response

if __name__ == '__main__':
    client = WeatherClient('127.0.0.1', 8000)
    client.connect()

    country = input("Enter country name: ")
    city = input("Enter city name: ")
    weather_data = client.get_weather(country, city)

    print("Weather for {city}, {country}: {weather_data}".format(city=city, country=country, weather_data=weather_data))

# 3
import requests

# Получаем ключ API для работы с погодным сервисом
api_key = 'your_api_key_here'

# Функция для получения погодных данных на основе координат
def get_weather_data(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric'
    response = requests.get(url).json()
    # Проверяем, что запрос успешен
    if response['cod'] == 200:
        # Формируем строку с данными о погоде
        weather = f"Погода в {response['name']}: {response['main']['temp']}°C, {response['weather'][0]['description']}"
        return weather
    else:
        # Если запрос неудачный, возвращаем сообщение об ошибке
        return 'Не удалось получить данные о погоде'

# Пример использования функции
print(get_weather_data(55.755826, 37.6172999)) # Погода в Moscow: 19.12°C, clear sky (ясно)