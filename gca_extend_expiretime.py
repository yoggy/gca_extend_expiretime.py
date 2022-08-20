#!/usr/bin/python3

import sys
import os
import glob
import subprocess
import json

current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

def usage():
  print(f"usage: {os.path.basename(__file__)} ~/your_credentials.json")
  print()
  sys.exit(1)

if len(sys.argv) == 1:
  usage()

json_file = sys.argv[1]

bearer_token = subprocess.check_output(["./oauth2l","fetch","--json",json_file,"arcore.management"],stderr=subprocess.DEVNULL)
bearer_token = bearer_token.decode()
bearer_token = bearer_token.strip()

gca_list_str = subprocess.check_output(["curl","-s","-H",f"Authorization: Bearer {bearer_token}","https://arcore.googleapis.com/v1beta2/management/anchors?page_size=9999"],stderr=subprocess.DEVNULL)

gca_list = json.loads(gca_list_str)

for gca in gca_list["anchors"]:
  anchor_id = gca["name"].split("/")[1]  #name="anchor/ua-xxxxxxxxxxxxxxxx"

  rv = subprocess.check_output(["curl","-H",f"Authorization: Bearer {bearer_token}","-H","Content-Type: application/json","-X","PATCH",f"https://arcore.googleapis.com/v1beta2/management/anchors/{anchor_id}?updateMask=expire_time","-d","{expireTime:\"2999-12-31T00:00:00Z\"}"],stderr=subprocess.DEVNULL)

  print(rv)

