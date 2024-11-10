#!/bin/bash

# Порт по умолчанию
PORT=9999

# Обработка аргументов командной строки для порта
while getopts "p:" opt; do
    case $opt in
    p)
        PORT=$OPTARG # Установка порта из аргумента
        ;;
    \?)
        echo "Недопустимый параметр -$OPTARG" >&2
        exit 1
        ;;
    esac
done

# Запуск Python-скрипта сервера с указанным портом
python3 ./server/server.py -p $PORT
