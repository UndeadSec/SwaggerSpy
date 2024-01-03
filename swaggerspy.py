#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests, sys, re
from colorama import Fore, Style

regex_patterns = {
    'google_api'     : r'AIza[0-9A-Za-z-_]{35}',
	'firebase'  : r'AAAA[A-Za-z0-9_-]{7}:[A-Za-z0-9_-]{140}',
	'google_captcha' : r'6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
	'google_oauth'   : r'ya29\.[0-9A-Za-z\-_]+',
	'amazon_aws_access_key_id' : r'A[SK]IA[0-9A-Z]{16}',
	'amazon_mws_auth_toke' : r'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
	'amazon_aws_url' : r's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
	'amazon_aws_url2' : r"(" \
		   r"[a-zA-Z0-9-\.\_]+\.s3\.amazonaws\.com" \
		   r"|s3://[a-zA-Z0-9-\.\_]+" \
		   r"|s3-[a-zA-Z0-9-\.\_\/]+" \
		   r"|s3.amazonaws.com/[a-zA-Z0-9-\.\_]+" \
		   r"|s3.console.aws.amazon.com/s3/buckets/[a-zA-Z0-9-\.\_]+)",
	'facebook_access_token' : r'EAACEdEose0cBA[0-9A-Za-z]+',
	'authorization_basic' : r'basic [a-zA-Z0-9=:_\+\/-]{5,100}',
	'authorization_bearer' : r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}',
	'mailgun_api_key' : r'key-[0-9a-zA-Z]{32}',
	'twilio_api_key' : r'SK[0-9a-fA-F]{32}',
	'twilio_account_sid' : r'AC[a-zA-Z0-9_\-]{32}',
	'twilio_app_sid' : r'AP[a-zA-Z0-9_\-]{32}',
	'paypal_braintree_access_token' : r'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
	'square_oauth_secret' : r'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
	'square_access_token' : r'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
	'stripe_standard_api' : r'sk_live_[0-9a-zA-Z]{24}',
	'stripe_restricted_api' : r'rk_live_[0-9a-zA-Z]{24}',
	'github_access_token' : r'[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
	'rsa_private_key' : r'-----BEGIN RSA PRIVATE KEY-----',
	'ssh_dsa_private_key' : r'-----BEGIN DSA PRIVATE KEY-----',
	'ssh_dc_private_key' : r'-----BEGIN EC PRIVATE KEY-----',
	'pgp_private_block' : r'-----BEGIN PGP PRIVATE KEY BLOCK-----',
	'json_web_token' : r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$',
	'slack_token' : r"\"api_token\":\"(xox[a-zA-Z]-[a-zA-Z0-9-]+)\"",
	'SSH_privKey' : r"([-]+BEGIN [^\s]+ PRIVATE KEY[-]+[\s]*[^-]*[-]+END [^\s]+ PRIVATE KEY[-]+)",
	'Heroku API KEY' : r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
	'possible_Creds' : r'(?i)(" \
					r"password\s*[`=:\"]+\s*[^\s]+|" \
					r"password is\s*[`=:\"]*\s*[^\s]+|" \
					r"pwd\s*[`=:\"]*\s*[^\s]+|" \
					r"passwd\s*[`=:\"]+\s*[^\s]+)',
	'email': r"[\w\.-]+@[\w\.-]+\.\w+",
	'ip': r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)",
}

def check_regex(data, regex_patterns):
    for pattern_name, pattern in regex_patterns.items():
        match = re.search(pattern, data)
        if match:
            return pattern_name, match.group()
    return None, None

def process_url(url, regex_patterns):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text
            matching_contents = []
            for line in data.split('\n'):
                pattern_name, matched_content = check_regex(line, regex_patterns)
                if pattern_name:
                    matching_contents.append((pattern_name, matched_content))
            return matching_contents
    except Exception as e:
        print(f"Error processing URL {url}: {e}")
    return []

def make_request(url, search_term, page):
    headers = {"accept": "application/json"}
    response = requests.get(url.format(search_term, page + 1), headers=headers)
    json_data = response.json()
    return json_data

def parse_data_api(json_api_data):
    url_list = []
    try:
        for api in json_api_data.get("apis", []):
            for prop in api.get("properties", []):
                url = prop.get("url")
                if url:
                    url_list.append(url)
    except Exception as e:
        print(f"Error parsing JSON data: {e}")
    return url_list

def get_urls(search_term):
    base_url = "https://app.swaggerhub.com/apiproxy/specs?sort=BEST_MATCH&order=DESC&query={}&page={}&limit=100"
    session = requests.Session()

    response = session.get(base_url.format(search_term, 0), headers={"accept": "application/json"})
    json_response = response.json()
    total_apis = int(json_response.get("totalCount", 0))
    pages_to_go_through = total_apis // 100
    urls_to_go_through = parse_data_api(json_response)

    threads = []
    with ThreadPoolExecutor(max_workers=25) as executor:
        for page in range(1, pages_to_go_through + 1):
            threads.append(executor.submit(make_request, base_url, search_term, page))

    for completed_task in as_completed(threads):
        json_data = completed_task.result()
        urls = parse_data_api(json_data)
        urls_to_go_through.extend(urls)

    urls_to_go_through = list(filter(None, urls_to_go_through))

    return urls_to_go_through

def print_colored(text, color):
    print(f"{color}{text}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_colored('''
         █▀▀ █ █ █▀█ █▀▀ █▀▀ █▀▀ █▀█ █▀▀ █▀█ █ █
         ▀▀█ █▄█ █▀█ █ █ █ █ █▀▀ █▀▄ ▀▀█ █▀▀  █
         ▀▀▀ ▀ ▀ ▀ ▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀ ▀ ▀▀▀ ▀    ▀  by Alisson Moretto (UndeadSec)
              AUTOMATED OSINT ON SWAGGERHUB''', Fore.MAGENTA)

    if len(sys.argv) != 2:
        print_colored("\nUsage: python3 swaggerspy.py searchterm (more accurate with domains).\n $ python3 swaggerspy.py test.com", Fore.RED)
        sys.exit(1)

    search_term = sys.argv[1]
    result_urls = get_urls(search_term)

    if result_urls:
        print("\n[*] Found {} urls".format(len(result_urls)))
    else:
        print("\n[!] No results")

    with ThreadPoolExecutor(max_workers=25) as executor:
        future_to_url = {executor.submit(process_url, url, regex_patterns): url for url in result_urls}

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            print_colored(f"\nURL: {url}", Fore.CYAN)

            try:
                matching_contents = future.result()

                if matching_contents:
                    for pattern_name, content in matching_contents:
                        print_colored(f"[*] {pattern_name}: {content}", Fore.GREEN)
                else:
                    print_colored("[!] No matches found", Fore.YELLOW)

            except Exception as e:
                print_colored(f"Error processing URL {url}: {e}", Fore.RED)

    print_colored("\nThanks for using SwaggerSpy! Consider following me on X, GitHub and LinkedIn: @UndeadSec, https://github.com/UndeadSec, https://linkedin.com/in/alissonmoretto\n", Fore.MAGENTA)