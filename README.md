# Тестовое задание
Выполнено (Основная задача):
- Модель Items (name, description, price)
- API с методами:
    -GET /buy/{item_id} Формируется Stripe session и в ответ отдается session id
    -GET /item/{item_id} Формируется простая HTML страница, на которой есть кнопка, при нажатии которой отправляется запрос на предыдущую страницу и получив session id производится переадресация на платежную форму
- Создан репозиторий GIT и описан этот файл Readme.md
- Опубликовано решение для быстрого тестирование

Выполнено (бонусные задачи):
- Используются Environment variables
- Все созданные модели полдключены к Django Admin панели
- Проект запущен на сервисе pythonanywhere.com
- Создана модель Order в которой можно создать заказ
- Создана модель ItemOrder в которой каждому заказу можно прикрепить несколько Item
- Сформированы endpoints для модели Order:
    -GET /orders/{item_id} Отобразит заказы с конечной суммой и кнопкой для получения платежной формы
    -GET /orders/buy/{item_id} Подобно основной задаче формирует id платежной сессии
- Добавлена модель Discount
- Добавлена модель Tax

Соответсвующие поля модели Order могут быть связаны с полями моделей Discount и Tax, в следствии к заказу могут применяться как налоги, так и скидки, что будет отображено в конечной платежной форме.

# Установка
Python не ниже версии 3.7. Все операции описаны для ОС Windows с установленным GitBash. Необходимо выполнять от имени администратора.

1. Клонировать репозиторий
```sh
git clone git@github.com:Promolife/task_stripe.git
```
2. Зайти в директорию проекта и создать виртуальное окружение
```sh
cd task_stripe
python -m venv venv
```
3. Активировать виртуальное окружение
```sh
source venv/Scripts/activate
```
4. Обновить pip и установить зависимости
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
5. Сформировать новый и записать ключ Django создав файл .env, так же в этом файле нужно хранить ключи Stripe. Примером может служить файл env.example
```sh
 python manage.py shell -c 'from django.core.management import utils; print("DJANGO_KEY=" + utils.get_random_secret_key())' >> .env
```
6. Создать миграции
```sh
python manage.py makemigrations mainapp
python manage.py migrate
```
7. Создать суперпользователя
```sh
python manage.py createsuperuser
```
8. Запустить сервер
```sh
python manage.py runserver
```