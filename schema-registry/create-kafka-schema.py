import argparse
import requests

parser = argparse.ArgumentParser(description="Create schema in Schema Registry")
parser.add_argument("--url", help="schema registry URL") # http://localhost:8081/subjects/ 
parser.add_argument("--name", help="schema name") # schema-test

args = parser.parse_args()

registry = args.url + args.name + '/versions'

headers = {
    'Content-Type': 'application/vnd.schemaregistry.v1+json',
}

data = '{"schema": "{\\"type\\":\\"record\\",\\"name\\":\\"Payment\\",\\"namespace\\":\\"io.confluent.examples.clients.basicavro\\",\\"fields\\":[{\\"name\\":\\"id\\",\\"type\\":\\"string\\"},{\\"name\\":\\"amount\\",\\"type\\":\\"double\\"}]}"}'

response = requests.post(registry, headers=headers, data=data)

print(response)
print(response.text)