# Response headers are important
import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + "<url>")
    sys.exit(1)


# Banner Grabbing
req = requests.get("https://" + sys.argv[1])
print("\n"+str(req.headers))

# IP
gethostby_ = socket.gethostbyname(sys.argv(1))
print("\nThe IP address of " + sys.argv[1] + " is: " + gethostby_ + "\n")

# ipinfo.io for iplookup
req_ip_lookup = requests.get("https://ipinfo.io/" + gethostby_ + "/json")
resp_ = json.loads(req_ip_lookup.text)

print("Location: " + resp_['loc'])
print("Region: " + resp_['region'])
print("City: " + resp_['city'])
print("Country: " + resp_['country'])