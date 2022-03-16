import requests
from tabulate import tabulate
response = requests.get('https://kubecost.k8s2.oyorooms.io/model/allocation?window=24h&aggregate=deployment&external=true&accumulate=true&shareIdle=false&idleByNode=false&filterNamespaces=owndel')
# print(response.json()["data"][0])


costMatrix = []

tableHeader = ["Name", "CPU", "GPU", "RAM", "Efficiency"]
costMatrix.append(tableHeader)

 
for key, value in response.json()["data"][0].iteritems():
	tableRow = []
	tableRow.append(str(key))
	tableRow.append("$" + str(round(value['cpuCost'], 2)))
	tableRow.append("$" + str(round(value['gpuCost'], 2)))
	tableRow.append("$" + str(round(value['ramCost'], 2)))
	tableRow.append("$" + str(round(value['totalEfficiency'],2)))
	costMatrix.append(tableRow)
	# print(key)
	# print(value)
# print(costMatrix)
print(tabulate(costMatrix, tablefmt='html'))
# for x in response.json()["data"]:

  





