import json
import os
from fastapi import FastAPI
import psycopg2
import requests

def create_app():
    print("Hello world!")
    app = FastAPI()

    @app.post('/greetings')
    async def say_hello(input_data: dict):
        # try:
        #     connection = psycopg2.connect(
        #         user=os.getenv("db_user"),
        #         password=os.getenv("db_pass"),
        #         host=os.getenv("db_host"),
        #         port=os.getenv("db_port"), 
        #         database=os.getenv("db_name"))
        #     cursor = connection.cursor()
        #     cursor.execute("SELECT * FROM first_table")
        #     records = cursor.fetchall()
        
        # except Exception as error:
        #     print("Ошибка при работе с PostgreSQL", error)
        # try:
        #     r = requests.get('web_app:5000/')
        # except Exception as error:
        #     print("Ошибка при работе с сервисом", error)
        return {'hello_string': f'{input_data["name"]}, your env is {os.getenv("MY_ENV")}'}

    @app.get('/actuator/health')
    async def health():
        return "I am working!!!"

    return app
