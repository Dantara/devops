# Devops course in Innopolis university
> Author: Nikita Aleshchenko, B18-SE-02

This repository contains a simple python web application that shows current time in Moscow (UTC+3 timezone)

### Prerequisites

To run an application you should install third version of python from official python website [link](https://www.python.org/downloads/).

## Installation

* Launch in terminal the following command to clone repository:

```sh
git clone https://github.com/dantara/devops
```

* and then install all required libraries:
```sh
cd app_python
pip3 install -r requirements.txt
```

## Running an application

To run the app do the following in the terminal
1. Change application directory with `cd app_python`
3. Start the server with `python3 app.py`
4. Open the [suggested link in the browser](http://127.0.0.1:5000/) to see the app

## Docker

### Building docker image

1. Install docker according [to this instructions](https://docs.docker.com/engine/install/)
2. Go to the app folder with `cd app_python`
3. Build the image with `docker build -t dantara/devops-python-app .`

### Using existing image

1. Check the [existing image on Docker Hub](https://hub.docker.com/r/dantara/devops-python-app)
2. Fetch it and run with `docker run --rm -it -p 5000:5000 dantara/devops-python-app`

## Tests

First of all, to run tests you need to install all development requirements:
```sh
pip3 install -r dev-requirements.txt
```

And then simply type:
```sh
pytest
```

## Contributing

1. Fork repository (<https://github.com/dantara/devops/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -m 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## References 

This Markdown README.md template is heavily inspired by
[the following repository](https://github.com/dbader/readme-template/blob/master/README.md)
