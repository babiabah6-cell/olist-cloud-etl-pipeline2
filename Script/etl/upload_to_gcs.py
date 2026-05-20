from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\olist-cloud-analytics\credentials\gcp-key.json"

PROJECT_ID = "ecomerce-olist-dataset"

BUCKET_NAME = "ecommerce_olist_bucket"

LOCAL_FILE = r"data/raw/olist_orders_dataset.csv"
DESTINATION_BLOB = "raw/olist_orders_dataset.csv"


def upload_to_gcs():

    client = storage.Client(project=PROJECT_ID)

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(DESTINATION_BLOB)

    blob.upload_from_filename(LOCAL_FILE)

    print(f"Uploaded successfully to gs://{BUCKET_NAME}/{DESTINATION_BLOB}")


if __name__ == "__main__":
    upload_to_gcs()
