Ansible Playbook Netology-8.02
Example Ansible Playbook Netology-8.02 repository containing an initial structure for Java, Elasticsearch and Kibana on the docker host with centos7 

The playbook has the following dirs:

Inventory (hosts)
Group_vars (variables)
Files
site.yml

Inventory (hosts)
This folder contains file prod.yml which specified using hosts, connections etc.


Group_vars
This repo contains a group_vars folder that includes standard connectivity variables defined 
for Java, ElastiSearch and Kibana.
Used variables are version, home directory which specified in the corresponding files.

Files
This repo contains archive with Java.

site.yml
describes task for installation of Java, ElasticSearch and Kibana on one host (centos7).
tags: java, elastic, kibana, skip_ansible_lint.
