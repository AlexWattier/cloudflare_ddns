import requests

with open('/usr/src/app/config.json') as config_file:
    config = json.load(config_file)

zone_id = config["zone_id"]
cloudflare_email = config["cloudflare_email"]
cloudflare_auth_key = config["cloudflare_Auth_Key"]
url = "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": "{cloudflare_email}",
    "X-Auth-Key": "{cloudflare_auth_key}"
}

response = requests.request("GET", url, headers=headers)

print(response.text)