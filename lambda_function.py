import json
from location import *


def lambda_handler(event, context):
	#query string params
	w1 = event['queryStringParameters']['w1']
	w2 = event['queryStringParameters']['w2']
	w3 = event['queryStringParameters']['w3']


	print('w1=' + w1)
	print('w2=' + w2)
	print('w3=' + w3)

	# create object
	address = Location(w1,w2,w3)

	#construct the body of the response object
	transactionResponse = {}
	transactionResponse['word1'] = w1
	transactionResponse['word2'] = w2
	transactionResponse['word3'] = w3
	transactionResponse['what3words'] = {}
	transactionResponse['what3words']['latitude'] = address.get_lat_long()[1]
	transactionResponse['what3words']['longitude'] = address.get_lat_long()[0]
	transactionResponse['what3words']['address'] = address.find_address()
	transactionResponse['message'] = 'Hello from Lambda land'

	#construct http response 
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(transactionResponse)

	
	return responseObject

# main for local testing 
if __name__ == "__main__":

    event ={
    "queryStringParameters": {
          "w1": "quit",
		  "w2": "kind",
		  "w3": "drag"
          }
    }
    context = []
    print(lambda_handler(event, context))
