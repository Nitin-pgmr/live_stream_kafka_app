# import statements
from flask import Flask, request, Response, render_template
import pandas as pd
import pickle
from flasgger import Swagger
from pykafka import KafkaClient
import json
import warnings

# ignore warnings
warnings.filterwarnings("ignore")

# encapsulate the app with Swagger API
app = Flask(__name__)
Swagger(app)

# unpickle the trained Minibatch kmeans file
pickle_in = open('/finalized_model', 'rb')
classifier = pickle.load(pickle_in)


# specify the default welcome page
@app.route("/")
def index():
    return (render_template('index.html'))


# specify the client port - usually in config
def get_kafka_client():
    return KafkaClient(hosts='192.168.99.100:9092')


@app.route('/predict')
def predict_flower():
    """Predicting the flower type
        This is using docstrings for specifications.
        ---
        parameters:
          - name: sepal_length
            in: query
            type: number
            required: true
          - name: sepal_width
            in: query
            type: number
            required: true
          - name: petal_length
            in: query
            type: number
            required: true
          - name: petal_width
            in: query
            type: number
            required: true
        responses:
            200:
                description: The output values

        """
    sepal_length = request.args.get('sepal_length')
    sepal_width = request.args.get('sepal_width')
    petal_length = request.args.get('petal_length')
    petal_width = request.args.get('petal_width')
    prediction = classifier.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return "The flower predicted is " + str(prediction)


@app.route('/predictlive')
def predict_flower_live():
    """Predicting the flower type live stream
        This is using docstrings for specifications.
        ---
        parameters:
          - name: topic_name
            in: query
            type: string
            required: true
        responses:
            200:
                description: The output values

        """
    # obtain the topic name
    topicname = request.args.get('topic_name')
    client = get_kafka_client()

    #Continuously running Function to run aynchronous message using generators
    def events():
        for i in client.topics[topicname].get_simple_consumer():
            val = json.loads(i.value.decode())
            df = pd.DataFrame([val])
            prediction = classifier.predict(df)
            yield 'data:{0},prediction:{1}\n\n'.format(i.value.decode(), prediction)

    return (Response(events(), mimetype="text/event-stream"))


@app.route('/predict_file', methods=["POST"])
def predict_flower_file():
    """Predicting the flower type for a file of records
        This is using docstrings for specifications.
        ---
        parameters:
          - name: file
            in: formData
            type: file
            required: true

        responses:
            200:
                description: The output values

        """
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return str(list(prediction))


if __name__ == '__main__':
    app.run()
