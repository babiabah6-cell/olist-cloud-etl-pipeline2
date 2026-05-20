from google.cloud import storage
import os

# Authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\olist-cloud-analytics\credentials\gcp-key.json"

PROJECT_ID = "ecomerce-olist-dataset"

BUCKET_NAME = "ecommerce_olist_bucket"

LOCAL_FILE = r"C:\olist-cloud-analytics\data\raw\olist_geolocation_dataset.csv"

DESTINATION_BLOB = "raw/olist_geolocation_dataset.csv"


def upload_geolocation():

    client = storage.Client(project=PROJECT_ID)

    bucket = client.bucket(BUCKET_NAME)

    blob = bucket.blob(DESTINATION_BLOB)

    print("Uploading geolocation dataset...")

    blob.upload_from_filename(
        LOCAL_FILE,
        timeout=1200
    )

    print("Geolocation dataset uploaded successfully")


if __name__ == "__main__":
    upload_geolocation()
