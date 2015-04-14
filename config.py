import json

config_file = open('config.json')

settings = json.loads(config_file.read())
