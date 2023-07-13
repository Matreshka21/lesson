import json

file = """ 
{
  "response": [
    {
      "id": 210700286,
      "first_name": "Lindsey",
      "last_name": "Stirling"
    },
    {
      "id": 297428682,
      "first_name": "Jared",
      "last_name": "Leto"
    }
  ]
}
"""

data = json.loads(file)
print(data)

print(data['response'][1]['id'])

wal1 = data['response']
print(wal1)

for itm in wal1:
    if itm['id']>0
        print('id есть')

