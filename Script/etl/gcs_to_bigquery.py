from google.cloud import bigquery
from google.cloud import storage
import os

# Authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\olist-cloud-analytics\credentials\gcp-key.json"

# GCP settings
PROJECT_ID = "ecomerce-olist-dataset"

DATASET_ID = "olist"

BUCKET_NAME = "ecommerce_olist_bucket"

GCS_FOLDER = "raw"


def load_gcs_to_bigquery():

    # BigQuery client
    bq_client = bigquery.Client(project=PROJECT_ID)

    # Storage client
    storage_client = storage.Client(project=PROJECT_ID)

    bucket = storage_client.bucket(BUCKET_NAME)

    blobs = bucket.list_blobs(prefix=GCS_FOLDER)

    for blob in blobs:

        if blob.name.endswith(".csv"):

            file_name = blob.name.split("/")[-1]

            table_name = file_name.replace(".csv", "")

            table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

            gcs_uri = f"gs://{BUCKET_NAME}/{blob.name}"

            print(f"Loading {file_name} into BigQuery...")

            job_config = bigquery.LoadJobConfig(

                source_format=bigquery.SourceFormat.CSV,

                skip_leading_rows=1,

                autodetect=True,

                write_disposition="WRITE_TRUNCATE"

            )

            load_job = bq_client.load_table_from_uri(

                gcs_uri,

                table_id,

                job_config=job_config

            )

            load_job.result()

            print(f"SUCCESS: {table_name} loaded")

    print("\nAll tables loaded successfully")


if __name__ == "__main__":
    load_gcs_to_bigquery()


