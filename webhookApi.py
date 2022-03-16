import requests

response = requests.get('https://kubecost.k8s2.oyorooms.io/model/allocation?window=24h&aggregate=deployment&external=true&accumulate=true&shareIdle=false&idleByNode=false&filterNamespaces=owndel')
print(response.json()["data"])


