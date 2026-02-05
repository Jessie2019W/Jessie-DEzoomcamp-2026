## BigQuery Setup
### Upload Data to GCS
Run the provided Python script: load_yellow_taxi_data.py to upload all 6 files of Yellow Taxi Trip Records to GCS bucket

### Create external table in BQ
```SQL
CREATE OR REPLACE EXTERNAL TABLE `project_id.dataset_id.yellow_taxi_2024_external` 
OPTIONS (
    format = 'PARQUET',
    uris = ['gs://bucket_name/yellow_tripdata_2024-*.parquet']
);
```

### Create materialized table
```SQL
CREATE OR REPLACE TABLE `project_id.dataset_id.yellow_taxi_2024`
AS
SELECT *
FROM `project_id.dataset_id.yellow_taxi_2024_external`;
```

## Question 1
```SQL
SELECT count(1) 
FROM `project_id.dataset_id.yellow_taxi_2024`;
```

## Question 2
```SQL
SELECT count(distinct PULocationID)
FROM `project_id.dataset_id.yellow_taxi_2024_external`;

SELECT count(distinct PULocationID)
FROM `project_id.dataset_id.yellow_taxi_2024`;
```

## Question 3
```SQL
SELECT PULocationID
FROM `project_id.dataset_id.yellow_taxi_2024`;

SELECT PULocationID, DOLocationID
FROM `project_id.dataset_id.yellow_taxi_2024`;
```

## Question 4
```SQL
SELECT count(1)
FROM `project_id.dataset_id.yellow_taxi_2024`
where fare_amount=0;
```

## Question 5
```SQL
CREATE OR REPLACE TABLE `project_id.dataset_id.yellow_taxi_2024_pc`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT *
FROM `project_id.dataset_id.yellow_taxi_2024_external`;
```

## Question 6
```SQL
SELECT DISTINCT VendorID
FROM `project_id.dataset_id.yellow_taxi_2024_pc`
WHERE tpep_dropoff_datetime between '2024-03-01' and '2024-03-15';
```

## Question 7
GCP Bucket

## Question 8
False

## Question 9
```SQL
SELECT count(*) 
FROM `project_id.dataset_id.yellow_taxi_2024`
```
