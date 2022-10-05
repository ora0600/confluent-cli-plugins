## This a script to list Confluent Schema Registry subjects and versions that are IN USE
## SOFT DELETED subjects are not shown
## ATTENTION: This script is used at your own risk. 
## You need to provide the SR url as well as SR apikey and api secret (lines 8 - 10 below).
import requests
from requests.auth import HTTPBasicAuth

sr_apikey = 'YOURKEY'
sr_apisecret = 'YOURSECRET'
sr_url = 'YOURURL'

auth = HTTPBasicAuth(sr_apikey, sr_apisecret)
r = requests.get(sr_url + '/subjects', auth=auth)
subjects = r.json()
print('')
print("Found in use %d subjects" % len(subjects))
count = 0
print('All subjects and versions - in use')
for subject in subjects:
  r = requests.get('%s/subjects/%s/versions' % (sr_url, subject), auth=auth)
  versions = r.json()
  print('%s\t\t%s' % (subject, versions))
  count += len(versions)
print('Total %d versions' % count)
print('')
