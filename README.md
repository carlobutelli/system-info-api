# Python Flask - Demo Web Application
---------------------

This is a simple Python Flask web application. The app provides system information and a realtime monitoring screen with dials showing CPU, memory, IO and process information.

The app has been designed with cloud native demos & containers in mind, in order to provide a real working application for deployment, 
something more than "hello-world" but with the minimum of pre-reqs. 
It is not intended as a complete example of a fully functioning architecture or complex software design.

Typical uses would be deployment to Kubernetes, demos of Docker, CI/CD (build pipelines are provided), deployment to cloud, monitoring, auto-scaling

---

## ENVs
```bash
export FLASK_APP=api
export FLASK_DEBUG=1
export FLASK_ENV=Development
```
ENVs: Development, Testing, Production

## Run
------
```bash
python -m venv venv && . venv/bin/activate
pip install -r requirements/dev.txt
flask run -p 8080
```

With docker-compose
```bash
docker-compose up
```
With Dockerfile (runs PROD env)
```bash
docker build --tag sys-info-api .
docker run -d -p 8080:8080 --name sys-info-api sys-info-api
```
then the API will be available at [http://localhost:8080](http://localhost:8080)

### Remove all packages from PIP
To install all the GLOBAL packages installed in your local machine execute
```bash
pip freeze | xargs pip uninstall -y
```
To install all the required packages into a virtualenv then run
```bash
python -m venv venv && . venv/bin/activate
pip install -r requirements/base.txt 
pip freeze > requirements/base.txt
```
Now base.txt has all the required packages in alphabetical order

---

## Screenshot
-------------

![screen](https://user-images.githubusercontent.com/14982936/30533171-db17fccc-9c4f-11e7-8862-eb8c148fedea.png)

---

### Pre-reqs
---------------------

- Be using Linux, WSL or MacOS, with bash, make etc
- [Python 3.8+](https://www.python.org/downloads/) - for running locally, linting, running tests etc
- [Docker](https://docs.docker.com/get-docker/) - for running as a container, or image build and push

The app runs under Flask and listens on port 5000 by default, this can be changed with the `PORT` environmental variable.

---

## Tests
To run tests go to /api then execute
```bash
pytest -v
```

## Kubernetes
---------------------

The app can easily be deployed to Kubernetes using Helm

## Push to registry
```bash
docker build --tag sys-info-api .
docker tag sys-info-api cbutelli/sys-info-api:<version>
docker login -u cbutelli 
(insert the access token for user cbutelli)
docker push cbutelli/sys-info-api:<version>
```

