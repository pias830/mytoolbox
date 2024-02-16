#! /usr/bin/python3

import requests
import sys

sub_list = open(".subdomains.txt").read()
subpages = sub_list.splitlines()

# Check if the script has enough command-line arguments
if len(sys.argv) < 2:
    print("Usage: subpage 'domain'")
    sys.exit(1)

try:
    for sub in subpages:
        sub_page = f"http://{sys.argv[1]}/{sub}"

        try:
            requests.get(sub_page)

        except requests.ConnectionError:
            pass

        else:
            print("Valid domain: ", sub_page)

except KeyboardInterrupt:
    print("\nYou interrupted and that's totally fine.")


