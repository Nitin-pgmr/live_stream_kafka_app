### Streaming Static and Live Data API

#### Introduction
The app is used to automate the machine learning pipeline by using the MiniBatch Kmeans algorithm on the iris dataset used to predict three species of flowers setosa(0),versicolor(1),virginica (2)

#### Functionality

The app uses Swagger API to provide a front end that services users input, csv file format input and live streaming API, to produce the live predictions


#### FILE STRUCTURE
|src -- contains the main app to be run<br/>
&nbsp;app  -- main application file<br/>
&nbsp; &nbsp;|template --default templates<br/>
&nbsp; &nbsp;&nbsp; &nbsp;|index.html --welcome page <br/>
|Dockerfile  -- spin up a docker<br/>
|Finalized_model --pickle file <br/>
|requirements.txt <br/>
|testinput_file.csv --sample inputs fed to the app during dev <br/>

#### Procedure
start zookeeper <br/>
start kafka <br/>

pip install -r requirements.txt <br/>
run producer on a topic <br/>
python app.py <br/>
access on the browser<br/>

#### Accessing live stream input request
Live stream is based on generator and will not be rendered on swagger however can be accessed as 

For Example: http://127.0.0.1:5000/predictlive?topic_name=jts on the browser directly

