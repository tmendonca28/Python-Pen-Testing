import requests
import sys

subd_list = open("subd.txt").read()
subd = subd_list.splitlines()

for word in subd:
    url_to_check = f"http://{word}.{sys.argv[1]}"

    try:
        requests.get(url_to_check)
    
    except requests.ConnectionError:
        pass

    else:
        print("Valid domain: ", url_to_check)