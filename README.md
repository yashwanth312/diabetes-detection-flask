# Diabetes-Detection-Flask
In this project I've used Flask framework by python to provide a UI for clients to interact with my AI based Diabetes Detection model
# Creation of ML model
The complete code and the datasets are avaiable above in diabetes-model.ipnyb and diabetes.csv files respectively. 
I trained my model to 78% efficiency using an ML arcitecture which contains 1 input layer with 8 neurons , 3 deep layers and an output layer. The actiavtion functions I've usedare RELU and SIGMOID for the deep layers and output layer respectively. "Adam" optimizer is used to guide the weights towards increase in efficiency. Finally the metrics named "accuracy" of the model is given as output.

# Deploying the Model in Docker container
For my model to be tested in a completely different enviornment (docker container - centos) , the container should contain KERAS , TENSORFLOW , PYTHON3 and FLASK preinstalled so that my app can run successfully without any environment based error.
The complete code for the flask framework is provided above. 
I've also created a container image for this so that the flask services run as soon as the container starts running. I've pushed this container image to centralised repository Doceker-Hub. You can pull the image using the command       "docker pull yashwanth3/flask-keras:v2"

# Deploying the services on top Kubernetes 
I further went on to deploy my application on local Kubernetes cluster so as to ensure the availability and uptime of services to my clients
