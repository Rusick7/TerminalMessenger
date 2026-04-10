import json
import subprocess

stdout, stderr = subprocess.Popen('curl https://api.ipify.org?format=json'.split(sep=' '),
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  text=True, shell=True).communicate()

with open("ip_info.json", "w") as f:
    json.dump(json.loads(stdout), f)