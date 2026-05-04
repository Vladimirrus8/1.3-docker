FROM python:3.9-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV MY_ENV=netology_10_04
EXPOSE 5050
CMD ["python3", "-u", "main.py", "--host", "0.0.0.0", "--port", "5050"]