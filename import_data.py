from google.cloud import automl

project_id = "automl-298621"
display_name = "holidays"
path = "gs://automl-298621-vcm/labels.csv"

client = automl.AutoMlClient()
dataset_id = "ICN6557996421939724288" #from running create_dataset.py
# Get the full path of the dataset.
dataset_full_id = client.dataset_path(
    project_id, "us-central1", dataset_id
)
# Get the multiple Google Cloud Storage URIs
input_uris = path.split(",")
gcs_source = automl.GcsSource(input_uris=input_uris)
input_config = automl.InputConfig(gcs_source=gcs_source)
# Import data from the input URI
response = client.import_data(name=dataset_full_id, input_config=input_config)

print("Processing import...")
print("Data imported. {}".format(response.result()))