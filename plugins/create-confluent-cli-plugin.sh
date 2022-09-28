#!/bin/bash
# create plugin for cli

confluent login
confluent plugin list

cd ~/Demos/confluent-cli
vi ~/.bash_profile
# add cli path export PATH=$CONFLUENT_HOME/bin:/Users/cmutzlitz/Demos/confluent-cli:$PATH
source ~/.bash_profile
#copy my service quota check N RENAME IT
mv 00_get_service_quota.sh confluent-get-service-quota

# run the plugin with additional arguments and flags passed in by the user
confluent get service quota
