#!/usr/bin/env python3

from typing import List, Tuple, Callable, Generator, TypeVar

# Определяем generic типы
T = TypeVar('T')
U = TypeVar('U')

# Определяем тип кортежа как неизменяемый список
IList = Tuple[T, ...]
IListT = Tuple[T, ...]
IListU = Tuple[U, ...]

# Определяем тип Predicate как функцию, принимающую элемент типа T и возвращающую bool
Predicate = Callable[[T], bool]

# Функция map_gen применяет функцию к каждому элементу списка, используя генератор
def map_gen(function: Callable[[T], U], collection: List[T]) -> Generator[U, None, None]:
    return (function(item) for item in collection)

# Функция filter_gen фильтрует элементы списка, используя предикат и генератор
def filter_gen(predicate: Predicate, collection: List[T]) -> Generator[T, None, None]:
    return (item for item in collection if predicate(item))

# Функция map_lgen применяет функцию к каждому элементу списка, используя list comprehension
def map_lgen(function: Callable[[T], U], collection: List[T]) -> List[U]:
    return [function(item) for item in collection]

# Функция filter_lgen фильтрует элементы списка, используя предикат и list comprehension
def filter_lgen(predicate: Predicate, collection: List[T]) -> List[T]:
    return [item for item in collection if predicate(item)]

# Функция head возвращает первый элемент кортежа
def head(collection: IList) -> T:
    return collection[0]

# Функция tail возвращает кортеж без первого элемента
def tail(collection: IList) -> IList:
    return collection[1:]

# Функция is_empty проверяет, является ли кортеж пустым
def is_empty(collection: IList) -> bool:
    return len(collection) == 0

# Функция non_empty проверяет, является ли кортеж непустым
def non_empty(collection: IList) -> bool:
    return len(collection) > 0

# Функция map_t применяет функцию к каждому элементу кортежа, возвращая новый кортеж
def map_t(function: Callable[[T], U], collection: IListT) -> IListU:
    return tuple(function(item) for item in collection)

# Функция filter_t фильтрует элементы кортежа, используя предикат
def filter_t(predicate: Predicate, collection: IListT) -> IListT:
    return tuple(item for item in collection if predicate(item))