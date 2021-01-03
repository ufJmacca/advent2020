#%%
import requests
import secrets
import re

#%%
header = {'cookie': secrets.cookie}

passport_start = requests.get('https://adventofcode.com/2020/day/4/input', headers = header)
# %%
passport_list = passport_start.text.split('\n\n')
print(re.split(' |\n', passport_list[0]))

# list of dicts
passport_dicts = [{j.split(':')[0]:j.split(':')[1] for j in re.split(' |\n', i) if len(j) > 0} for i in passport_list]
print(passport_dicts[0])

# %%
valid_passports = 0

for passport in passport_dicts:
    