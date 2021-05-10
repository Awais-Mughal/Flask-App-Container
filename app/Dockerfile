FROM python:3.8.5

WORKDIR /app

RUN pip3 install flask 

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3", "./app.py", "--host=0.0.0.0"]

#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
