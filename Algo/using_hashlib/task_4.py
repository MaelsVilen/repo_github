"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносит ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib as hl
from uuid import uuid4


cache = {}


def web_caching(url):
    salt = uuid4().hex
    if url not in cache.keys():
        cache.update({url: hl.sha256(salt.encode() + url.encode()).hexdigest()})
        return cache
    else:
        return cache


web_caching('https://geekbrains.ru/')
web_caching('https://play.google.com/')
web_caching('https://mail.google.com/')
print(web_caching('https://play.google.com/'))
