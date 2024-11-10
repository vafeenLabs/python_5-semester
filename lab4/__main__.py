import requests  # Импортируем библиотеку для выполнения HTTP-запросов
import threading  # Импортируем модуль для работы с потоками
import timeit  # Импортируем модуль для измерения времени выполнения кода


def benchmark(func):  # Декоратор для измерения времени выполнения функции
    def wrapper(url):  # Вложенная функция, принимающая URL
        start_time = timeit.default_timer()  # Запоминаем время начала выполнения
        result = func(url)  # Вызываем оригинальную функцию и сохраняем результат
        end_time = timeit.default_timer()  # Запоминаем время окончания выполнения
        elapsed_time = (end_time - start_time) * 1000  # Вычисляем время в миллисекундах
        print(f"{url} -> {elapsed_time:.2f} ms".replace("\n", ""))  # Выводим URL и время выполнения
        return result  # Возвращаем результат оригинальной функции

    return wrapper  # Возвращаем обертку


@benchmark  # Применяем декоратор к функции download_page
def download_page(url):  # Функция для загрузки содержимого страницы по URL
    response = requests.get(url)  # Выполняем GET-запрос к указанному URL
    return response.text  # Возвращаем текст ответа


def download_pages_from_file(file_path):  # Функция для загрузки страниц из файла с URL
    with open(file_path, "r") as file:  # Открываем файл с URL в режиме чтения
        urls = file.readlines()  # Читаем все строки (URL) из файла

    threads = []  # Список для хранения потоков
    for url in urls:  # Проходим по каждому URL в списке
        thread = threading.Thread(target=download_page, args=(url,))  # Создаем новый поток для загрузки страницы
        threads.append(thread)  # Добавляем поток в список потоков
        thread.start()  # Запускаем поток

    for thread in threads:  # Ждем завершения всех потоков
        thread.join()  # Блокируем основной поток до завершения текущего потока


# Пример использования функции download_pages_from_file с файлом "urls.txt"
download_pages_from_file("urls.txt")
