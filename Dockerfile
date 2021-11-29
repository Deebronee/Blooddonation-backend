#-alpine
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

RUN pip install mysqlclient
RUN pip install channels
RUN pip install djangorestframework
RUN pip install markdown
RUN pip install django-filter
RUN pip install channels_redis
RUN pip install djangochannelsrestframework

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000