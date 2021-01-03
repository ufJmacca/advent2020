#%%
import requests
import secrets
import re

#%%
header = {'cookie': secrets.cookie}

passwords = requests.get('https://adventofcode.com/2020/day/2/input', headers = header)
# %%
# %%
password_list = passwords.text.split('\n')
print(password_list)
# %%
password_list_split = [i.split(': ') for i in password_list if len(i) > 0]
print(password_list_split)
# %%
# Part one count how many passwords match the policy
matches = 0

for policy, password in password_list_split:
    policy_range, policy_letter = policy.split(' ')
    occurences = password.count(policy_letter)
    min_occurences, max_occurences = policy_range.split('-')

    if int(min_occurences) <= occurences <= int(max_occurences):
        print(password, 'matches policy', policy)
        matches += 1

print(matches)
# %%
matches = 0

for policy, password in password_list_split:
    policy_range, policy_letter = policy.split(' ')
    first_position, second_position = policy_range.split('-')

    first_match = 1 if password[int(first_position) - 1] == policy_letter else 0
    second_match = 1 if password[int(second_position) - 1] == policy_letter else 0

    if first_match + second_match == 1:
        print(password, 'matches policy', policy)
        matches += 1

print(matches)
# %%

# %%
