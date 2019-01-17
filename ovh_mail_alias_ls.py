# -*- encoding: utf-8 -*-

import config # config file
import os
# Make sure we are in script's directory for ovh module to find its ovh.conf file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# OVH API python wrapper
import ovh

# API endpoint for email redirection
base_api_endpoint = "/email/domain/%s/redirection" % config.domain

# Create wrapper
client = ovh.Client()

# Get the list
redirection_list = client.get(base_api_endpoint)

# Loop through it
print("ID\tFrom\tTo")
for redir_id in redirection_list:
    redir_details = client.get("%s/%s" % (base_api_endpoint, redir_id))
    print("%s\t%s\t%s" % (redir_id, redir_details['to'], redir_details['from']))
print("")
