Prepare the docker-compose.yaml

Download GCP service account key and encode it 
```
echo SECRET_GCP_SERVICE_ACCOUNT=$(cat service-account.json | base64 -w 0) >> .env_encoded
```

Run `docker compose up -d`

Go to [localhost:8080](http://localhost:8080/) and input the username and password for Kestra

Prepare the workflow in the Kestra. I added 2 new parts based on the course-provided code, `bq_yellow_yearly_archive` and `bq_green_yearly_archive`, to load the yearly data for answering some homework questions much easier.

Go to Triggers, use the backfill to load both yellow and green taxi data from 2019-01-01 to 2021-07-31.
