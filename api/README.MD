[![SPHINX](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://choosealicense.com/licenses/mit/) 
[![Pytest-cov](https://img.shields.io/badge/coverage-100%25-green)
[![Beerware License](https://img.shields.io/badge/license-Beerware-yellow)](https://github.com/BlazejBielski/url_shortener/blob/master/LICENSE)


# URL Shortener


A Django URL shortener app is a web application that generates short, customized links that redirect to longer URLs. It uses Django and a database to store original and short URLs, and may incorporate third-party services for URL shortening. The app is useful for simplifying the sharing of links online.



## Demo

[URL Shortener Heroku](https://desolate-anchorage-51220.herokuapp.com/api/schema/swagger-ui/)



## Tech Stack

**Server:** Python, Django, Django Rest Framwework, Docker, Postgres


## Run Locally

Clone the project

```bash
  git clone git@github.com:BlazejBielski/url_shortener.git
```

Go to the project directory

```bash
  cd url_shortener
```

Set enviroment variables

```bash
cp ./envs/api.default.env ./envs/api.env
cp ./envs/postgres.default.env ./envs/postgres.env
# set variable values
```

Start docker containers

```bash
  docker compose up
```

Go to your client and type:
```bash
http://0.0.0.0:8000/api/schema/swagger-ui
```
## Environment Variables

To run this project, you will need to add the following environment variables to your ./envs/api.env file

<<<<<<< HEAD
`DJ_SECRET_KEY=` - Django secrest key for CSRF
=======
`DJ_SECRET_KEY=` - Django secret key for CSRF
>>>>>>> US-003_readme

`DJ_DEBUG=` - Production development mode 

`DJ_ALLOWED_HOSTS=` - Allowed host for Django

`LOGGING LEVEL=` - Python logging package levels 


`DJ_SU_NAME=`  - Default superuser name

`DJ_SU_EMAIL=` - Default superuser email

`DJ_SU_PASSWORD=` - Default superuser password


Also variables to your ./envs/postgres.env file

`POSTGRES_USER=` - Potstgres root user

`POSTGRES_PASSWORD=` - Postrges root password

`POSTGRES_DB=` - Database name

`POSTGRES_HOST=` - Database host - data docker service name

`POSTGRES_PORT=` - Database port



## Running Tests

To run tests, run the following command

```bash
  docker compose exec api pytest
```


## Coverage report

![Coverage report](https://raw.githubusercontent.com/BlazejBielski/url_shortener/master/screenshots/img.png)


## Authors

- [@BlazejBielski](https://github.com/BlazejBielski)


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/BlazejBielski?tab=repositories)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/blazej-bielski/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)


## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.
# API Service for URL Shortener
