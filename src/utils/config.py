import configparser

config = configparser.ConfigParser()
config.read("src/utils/ip_addres.ini")

ip_address = config.get("server", "ip")
IP = f'http://{ip_address}'