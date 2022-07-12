FROM python:3.9.9
RUN pip install pipenv
WORKDIR /app/
COPY Pipfile \ 
    Pipfile.lock \
    manage.py \ 
    /app/
RUN pipenv sync
COPY ./api /app/api
COPY ./alien_invasion_api /app/alien_invasion_api
EXPOSE 8000
CMD pipenv run python3 manage.py migrate \ 
    && pipenv run uvicorn --host=0.0.0.0 alien_invasion_api.asgi:application
