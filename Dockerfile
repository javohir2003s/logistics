FROM python:3.8.10

WORKDIR /app

COPY . /app

RUN apt update
RUN apt install gettext -y

RUN pip install -r req.txt 

    

EXPOSE 8080

ENTRYPOINT ["sh", "entrypoint.sh"]
