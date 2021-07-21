import os
import json
from dotenv import load_dotenv
import requests
from simple_chalk import chalk
load_dotenv()

if __name__ == '__main__':
    # Print information from Environment variables
    print('{} say "{}"'.format(os.environ.get('USER'), os.environ.get('MSG_INPUT')))
    #print(os.environ.get('MSG_INPUT'))
    try:
        # Send HTTP GET request to watasalim website
        response = requests.get('https://watasalim.vercel.app/api/quotes/random')
    except Exception as exp:
	    print('Caught exception: {}'.format(str(exp)))

    if response.status_code == 200: # HTTP Request OK
        print(chalk.yellow.bold('Salim said {}'.format(response.json()['quote']['body'])))
        print('Powered by {}'.format(response.json()['quote']['url']))
    else: # HTTP Error
        print(chalk.red('Get Salim Quote failure: {} {}'.format(response.status_code, response.reason)))
        print(chalk.red('Text: {}'.format(response.text)))