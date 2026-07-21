# подгружаем образ linux с python:3.9
FROM python:3.9
# создаем папку app
WORKDIR /app
# копируем содержимое проекта в папку app
COPY . .
# устанавливаем зависимости проекта
RUN pip install -r requirements.txt
# при старте контейнера запускаем команду pytest с генерацией отчета в папку allure-results
CMD ["pytest", "--alluredir", "allure-results"]