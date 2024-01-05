# `confluent cli` plugins

The confluent command line interface `confluent` allows to write easy plugins to do stuff like analysis of things, print out daily summaries, doing a complex job like onboarding a team project.
For you can wirte scripts in a language you want. The only things you have to do:
* put the execuable scripts in directory and add to the $PATH variable
* script must start with "confluent" e.g. "confluent-show-me-the highwatermark" the dashed will interpreted as " " (spaces), so you can write want you want.

This repo will show some simple plugins for `confluent cli`
```bash
           Plugin Name                     |              File Path                                
-------------------------------------------+---------------------------------------------------
  confluent api key analysis               | /confluent-cli/confluent-api-key-analysis       
  confluent check ccloud wasty             | /confluent-cli/confluent-check-ccloud-wasty
  confluent check internal topics          | /confluent-cli/confluent-check-internal-topics  
  confluent get service quota              | /confluent-cli/confluent-get-service-quota      
  confluent ksqldb topic analysis          | /confluent-cli/confluent-ksqldb-topic-analysis  
  confluent sa wo keys                     | /confluent-cli/confluent-sa-wo-keys   
  confluent list srsubjects inuse          | /confluent-cli/confluent-list-srsubjects-inuse
  confluent list srsubjects all            | /confluent-cli/confluent-list-srsubjects-all
  confluent delete srsubjects permanent    | /confluent-cli/confluent-delete-srsubjects-permanent
  confluent del orphaned acls              | /confluent-cli/confluent-del-orphaned-acls
  confluent recently used apikeys          | /confluent-cli/confluent-recently-used-apikeys 
  
```
* confluent api key analysis : will find api key with dropped resources
* confluent check ccloud wasty: will count all billable resources
* confluent check internal topics: will show all internal topics and generate a bash script to delete them, per cluster and environment
* confluent get service quota: will give an overview of applied service quota limits, and the current usage
* confluent ksqldb topic analysis: Will show all ksqlDB topics which having no ksqlDB cluster anymore and could be deleted
* confluent sa wo keys: will find service accounts without a API Key
* confluent confluent list srsubjects inuse: will list your Confluent Cloud Schema Registry subjects and versions that are IN USE
* confluent confluent list srsubjects all: will list ALL your Confluent Cloud Schema Registry subjects and versions that are IN USE and SOFT DELETED
* confluent delete srsubjects permanent: will delete your all SOFT DELETED SR subjects. PLEASE, test it first in a test env before you use it in your prod env. 
* confluent del orphaned acls  : Print out where could be a problem with orphaned ACLs
* confluent recently used api keys: print out API keys used so far, all other API keys could be an option to delete.


DISCLAIMER: You are using it at your own risk. Here are only samples of useful tools.

Please change the script with your own API Keys and REST URLs.

I do have bash and Python scripts. So, please install python 3.8.

Additional plug-ins
* Please check Repo for [Schema deletion tool](https://github.com/confluentinc/schema-deletion-tool)
