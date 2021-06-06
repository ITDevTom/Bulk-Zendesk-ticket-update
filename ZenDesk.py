import json
import requests

# Tickets to update
print('This tool will update tickets in batches of five with the same update')
print('Please enter first ticket ID')
id1 = input()
print('Please enter second ticket ID')
id2 = input()
print('Please enter third ticket ID')
id3 = input()
print('Please enter fourth ticket ID')
id4 = input()
print('Please enter fifth ticket ID')
id5 = input()

# Update message
print('What would you like the bulk update to be?')
body = input()

# Package the data in a dictionary matching the expected JSON
data = { 'ticket': { 'comment': { 'body': body } } }

# Encode the data to create a JSON payload
payload = json.dumps(data)

# Set the request parameters
url = 'https://Conpany.zendesk.com/api/v2/tickets/update_many.json?ids=' + id1 + ',' + id2 + ',' + id3 + ',' + id4 + ',' + id5
user = 'User@email.com'
pwd = 'Password'
headers = {'content-type': 'application/json'}

# Do the HTTP put request
response = requests.put(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Report success
print('Successfully added comment to ticket #{}'.format(id1, id2, id3, id4, id4))
