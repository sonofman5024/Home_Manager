import requests
import sys
import hashlib
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _


class  PwnedValidator(object):

    def __init__(self, max_pwned_times=10):
        self.max_pwned_times = max_pwned_times

    def req_api_data(self, query_char):
        url = 'https://api.pwnedpasswords.com/range/' + query_char
        res = requests.get(url)
        if res.status_code == 200:
            return res
        raise RuntimeError(f'something went wrong. Please check hash char. Status code = {res.status_code}')
        
    def get_pw_leak_count(self, hashes, hash_to_check):
        hashes = (line.split(':') for line in hashes.text.splitlines())
        for tail, count in hashes:
            if tail == hash_to_check:
                return count
        return 0

    def pwd_api_check(self, passwords):
        
        sha1pw = hashlib.sha1(passwords.encode('utf-8')).hexdigest().upper()
        first_five, tail = sha1pw[:5], sha1pw[5:]
        response = self.req_api_data(first_five)
                
        return self.get_pw_leak_count(response, tail)

    def main(self, pw_to_check):
        for pw in pw_to_check:
            return self.pwd_api_check(pw) 
            # if count == 0:
            #     print(f'{pw} is safe. Carry on!')
            # else:
            #     print(f'{pw} has been pwned {count} times. Please choose another one.')

    def validate(self, password, user=None):
        if int(self.main([password])) > self.max_pwned_times:
            raise ValidationError(
                _("This password has been pwned at most %(pwned_times)d times. You need a stronger password"),
                code='password_over_pwned',
                params={'pwned_times': int(self.main([password]))},
            )

    def get_help_text(self):
        return _(
            "This password must not been pwned over %(max_pwned_times)d times."
            % {'max_pwned_times': self.max_pwned_times}
        )

if __name__ == "__main__":
    validator = PwnedValidator()
    validator.validate('1234')