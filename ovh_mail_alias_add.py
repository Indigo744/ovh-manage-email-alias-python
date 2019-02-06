# -*- encoding: utf-8 -*-

import config # config file
import os
import sys
from slugify import slugify
import tldextract
# Make sure we are in script's directory for ovh module to find its ovh.conf file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# OVH API python wrapper
import ovh

# API endpoint for email redirection
base_api_endpoint = "/email/domain/%s/redirection" % config.domain

# Ask for redir name if not provided through args
if len(sys.argv) < 2:
    src = input("Enter an alias name (or an URL to extract the domain):\n")
else:
    src = sys.argv[1]

# Remove any surounding whitespaces
src = src.strip()

# If starts with http or www, try to extract the domain
if src.startswith('http') or src.startswith('www'):
    src = slugify(tldextract.extract(src).domain, max_length=10, word_boundary=True, separator="-")

# Determine from/to parameters
param_from = "%s%s%s@%s" % (config.alias_prefix, src, config.alias_suffix, config.domain)
param_to = config.alias_to

# Ask for confirmation
print("")
print("Create email alias:")
print("From: %s" % param_from)
print("To  : %s" % param_to)
print("")
input("Continue (ENTER or CTRL+C to cancel)?")
print("")

# Create wrapper
client = ovh.Client()

try:
    # Create alias
    result = client.post(base_api_endpoint, _from=param_from, to=param_to, localCopy=False)
    print("Alias created (ID=%s)" % result['id'])
except ovh.exceptions.ResourceConflictError as e:
    print("Error: an alias with the same name already exists")
print("")
