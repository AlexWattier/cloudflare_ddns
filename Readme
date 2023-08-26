# Cloudflare DDNS Docker

This project enables you to set up a Cloudflare Dynamic DNS service using Docker. It uses Python to interact with Cloudflare APIs and ensures that your DNS record is always updated with your current IP address.

## Files

### 1. cloudflareddns.py

This file contains the main script that fetches your current IP address using the IPify API and updates your Cloudflare DNS record with that IP address. The script runs in a loop with a configurable check interval.

### 2. Dockerfile

The Dockerfile defines how to build the Docker image to run the "cloudflareddns.py" script. It uses the Python 3.8 image as the base, installs the "requests" module, and configures the image to run the script as the main process when the container starts.

### 3. config.json

The configuration file contains the necessary information for authenticating with the Cloudflare API and other configuration settings. Make sure to fill this file properly with your own information. Particularly note that the "dns_record_id" field needs to be populated for the script to work correctly.

### 4. listcloudflare.py

This file can be used to list the DNS records in your Cloudflare zone and obtain the ID of the DNS record you want to update. Use this script to retrieve the DNS record ID and fill it into the "dns_record_id" field in the "config.json" file.

## Usage

1. Fill out the "config.json" file correctly with your Cloudflare information and preferences.

2. Use the "listcloudflare.py" file to get the ID of the DNS record you want to update. Copy this ID into the "dns_record_id" field in the "config.json" file.

3. Build the Docker image using the following command in the same directory as your Dockerfile:

   ```sh
   docker build -t cloudflareddns:latest .

4. Run the Docker container using the following command, replacing /path/to/your/config.json with the absolute path to your configuration file:

    ```sh
    docker run --name ddns -it -v /path/to/your/config.json:/usr/src/app/config.json cloudflareddns:latest
