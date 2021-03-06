FROM confluentinc/cp-zookeeper
FROM confluentinc/cp-kafka

FROM continuumio/anaconda3:4.4.0
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install -r requirements.txt
WORKDIR /usr/app/src
CMD python app.py