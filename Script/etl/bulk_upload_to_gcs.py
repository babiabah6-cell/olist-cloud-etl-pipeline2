from google.cloud import storage
import os

# GCP authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\olist-cloud-analytics\credentials\gcp-key.json"

# GCP settings
PROJECT_ID = "ecomerce-olist-dataset"
BUCKET_NAME = "ecommerce_olist_bucket"

# Local raw data folder
LOCAL_FOLDER = r"C:\olist-cloud-analytics\data\raw"

# GCS destination folder
DESTINATION_FOLDER = "raw"


def bulk_upload_to_gcs():

    print("Starting bulk upload...")

    # Create storage client
    client = storage.Client(project=PROJECT_ID)

    # Connect to bucket
    bucket = client.bucket(BUCKET_NAME)

    # Read local files
    files = os.listdir(LOCAL_FOLDER)

    # Keep only CSV files
    csv_files = [file for file in files if file.endswith(".csv")]

    # Debug print
    print("CSV files detected:")
    print(csv_files)

    print(f"\nFound {len(csv_files)} CSV files\n")

    # Upload loop
    for file_name in csv_files:

        try:

            local_file_path = os.path.join(LOCAL_FOLDER, file_name)

            destination_blob_name = f"{DESTINATION_FOLDER}/{file_name}"

            print(f"Uploading {file_name}...")

            blob = bucket.blob(destination_blob_name)

            blob.upload_from_filename(local_file_path, timeout=600)


            print(f"SUCCESS: {file_name} uploaded\n")

        except Exception as e:

            print(f"FAILED: {file_name}")
            print(e)
            print()

    print("Bulk upload process completed")


if __name__ == "__main__":
    bulk_upload_to_gcs()

