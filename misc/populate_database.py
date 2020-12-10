import json
import requests
import sys

session = None

def read_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def get_request(prefix, request_info):
    pass

def post_request(prefix, request_info):
    for d in request_info['data']:
        r = requests.post(prefix + request_info['name'], json=d)

        if r.status_code not in [200, 201]:
            print("======== ERRO NO REQUEST {}\n\n".format(request_info['name']), r.content)
    

def main(args):
    global session
    
    config_file = read_json(args[1])
    session = requests.session()
    
    for r in config_file['requests']:
        if r['type'] == 'post':
            post_request(config_file['api_prefix'], r)
        elif r['type'] == 'get':
            continue
        else:
            continue
            

if __name__ == '__main__':
    main(sys.argv)
