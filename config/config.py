import configparser


def create_default_config():
    config = configparser.ConfigParser()

    key = input("Enter your Porkbun API key: ")
    if len(key) <= 0:
        print("Please enter a valid API key")
        return

    private = input("Enter your Porkbun private key: ")
    if len(private) <= 0:
        print("Please enter a valid private key")
        return

    domain = input("Enter the domain you want to retrieve the SSL certificate for: ")
    if len(domain) <= 0 & domain.count('.') != 1:
        print("Please enter a valid domain")
        return

    destination = input(
        "Enter the destination for the SSL certificate files\nLeave empty to drop the files in the current location: ")

    config['DEFAULT'] = {
        'key': key,
        'private-key': private,
        'domain': domain,
        'destination': destination
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("Made config file as config.ini\n"
          "Manually edit this file if you want to change the domain or keys.")
