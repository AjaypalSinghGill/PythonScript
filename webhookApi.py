import requests
from tabulate import tabulate
from datetime import date, timedelta

def getTotalCostOfNthDay(n):
	d = date.today() - timedelta(days=n)
	startDate = d
	endDate = date.today() - timedelta(days=(n-1))
	print(startDate)
	print(endDate)
	url = 'https://kubecost.k8s2.oyorooms.io/model/allocation?window={startDate}T00%3A00%3A00Z%2C{endDate}T00%3A00%3A00Z&aggregate=deployment&external=true&accumulate=true&shareIdle=false&idleByNode=false&shareTenancyCosts=true&filterNamespaces=owndel'.format(startDate = startDate, endDate = endDate)
	response = requests.get(url)

	costMatrix = []

	tableHeader = ["Name", "CPU", "GPU", "RAM", "Efficiency"]
	costMatrix.append(tableHeader)

	totalCpuCost = 0
	totalGpuCost = 0
	totalRamCost = 0
	 
	for key, value in response.json()["data"][0].iteritems():
		totalCpuCost = totalCpuCost + round(value['cpuCost'], 2)
		totalGpuCost = totalGpuCost + round(value['gpuCost'], 2)
		totalRamCost = totalRamCost + round(value['ramCost'], 2)

	totalCostRow = ["Total Cost({date})".format(date=startDate),"$" + str(totalCpuCost),"$" +  str(totalGpuCost),"$" +  str(totalRamCost)]

	return totalCostRow






response = requests.get('https://kubecost.k8s2.oyorooms.io/model/allocation?window=24h&aggregate=deployment&external=true&accumulate=true&shareIdle=false&idleByNode=false&filterNamespaces=owndel')
# print(response.json()["data"][0])


costMatrix = []
costMatrixOfUnderPerforming = []

tableHeader = ["Name", "CPU", "GPU", "RAM", "Efficiency"]
costMatrix.append(tableHeader)
costMatrixOfUnderPerforming.append(tableHeader)

totalCpuCost = 0
totalGpuCost = 0
totalRamCost = 0
 
for key, value in response.json()["data"][0].iteritems():
	totalCpuCost = totalCpuCost + round(value['cpuCost'], 2)
	totalGpuCost = totalGpuCost + round(value['gpuCost'], 2)
	totalRamCost = totalRamCost + round(value['ramCost'], 2)
	tableRow = []
	if(str(key)=="__idle__"):
		continue
	tableRow.append(str(key))
	tableRow.append("$" + str(round(value['cpuCost'], 2)))
	tableRow.append("$" + str(round(value['gpuCost'], 2)))
	tableRow.append("$" + str(round(value['ramCost'], 2)))
	tableRow.append(str(round(value['totalEfficiency'],2)))
	costMatrix.append(tableRow)
	if(value['totalEfficiency'] < .30):
		costMatrixOfUnderPerforming.append(tableRow)
	# print(key)
	# print(value)
# print(costMatrix)

totalCostRow = ["Total Cost(Last 24 hours)","$" + str(totalCpuCost),"$" +  str(totalGpuCost),"$" +  str(totalRamCost)]

costMatrix.append(totalCostRow)
# finalCostMatrix = []

# finalCostMatrix.append(totalCostRow)

# finalCostMatrix.update(costMatrix)
costMatrix.append(getTotalCostOfNthDay(2))
costMatrix.append(getTotalCostOfNthDay(3))
costMatrix.append(getTotalCostOfNthDay(9))
table = tabulate(costMatrix, tablefmt='html')
# table = table.replace("<table>", "<table border=\"1\"  class=\"dataframe\">")

print(table)
# for x in response.json()["data"]:

webhook_url="https://oyoenterprise.webhook.office.com/webhookb2/ad40733b-2c8e-4d8a-833c-016e5d1d3030@04ec3963-dddc-45fb-afb7-85fa38e19b99/IncomingWebhook/65e3f90f975242ef87d4a6c28cca44d3/a3fa0b73-93cc-4cf0-945e-049bd89348e7"


responseWebhook = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": "000000",
            "summary": "Cost metrics of all service",
            "sections": [{
                "activityTitle": "Cost metrics of all service",
                "activitySubtitle": tabulate(costMatrix, headers="firstrow", tablefmt='grid')
            }],
        },
    )


responseWebhook = requests.post(
        url=webhook_url,
        headers={"Content-Type": "application/json"},
        json={
            "themeColor": "000000",
            "summary": "Cost metrics of under utilised services for last 24 hours(Efficiency less than 30%)",
            "sections": [{
                "activityTitle": "Cost metrics of under utilised services for last 24 hours(Efficiency less than 30%)",
                "activitySubtitle": tabulate(costMatrixOfUnderPerforming, headers="firstrow", tablefmt='grid')
            }],
        },
    )
  





