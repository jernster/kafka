import requests
import argparse

parser = argparse.ArgumentParser(description="Delete schema in Schema Registry")
parser.add_argument("--url", help="schema registry URL") # http://localhost:8081/subjects/ 
parser.add_argument("--name", help="schema name") # schema-test

args = parser.parse_args()

registry_url = args.url
schema_name = args.name

print('Removing schema {0}'.format(schema_name))
response = requests.delete(registry_url + schema_name)
print(response)
print(response.text)