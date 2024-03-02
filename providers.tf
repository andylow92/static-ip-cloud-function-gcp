# Configure Google Cloud Provider
provider "google" {
  project = "gcp project id"
  region  = "europe-west1"
  credentials = "${file("account.json")}"
}
