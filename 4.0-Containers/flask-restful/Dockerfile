FROM ubuntu
RUN apt-get update  && apt install -y git && apt install -y python3-pip
RUN pip install flask-restful
RUN git clone https://github.com/flask-restful/flask-restful.git
RUN python3 ./flask-restful/setup.py develop
COPY api.py ./flask/api.py
ENTRYPOINT ["python3","./flask/api.py"]
EXPOSE 5000

