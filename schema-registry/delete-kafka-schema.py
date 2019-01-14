import argparse
import requests

parser = argparse.ArgumentParser(description="Delete schema in Schema Registry")
parser.add_argument("--url", help="schema registry URL", required=True) # http://localhost:8081/subjects/ 
parser.add_argument("--name", help="schema name", required=True) # schema-test

args = parser.parse_args()

registry_url = args.url
schema_name = args.name

print('Removing schema {0}'.format(schema_name))
response = requests.delete(registry_url + schema_name)
print(response)
print(response.text)