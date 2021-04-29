import requests
import sys
import hashlib



def req_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code == 200:
        return res
    raise RuntimeError(f'something went wrong. Please check hash char. Status code = {res.status_code}')
    
def get_pw_leak_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for tail, count in hashes:
        if tail == hash_to_check:
            return count
    return 0

def pwd_api_check(passwords):
    
    sha1pw = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
    first_five, tail = sha1pw[:5], sha1pw[5:]
    response = req_api_data(first_five)
            
    return get_pw_leak_count(response, tail)

def main(pw_to_check):
    for pw in pw_to_check:
        count = pwd_api_check(pw) 
        if count == 0:
            print(f'{pw} is safe. Carry on!')
        else:
            print(f'{pw} has been pwned {count} times. Please choose another one.')

main(sys.argv[1:])

