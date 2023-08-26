import requests
import json
import time

# Config
with open('/usr/src/app/config.json') as config_file:
    config = json.load(config_file)

cloudflare_email = config["cloudflare_email"]
cloudflare_token = config["cloudflare_token"]
zone_id = config["zone_id"]
dns_record_id = config["dns_record_id"]
domain = config["domain"]
check_interval = config["check_interval"]


def get_current_ip():
    response = requests.get("https://api64.ipify.org?format=json")
    data = response.json()
    return data["ip"]


def update_dns_record(ip):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{dns_record_id}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {cloudflare_token}"
    }
    payload = {
        "type": "A",
        "name": domain,
        "content": ip
    }
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    return response.json()

def main():
    current_ip = get_current_ip()
    print(f"IP actuel: {current_ip}")
    update_response = update_dns_record(current_ip)
    if update_response["success"]:
        print("DNS update reussi.")
    else:
        print(update_response)
        print("update rater.")
        
    time.sleep(check_interval)


try:
    while True:
        main()
except KeyboardInterrupt:
    print("arret.")
