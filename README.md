Тестовое задание на позицию “Backend-разработчик на языке Python
” в компанию **IT-Solutions**


## Установка

1. Клонирование репозитория 

```git clone https://github.com/Sh0ma28/django-solutions.git```

2. Переход в директорию django-solutions

```cd django-solutions```

3. Создание виртуального окружения

```python -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip install -r requirements.txt```

6. Запуск миграций

```python manage.py migrate```

7. Запуск приложения

```python manage.py runserver```

## Конечные точки API

- ```GET /api/cars/``` — получение списка автомобилей.
- ```GET /api/cars/<id>/``` — получение информации о конкретном автомобиле.
- ```POST /api/cars/``` — создание нового автомобиля.
- ```PUT /api/cars/<id>/``` — обновление информации о автомобиле.
- ```DELETE /api/cars/<id>/``` — удаление автомобиля.
- ```GET /api/cars/<id>/comments/``` — получение комментариев к автомобилю.
- ```POST /api/cars/<id>/comments/``` — добавление нового комментария к автомобилю.
