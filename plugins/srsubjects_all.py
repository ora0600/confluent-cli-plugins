## This a script to list all Confluent Schema Registry subjects and versions - IN USE and SOFT DELETED
## ATTENTION: This script is used at your own risk. 
## You need to provide the SR url as well as SR api key and api secret (lines 7 - 9 below).
import requests
from requests.auth import HTTPBasicAuth

sr_apikey = '5E3AAFNBZ'
sr_apisecret = 'Yc+H885rLIDXaKBVX41ml0pAf+yr'
sr_url = 'https://psrc-opw.europe-west.gcp.confluent.cloud'

auth = HTTPBasicAuth(sr_apikey, sr_apisecret)
r1 = requests.get(sr_url + '/subjects?deleted=true', auth=auth)
subjects1 = r1.json()

r2 = requests.get(sr_url + '/subjects', auth=auth)
subjects2 = r2.json()

softdeleted = len(subjects1) - len(subjects2)
print('')
print("Found in use %d subjects" % len(subjects2))
print("Found %d soft deleted subjects" % softdeleted)

count = 0
print('All subjects and versions - in use and soft deleted')

for subject in subjects1:
  r1 = requests.get('%s/subjects/%s/versions?deleted=true' % (sr_url, subject), auth=auth)
  versions1 = r1.json()
  print('%s\t\t%s' % (subject, versions1))
  count += len(versions1)

print('Total %d versions' % count)
print('')
