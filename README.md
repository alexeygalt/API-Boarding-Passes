## Test API "Boarding Passes"

### Before starting work:

#### Environment setup:

For the project to work, you need to create **.env** in the root folder.
In it, you need to specify the necessary values of the variables:
* PORT = **port_number**

#### Installing dependencies:


In the root folder there is a file with dependencies pyproject.toml:

```shell
pip install poetry
```
```shell
poetry install
```
* Launch of the project


```shell
gunicorn -w 4 main:app
```
> **_NOTE_** ⚠: If your computer has an error when running gunicorn, you can directly run the python file main.py and it will spin up a WSGI server from python standard library

#### Docker

* Launch of the docker

```shell
docker compose up --build -d
```


The project implemented only two methods **GET** and **POST** on the root **path**

You can also get acquainted with the format of input / output data. To do this, use **first_step.http** in the root directory of the project
