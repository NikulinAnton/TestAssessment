## Тестовое задание

### Задание
Ознакомиться с тестовым заданием можно в файле test_assessment.pdf

### Развернуть проект:

1. Перейти в директорию проекта `cd reksoft`
2. Создать виртуальное окружение `pipenv --python 3 shell`
2. Установить зависимости `pipenv install` (Если возникнут проблемы с lock файлом, то можно сгенерировать pipfile.lock файл ```pipenv lock``` после чего повторить 2 пункт)
3. Создать .env файл на основе .env.template и заполнить
5. Применить миграции `python3 manage.py migrate`
6. Загрузить начальные данные командами:  
`python3 manage.py loaddata truck_models.json`  
`python3 manage.py loaddata trucks.json`


### P.S.:

Начальные данные можно подгружать и через миграции:
`python manage.py makemigrations --empty core`
и с помощью `migrations.RunPython(create_truck_and_models),` загрузить необходимые данные.

Добавлять новые модели и самосвалы можно с помощью админки, либо если необходимо могу добавить вьюхи для CRUD операций
