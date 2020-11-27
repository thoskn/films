##Set Up
The program is run using docker, so you will need to install docker, see [here](https://docs.docker.com/get-docker/)
The data can be queried using psql which can be installed using [these](https://www.compose.com/articles/postgresql-tips-installing-the-postgresql-client/)
instructions.

## Run
It can then be run by executing the following command: 
```commandline
docker-compose -f docker/docker-compose.yaml up --build
```

##Query
### Connect
You can use psql to query the data. To start a session run the following:
```commandline
psql -h localhost -p 5432 -U truefilm -d films
```
You will be prompted for a password, which is `abc`.

You may now execute queries against the `TOP_FILMS` table.

###Schema
