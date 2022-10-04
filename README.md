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
  confluent get service quota              | /confluent-cli/confluent-get-service-quota      
  confluent ksqldb topic analysis          | s/confluent-cli/confluent-ksqldb-topic-analysis  
  confluent sa wo keys                     | /Demos/confluent-cli/confluent-sa-wo-keys   
  confluent list srsubjects inuse          | /plugins/confluent-list-srsubjects-inuse
  confluent list srsubjects all            | /plugins/confluent-list-srsubjects-all
  confluent delete srsubjects permanent    | /plugins/confluent-delete-srsubjects-permanent
```
* confluent api key analysis : will find api key with dropped resources
* confluent check ccloud wasty: will count all billable resources
* confluent get service quota: will give an overview of applied service quota limits, and the current usage
* confluent ksqldb topic analysis: Will show all ksqlDB topics which having no ksqlDB cluster anymore and could be deleted
* confluent sa wo keys: will find service accounts without a API Key
* confluent confluent list srsubjects inuse: will list your Confluent Cloud Schema Registry subjects and versions that are IN USE
* confluent confluent list srsubjects all: will list ALL your Confluent Cloud Schema Registry subjects and versions that are IN USE and SOFT DELETED
* confluent delete srsubjects permanent: will delete your all SOFT DELETED SR subjects. PLEASE, test it first in a test env before you use it in your prod env. DISCLAIMER: You are using it at your own risk. 




I do have bash and Python scripts. So, please install python 3.8.
