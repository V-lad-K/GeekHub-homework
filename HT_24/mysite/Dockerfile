FROM python:3.11-slim

COPY requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip install --upgrade pip
RUN pip install factory-boy
RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]