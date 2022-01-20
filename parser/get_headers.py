import json

def get_headers(filename='headers/headers.txt'):
    headers = open(filename, 'r').read().split('\n')
    headers = [h for h in headers if h != ""]
    headers_json = {}
    for h in headers:
        if h[0] ==':': continue
        index = h.find(':')
        line = h 
        headers_json.update({
           line[0:index].strip() : line[index+1:].strip()
        })
    #with open(filename.split('.')[0]+'.json', 'w') as f:
    #    json.dump(headers_json, f, indent=4)
    return headers_json
    
if __name__ == '__main__':
    get_headers()
