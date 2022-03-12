# Admin API
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

RUN python manage.py makemigrations

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000