# AWS Lambda what3words function

This lambda function interacts with the what3words API to retrieve data regarding a location.


## Files

| File | Description |
|--|--|
| location.py | Location object which calls from what3words and geopy. All location methods are here. |
| lambda_function.py | The primary file that calls the Location object and is executed by AWS lambda |


## Requirements
### Python Packages

    pip install requests
    pip install what3words
    pip install geopy

### what3words API key
Go to [what3words developer page](https://developer.what3words.com/public-api) to get your free API key

## API Gateway Setup




## Request example
