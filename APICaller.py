#Author: Nathaniel Mugenyi
#Project Name: API Caller 

#Description: A script to call an API 

import requests

def get_posts():

    #API endpoint 
    url = 'http://127.0.0.1:8000/'

    try:
        #Make a get request to the API endpoint
        response = requests.get(url)

        #Check if the request was succesful 
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
        
    except requests.exceptions.RequestException as e:

        # For handling any network related errors or exceptions
        print('Error:', e)
        return None

def main():

    posts = get_posts()
    if posts:
        print('Value:', posts['Hello'])

    else:
        print('Failed to fetch posts from API.')

if __name__ == '__main__':
    main()
