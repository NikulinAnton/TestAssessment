## Тестовое задание в Рексофт

### Задание:

#### Дано:
В карьере находятся 3 самосвала с бортовыми номерами "101", "102" и "К103".
"101" и "102" самосвалы модели "БЕЛАЗ", а "K103" - "Komatsu". У моделей "БЕЛАЗ" максимальная грузоподъемность 120 т руды, а у "Komatsu" - 110 т.
На текущий момент "101" самосвал везет 100 т руды, »102" - 125 т, "К103" - 120 т.

#### Задача:
Сделать приложение на Django, без авторизации. СУБД использовать sqlite.
Создать ORM-модели под описанные объекты. Учесть, что в систему в будущем могут добавляться новые самосвалы и модели самосвалов.
Создать страницу. Добавить на страницу выпадающий список (select) для выбора модели самосвала и кнопку "Применить". Список должен содержать пункт "Все", а также все модели из справочника моделей. Ниже разместить таблицу, отображающую справочные параметры самосвалов и текущее значение перегруза в % (выводить на сколько процентов превышена макс. грузоподъемность).

При нажатии на кнопку "Применить" страница должна перезагружаться, а список самосвалов в таблице фильтроваться по выбранной модели. Т.е. если выбрать "БелА3" в отчёте должны остаться только самосвалы модели "БелАз". Если выбран пункт "Все" - отображать все самосвалы.

*Полностью тестовое задание можно найти в файле test_assessment.pdf*

### Развернуть проект:

1. Перейти в директорию проекта `cd reksoft`
2. Создать виртуальное окружение `pipenv --python 3 shell`
2. Установить зависимости `pipenv install` (Если возникнут проблемы с lock файлом, то можно сгенерировать pipfile.lock файл ```pipenv lock``` после чего повторить 2 пункт)
3. Создать .env файл на основе .env.template и заполнить
5. Применить миграции `python3 manage.py migrate`
6. Загрузить начальные данные командами:
`python3 manage.py loaddata truck_models.json`
`python3 manage.py loaddata trucks.json`