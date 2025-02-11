FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "electronics_network.wsgi:application", "--bind", "0.0.0.0:8000"]
