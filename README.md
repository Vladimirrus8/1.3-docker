# Docker Assignment: Nginx и Django REST API

## Задание 1: Nginx с кастомной страницей

### Сборка и запуск

```bash
# Перейти в директорию с заданием 1
cd task1-nginx

# Собрать Docker образ
docker build -t my-nginx .

# Запустить контейнер
docker run -d -p 8080:80 --name my-nginx-container my-nginx

# Проверить работу
curl http://localhost:8080
# Или открыть в браузере: http://localhost:8080# 1.3-docker
