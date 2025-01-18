# Read the default_config_generation file
import configparser
import os

import requests


def ssl_getter():
    # Create a ConfigParser object
    config = configparser.ConfigParser()
    # Read the configuration file
    config.read('config.ini')

    # Extract the API key, private key, domain, and destination from the configuration file
    api_key = config['DEFAULT']['key']
    private_key = config['DEFAULT']['private-key']
    domain = config['DEFAULT']['domain']
    location = config['DEFAULT']['destination']

    # Define the URL for the API request
    url = f"https://api.porkbun.com/api/json/v3/ssl/retrieve/{domain}"
    # Define the payload for the API request
    payload = {
        "secretapikey": private_key,
        "apikey": api_key
    }

    # Send the POST request to the API
    response = requests.post(url, json=payload)

    # Parse the response data as JSON
    response_data = response.json()

    # Create the destination directory if it does not exist
    os.makedirs(location, exist_ok=True)
    # Set the location to the current directory if it is not specified
    if not location:
        location = '.'

    # Define the file paths for the certificate, private key, and public key
    cert_file = os.path.join(location, "domain.cert.pem")
    private_key_file = os.path.join(location, "private.key.pem")
    public_key_file = os.path.join(location, "public.key.pem")

    # Write the certificate to the file
    with open(cert_file, 'w') as cert_out:
        cert_out.write(response_data.get('certificatechain', ''))

    # Write the private key to the file
    with open(private_key_file, 'w') as private_key_out:
        private_key_out.write(response_data.get('privatekey', ''))

    # Write the public key to the file
    with open(public_key_file, 'w') as public_key_out:
        public_key_out.write(response_data.get('publickey', ''))

    # Print the file paths where the data has been written
    print(f"Certificate chain written to {cert_file}")
    print(f"Private key written to {private_key_file}")
    print(f"Public key written to {public_key_file}")
