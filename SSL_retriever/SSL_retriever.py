# Read the default_config_generation file
import configparser
import os

import requests


def ssl_getter():
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Extract the API key and domain from the default_config_generation file
    api_key = config['DEFAULT']['key']
    private_key = config['DEFAULT']['private-key']
    domain = config['DEFAULT']['domain']
    location = config['DEFAULT']['destination']

    # Define the URL and payload
    url = f"https://api.porkbun.com/api/json/v3/ssl/retrieve/{domain}"
    payload = {
        "secretapikey": private_key,
        "apikey": api_key
    }

    # Send the POST request
    response = requests.post(url, json=payload)

    response_data = response.json()

    # Print the response
    # Write the response data to files
    os.makedirs(location, exist_ok=True)
    if not location:
        location = '.'

    cert_file = os.path.join(location, "domain.cert.pem")
    private_key_file = os.path.join(location, "private.key.pem")
    public_key_file = os.path.join(location, "public.key.pem")

    with open(cert_file, 'w') as cert_out:
        cert_out.write(response_data.get('certificatechain', ''))

    with open(private_key_file, 'w') as private_key_out:
        private_key_out.write(response_data.get('privatekey', ''))

    with open(public_key_file, 'w') as public_key_out:
        public_key_out.write(response_data.get('publickey', ''))

    print(f"Certificate chain written to {cert_file}")
    print(f"Private key written to {private_key_file}")
    print(f"Public key written to {public_key_file}")
