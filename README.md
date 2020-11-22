
# AWS Lambda what3words function

A serverless lambda function which interacts with the what3words API to retrieve data regarding a location.


## Files

| File | Description |
|--|--|
| location.py | Location object which calls from what3words and geopy. All location methods are here. |
| lambda_function.py | The primary file that calls the Location object and is executed by AWS lambda. |


## Requirements
### Python Packages

    pip install requests
    pip install what3words
    pip install geopy

### what3words API key
Go to [what3words developer page](https://developer.what3words.com/public-api) to get your free API key


## Request example

    QueryStringParameters = w1=unrealistic&w2=units&w3=device

```json
{
   "word1":"unrealistic",
   "word2":"units",
   "word3":"device",
   "what3words":{
      "latitude":-1.547537,
      "longitude":53.796289,
      "address":"The Black Prince, City Square, Holbeck Urban Village, Leeds, West Yorkshire, Yorkshire and the Humber, England, LS1 2ES, United Kingdom",
      "directions":"https://www.google.com/maps/dir/?api=1&destination=53.796289,-1.547537"
   }
}
```
