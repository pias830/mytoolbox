#! /usr/bin/python3

import requests
import sys

sub_list = open(".subdomains.txt").read()
subdoms = sub_list.splitlines()

# Check if the script has enough command-line arguments
if len(sys.argv) < 2:
    print("Usage: subdomain 'domain'")
    sys.exit(1)

try:
    for sub in subdoms:
        sub_domains = f"http://{sub}.{sys.argv[1]}"

        try:
            requests.get(sub_domains)

        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", sub_domains)

except KeyboardInterrupt:
    print("\nYou interrupted and that's totally fine.")


