#!/bin/bash

## This script is used to delete all SOFT DELETED subjects.
## Please try this script in a test environment first. ATTENTION: This script is used at your own risk. 
## Change Schema Registry API Key and API Secret and Schema Registry url (lines 10 and 12 below).
## Don't wonder in the subjects_todelete.txt you will find ALL subjects. Subjects IN USE and subjects SOFT DELETED.
## However, to delete PERMANENTLY subjects, they need to be first SOFT DELETED.
## This means subjects that are not SOFT DELETED - means IN USE - can't be PERMANENTLY DELETED.

curl -X GET -u "APIKEY:APISECRET" https://psrc-opw.europe-west.gcp.confluent.cloud/subjects?deleted=true|jq |awk -F '"' '{print $2}' >subjects_todelete.txt

while read line; do curl  -X DELETE  -u "APIKEY:APISECRET" https://psrc-opw.europe-west.gcp.confluent.cloud/subjects/$line?permanent=true; done< subjects_todelete.txt
