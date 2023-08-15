# Проект Yatube API
#### API социальной сети
### Описание
API для соцсети YaTube позволяет работать в ней и проводить различные творческие эксперименты.\
Поддерживаются методы GET, POST, PUT, PATCH, DEL для постов и комментариев.\
Для сообществ - только метод GET, для подписок - GET, POST.\
Для аутентификации используются JWT-токены + библиотека Djoser.
### Инструменты:
Python 3.11.14\
Django 3.2\
Django Rest Framework 3.12.4\
Djoser 2.2.0
### Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:\
`git clone git@github.com:alextriano/api_final_yatube.git`\
`cd api_yatube`

Cоздать и активировать виртуальное окружение:\
`python -m venv venv`\
`source venv/Scripts/activate`

Установить pip и зависимости:\
`python -m pip install --upgrade pip`\
`pip install -r requirements.txt`

Применить миграции и запустить проект:\
`python manage.py migrate`\
`python manage.py runserver`