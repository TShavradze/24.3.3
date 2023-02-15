import requests

status = 'available'

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus", params={'status': 'available'}, headers={'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))


res = requests.post(f"https://petstore.swagger.io/v2/pet", headers={'accept': 'application/json'}, data={'name': 'string'})
print(res.text)

res = requests.delete(f"https://petstore.swagger.io/v2/pet/{0}", data={'key':'value'})
print(res.text)

res = requests.put(f"https://petstore.swagger.io/v2/pet",  data={'name': 'string'})
print(res.text)
