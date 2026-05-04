FROM nginx:alpine

# Удаляем стандартную страницу приветствия
RUN rm /usr/share/nginx/html/index.html

# Копируем нашу страницу
COPY index.html /usr/share/nginx/html/

# Открываем порт 80
EXPOSE 80

# Запускаем nginx
CMD ["nginx", "-g", "daemon off;"]