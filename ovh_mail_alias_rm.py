# -*- encoding: utf-8 -*-

import config # config file
import os
import sys
# Make sure we are in script's directory for ovh module to find its ovh.conf file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# OVH API python wrapper
import ovh

# API endpoint for email redirection
base_api_endpoint = "/email/domain/%s/redirection" % config.domain

# Ask for redir ID if not provided through args
if len(sys.argv) < 2:
    redir_id = input("Enter redirection ID:\n")
else:
    redir_id = sys.argv[1]

# Create wrapper
client = ovh.Client()

try:
    # Try to find the ID
    redir_details = client.get("%s/%s" % (base_api_endpoint, redir_id))
    
    # Ask for confirmation
    print("")
    print("Delete the following alias:")
    print("ID    : %s" % redir_id)
    print("From  : %s" % redir_details['from'])
    print("To    : %s" % redir_details['to'])
    print("")
    input("Continue (ENTER or CTRL+C to cancel)?")
    print("")

    print("Deleting...")
    result = client.delete("%s/%s" % (base_api_endpoint, redir_id))
    
    # Check if deletion was real
    try:
        client.get("%s/%s" % (base_api_endpoint, redir_id))
        print("Something went wrong, the alias still seems to exists...")
    except ovh.exceptions.ResourceNotFoundError as e:
        print("Alias deleted!")

except ovh.exceptions.ResourceNotFoundError as e:
    print("Error: alias %s does not exists!" % redir_id)
print("")
