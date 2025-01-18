# Import the configparser module to handle configuration files
import configparser


def create_default_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Prompt the user to enter their Porkbun API key
    key = input("Enter your Porkbun API key: ")
    if len(key) <= 0:
        print("Please enter a valid API key")
        return

    # Prompt the user to enter their Porkbun private key
    private = input("Enter your Porkbun private key: ")
    if len(private) <= 0:
        print("Please enter a valid private key")
        return

    # Prompt the user to enter the domain for the SSL certificate
    domain = input("Enter the domain you want to retrieve the SSL certificate for: ")
    if len(domain) <= 0 & domain.count('.') != 1:
        print("Please enter a valid domain")
        return

    # Prompt the user to enter the destination for the SSL certificate files
    destination = input(
        "Enter the destination for the SSL certificate files\nLeave empty to drop the files in the current location: ")

    # Set the configuration values
    config['DEFAULT'] = {
        'key': key,
        'private-key': private,
        'domain': domain,
        'destination': destination
    }

    # Write the configuration to a file named config.ini
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("Made default_config_generation file as config.ini\n"
          "Manually edit this file if you want to change the domain or keys.")
