import os
import json
from dotenv import load_dotenv
import requests
from simple_chalk import chalk
load_dotenv()

if __name__ == '__main__':
    # Print information from Environment variables
    print('{} say "{}"'.format(os.environ.get('USER'), os.environ.get('MSG_INPUT')))
    api_url = os.environ.get('BASE_URL') + os.environ.get('API_ENDPOINT')
    #print(os.environ.get('MSG_INPUT'))
    try:
        # Send HTTP GET request to API Endpoint
        response = requests.get(api_url)
    except Exception as exp:
	    print('Caught exception: {}'.format(str(exp)))

    if response.status_code == 200: # HTTP Request OK
        print(chalk.yellow.bold('Salim said {}'.format(response.json()['quote']['body'])))
        print('Powered by {}'.format(response.json()['quote']['url']))
    else: # HTTP Error
        print(chalk.red('Get Salim Quote failure: {} {}'.format(response.status_code, response.reason)))
        print(chalk.red('Text: {}'.format(response.text)))