import requests
import json
import os, sys
import subprocess
import getpass

if len(sys.argv) < 2:
	print 'Try again with username'
	sys.exit(1) 

username = sys.argv[1]
token = "a2e6eb20283eba576de4ad2bcc53471c9c46e14b"

baseURL = "https://api.github.com/users/"+ username

response = requests.get(baseURL)
responseData = response.json()

print "Hello, " , responseData['name']

repoURL = baseURL + "/repos"
parameters = { "access_token" : token, "per_page" : "200" }
response = requests.get(repoURL, params=parameters)
responseData = response.json()

with open("data.json", 'w') as outfile: 
	json.dump(responseData, outfile)

with open("url.txt", "w") as outfile:
	for key in responseData:
		outfile.write(key['clone_url'] + "\n")

urllist = [line.rstrip('\n') for line in open('url.txt', 'r')]

# '''
path = "/home/" + getpass.getuser() + "/Development/github"
print "Path: ", path

try:
	os.chdir(path)
except OSError:
	os.makedirs(path)
	os.chdir(path)

retval = os.getcwd()
print "Directory changed successfully %s" % retval

for cloneURL in urllist:
	subprocess.call(["git", "clone", cloneURL])


print "Done!"