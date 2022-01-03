FROM ubuntu
RUN apt-get update  && apt install -y git && apt install -y python3-pip
RUN pip install flask-restful
RUN git clone https://github.com/flask-restful/flask-restful.git
RUN python3 ./flask-restful/setup.py develop
RUN mkdir flask
WORKDIR /flask
VOLUME /flask

COPY api.py api.py
ENTRYPOINT ["python3","./api.py"]
EXPOSE 5000

