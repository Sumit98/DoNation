DoNation is a platform meant to help NGOs during an emergency situation. The NGOs can ask for donations, resources or volunteers, and users can browse the needs that various NGOs have.

Objective: Safe and coherent collection of aid.

How: The application displays verified and validated NGOs for the collection and distribution of resources.


## Contributing

If you want to make any change to this repository, please **make a fork first**
If you would like to suggest new functionality, open an Issue and mark it as a __[Feature request]__. Please be specific about why you think this functionality will be of use. If you can, please include some visual description of what you would like the UI to look like, if you are suggesting new UI elements. 

## Built With

Django

### Programming languages

Python 3

### Development
Docker is used to run the development version, so you'll need to install [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/).
Once installed, you just need to copy `cp .env.example .env` and run `docker-compose up` and point your browser to http://localhost:8000/,

A seed command is being run on each start, so you can have fresh new random data to play with. 

In case you are using WSL with Docker for Desktop (version 2.2.0.4) on Windows: you need to have your repository on the Windows file system rather than on the WSL one because otherwise the volume won't be mounted (solution inspired from this work around: https://github.com/docker/for-win/issues/2151#issuecomment-402163189)

If you want to make migrations, run tests or add a dependency, you can get into the web container using:
```bash
docker-compose exec web sh
./manage makemigrations
pip install <my cool dependency>
```

We're using black for formatting and each push is checked against it. Running 
```bash
black --line-length 120 --target-version py37
```
before a commit will do the trick.


## Feedback

* Request a new feature on GitHub.
* Vote for popular feature requests.
* File a bug in GitHub Issues.

