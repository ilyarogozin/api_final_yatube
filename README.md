# API for Yatube social network
## api_yatube - это учебное API для учебного проекта - социальной сети "Yatube"
### Проект реализован на DRF
# Как запустить проект:
- Клонировать репозиторий и перейти в него:
>git clone git@github.com:ilyarogozin/api_final_yatube.git

>cd kittygram

- Cоздать и активировать виртуальное окружение:
>python3 -m venv env

>source env/bin/activate

- Установить зависимости из файла requirements.txt:
>python3 -m pip install --upgrade pip

>pip install -r requirements.txt

- Выполнить миграции:
>python3 manage.py migrate

- Запустить проект:
>python3 manage.py runserver

## Примеры запросов к API можно посмотреть по запросу:
http://127.0.0.1:8000/redoc/
