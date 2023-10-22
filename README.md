### Учебный проект "пульт охраны банка"

Это внутренний репозиторий, вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать
код для вёрстки или посмотреть как реализованны запросы к БД.

### Как установить
Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
### Как запустить
```
python manage.py runserver 0.0.0.0:8000
```
### Параметры и как подключить БД
В папке скрипта создайте файл с названием .env и пропишите настроечные параметры приложения:
```
SECRET_KEY=<secret key>
DEBUG=<true/false>
ALLOWED_HOSTS=['localhost', 'www.example.com']
```
Настройка доступа к БД происходит согласно [URL schema](https://github.com/jazzband/dj-database-url#url-schema). Пример подключения PostgreSQL:
```
DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
```
