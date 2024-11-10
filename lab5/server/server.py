import http.server
import socketserver
import os
import sys
import threading

PORT = 9999  # Порт по умолчанию
HOST = "localhost"  # Хост, на котором будет запущен сервер
server_thread = None  # Переменная для хранения потока сервера
server = None  # Переменная для хранения экземпляра сервера


# Класс для обработки HTTP-запросов с поддержкой Content-Type
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def guess_type(self, path):
        base, ext = os.path.splitext(path)  # Получаем базовое имя и расширение файла
        print(f"ext = {ext}")  # Выводим расширение файла для отладки
        if ext in [".html", ".htm"]:
            return "text/html"  # Возвращаем тип для HTML файлов
        elif ext in [".png"]:
            return "image/png"  # Возвращаем тип для PNG изображений
        elif ext in [".jpeg", ".jpg"]:
            return "image/jpeg"  # Возвращаем тип для JPEG изображений
        elif ext in [".bmp"]:
            return "image/bmp"  # Возвращаем тип для BMP изображений
        elif ext in [".js"]:
            return "text/javascript"  # Возвращаем тип для JavaScript файлов
        elif ext in [".css"]:
            return "text/css"  # Возвращаем тип для CSS файлов
        else:
            return "application/octet-stream"  # Для неизвестных типов возвращаем бинарный поток


# Функция для запуска сервера
def start_server():
    global server
    server = socketserver.TCPServer((HOST, PORT), MyHandler)  # Создаем сервер с обработчиком MyHandler
    print(f"Serving at http://{HOST}:{PORT}")  # Выводим сообщение о запуске сервера
    server.serve_forever()  # Запускаем сервер в бесконечном цикле


# Функция для остановки сервера
def stop_server():
    global server
    if server:
        server.shutdown()  # Останавливаем сервер
        print("Server stopped.")  # Выводим сообщение о том, что сервер остановлен


# Проверка аргументов командной строки для порта
if len(sys.argv) > 1:
    if sys.argv[1] == "-p" and len(sys.argv) > 2:
        PORT = int(sys.argv[2])  # Если указан порт, устанавливаем его значение

os.chdir("webapp")  # Переход в директорию с контентом (webapp)

# Основной цикл меню
while True:
    # Проверка состояния сервера (работает или спит)
    server_status = (
        "Working" if (server_thread and server_thread.is_alive()) else "Sleeping"
    )

    print(f"\nServer state: {server_status}")  # Выводим текущее состояние сервера
    print("Menu:")
    print("1 - Start Server")  # Опция для запуска сервера
    print("0 - Stop Server")   # Опция для остановки сервера
    print("q - Quit Application")  # Опция для выхода из приложения

    choice = input("Enter your choice: ")  # Запрашиваем выбор пользователя

    if choice == "1":
        if server_thread is None or not server_thread.is_alive():
            server_thread = threading.Thread(target=start_server)  # Создаем новый поток для сервера
            server_thread.start()  # Запускаем поток сервера
        else:
            print("Server is already working.")  # Сообщение, если сервер уже запущен

    elif choice == "0":
        stop_server()  # Остановка сервера

    elif choice == "q":
        if server:
            stop_server()  # Остановить сервер перед выходом из приложения
        print("Exit.")  # Сообщение о выходе из приложения
        break

    else:
        print("Incorrect choice. Repeate, please.")  # Сообщение об ошибочном выборе