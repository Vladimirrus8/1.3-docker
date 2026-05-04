#!/bin/bash

# Применяем миграции
python manage.py migrate

# Создаем суперпользователя, если заданы переменные окружения
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL 2>/dev/null || true
fi

# Собираем статику
python manage.py collectstatic --noinput

# Запускаем сервер
python manage.py runserver 0.0.0.0:8000