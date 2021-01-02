#%%
import requests
import secrets

header = {'cookie': secrets.cookie}

expenses = requests.get('https://adventofcode.com/2020/day/1/input', headers = header)
# %%
print(type(expenses.text))
# %%
expense_list = expenses.text.split('\n')

expense_list_ints = [int(i) for i in expense_list if len(i) > 0]
# %%
# challenge 1 2 numbers that add to 2020
for expense1 in expense_list_ints:
    for expense2 in expense_list_ints:
        if expense1 + expense2 == 2020:
            print(expense1*expense2)

# %%
# challenge 2 3 numbers that add to 2020
for expense1 in expense_list_ints:
    for expense2 in expense_list_ints:
        for expense3 in expense_list_ints:
            if expense1 + expense2 + expense3 == 2020:
                print(expense1*expense2*expense3)
# %%
