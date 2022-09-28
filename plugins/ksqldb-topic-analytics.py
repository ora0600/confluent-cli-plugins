# api-key-analytics.py

import json
import sys
import requests
import subprocess

env_list = sys.argv[1]
keybase64 = 'your own key'
headersAuth = {'Authorization': 'Basic ' + str(keybase64)}

# open File to write delete commands
command_text_file = open("/tmp/delete_ksqlDB_topic.txt", "w")

#read all environments
with open(env_list) as env:
    envs = json.load(env)
topic_counter = 0
# Wir brauchen cluster pro environment 
# confluent kafka cluster list
# confluent kafka topic list | grep pksqlc
# confluent ksql cluster list

# Do the analysis: Check in Envs -> kafka cluster -> get ksqldb topics out of cluster -> check ksqlDB cluster
for environment in envs:
    envid = environment['id']           
    envname = environment['name']           
    # confluent kafka cluster list
    envcommand = 'confluent kafka cluster list --environment {} -o json > /tmp/kcluster_list.json 2>/dev/null'.format(envid)  
    k = subprocess.Popen(envcommand, stdout=subprocess.PIPE, shell=True)
    k.communicate()  
    # check now kafka clusters in environment
    with open('/tmp/kcluster_list.json') as kcluster:
        kclusters = json.load(kcluster)    
    for kafka in kclusters:
        kid = kafka['id']
        kname = kafka['name']
        kprovider = kafka['provider']
        kregion = kafka['region']
        if kid != '':  # empty
            print('Environment {}: Kafka Cluster ID {} with name {} in {} {} region '.format(envid, kid, kname, kprovider,kregion))
            # now check the topics
            topiccommand = 'confluent kafka topic list --cluster {} --environment {} -o json > /tmp/ktopic_list.json 2>/dev/null'.format(kid, envid)  
            t = subprocess.Popen(topiccommand, stdout=subprocess.PIPE, shell=True)
            t.communicate()  
            with open('/tmp/ktopic_list.json') as ktopic:
                ktopics = json.load(ktopic)   
            for topic in ktopics:
                tname = topic['name']
                # Sample, get the topic prefix typical topic of ksqldb pksqlc-gx63m-processing-log
                if tname.find('pksqlc') > 0:
                    replacedString = tname.replace('_confluent-ksql-', '')
                    replacedString = replacedString.replace('query', '-query')
                    replacedString = replacedString.replace('_command', '-command')
                    replacedString = replacedString.replace('ALERTS', '-ALERTS')
                    replacedString = replacedString.replace('TRIGGERED_ALERTS', '-TRIGGERED_ALERTS')
                    # print(replacedString)
                    a,b,c = replacedString.split('-', 2)
                    topic_prefix = a + '-' + b
                    # print('ksqlDB Topic {} with prefix {} in kafka cluster {} {} in environment {}'.format(tname, topic_prefix, kid, kname, envid))
                    # Now search for ksqlDB and compare topic_prefix
                    ksqldbcommand = 'confluent ksql cluster list  --environment {} -o json > /tmp/ksqldb_list.json 2>/dev/null'.format(envid)  
                    s = subprocess.Popen(ksqldbcommand, stdout=subprocess.PIPE, shell=True)
                    s.communicate()  
                    with open('/tmp/ksqldb_list.json') as ksql:
                            ksqldbs = json.load(ksql)   
                    ksqldb_cluster_available = 'FALSE'
                    for ksqldb in ksqldbs:
                        ksqlid = ksqldb['id']
                        ksqlname = ksqldb['name']
                        ksql_topic_prefix = ksqldb['topic_prefix']
                        ksql_kafka = ksqldb['kafka']
                        if ksqlid != '':  # empty
                            # compare topic_prefix exists
                            if topic_prefix == ksql_topic_prefix:
                                ksqldb_cluster_available = 'TRUE'
                                print('ksqlDB cluster {} using topic prefix {} exists: Topic {} can stay'.format(ksqlname, ksql_topic_prefix, tname))
                    if ksqldb_cluster_available == 'TRUE':
                        print('ksqlDB cluster {} using topic prefix {} exists: Topic {} can stay'.format(ksqlname, ksql_topic_prefix, tname))
                    else:
                        print('No ksqlDB cluster with prefix {}: Topic {} can deleted'.format(topic_prefix, tname))
                        #write string to file
                        delete_command = 'confluent kafka topic delete {} --cluster {} --environment {}'.format(tname, kid, envid)
                        n = command_text_file.write(delete_command)
                        topic_counter+=1

#close file
command_text_file.close()
print('In total {} ksqldb-topics can be deleted having no ksqlDB cluster anymore.'.format(topic_counter))
print('delete command file is stored here /tmp/delete_ksqlDB_topic.txt')
