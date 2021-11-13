"""Intacct Inter-Entity Account Mapper
Sage Intacct has great functionality to track due-to and due-from balances.
Thinking through the relationship isn't always obvious, so this can help.
Tags: Intacct, inter-entity"""

#! python3

import sys
import csv

print(
    r'''
    ___    ____       _    ___      __       ______          __  
   /   |  / / /_____ | |  / (_)____/ /_____ /_  __/__  _____/ /_ 
  / /| | / / __/ __ `/ | / / / ___/ __/ __ `// / / _ \/ ___/ __ \
 / ___ |/ / /_/ /_/ /| |/ / (__  ) /_/ /_/ // / /  __/ /__/ / / /
/_/  |_/_/\__/\__,_/ |___/_/____/\__/\__,_//_/  \___/\___/_/ /_/ 

'''
)

def export_file():
    try:
        with open('iet_config_dv_{}.csv'.format(iet_option), 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)
            writer.writerows(csv_data)
    except PermissionError:
        print("\nHey! Looks like you have our CSV open... that means we skip it!")
    except:
        print("\nSomething unexpected happened. No CSV created.")
    else:
        print(
            "\nThere! Made a CSV file as an example as a starting point. Find/Replace a few values and you're good to import."
        )
    with open('acct_listing_avt.txt', 'w', encoding='UTF8', newline='') as f:
        f.write('ACCOUNTS\n')
        for acct in acct_list:
            f.write('{}\n'.format(acct))

while True:
    print('Enter number of entities:')
    entities = input('> ').upper()
    if entities.isnumeric() is True:
        if int(entities) > 0:
            break
    else:
        if len(entities) == 0 or entities == 'QUIT':
            print('Quitting!')
            sys.exit()
entities = int(entities)
print('Great! Time to plan for inter-entity accounts!')


ENT_BASIC       = entities * 2
ENT_ADV2        = entities ** 2 - entities
ENT_ADV4        = entities * (entities - 1) * 2
ENT_BASIC_SIMP  = entities
ENT_ADV2_SIMP   = int((entities ** 2 - entities) / 2)


print(
    '''
We can set up Basic or Advanced. Many options exist for how to set up
relationships. 

For reference, with {0:,d} entities, you could have:
 - Basic: {1:,d} accounts (one payable and receivable acct per entity)
 - Advanced Two: {2:,d} accounts (one payable and receivable per entity pair)
 - Advanced Four: {3:,d} accounts (one payable and receivable per entity relationship)
 - Advanced Basic, single Bal Sheet acct: {4:,d} accounts
 - Advanced Four, single Bal Sheet acct: {2:,d} accounts
 - Advanced Two, single Bal Sheet acct: {5:,d} accounts
 - Advanced Simpifed Four: {1:,d} accounts

We find that this last option ("Advanced Simplified Four") is the best.

'''.format(
        entities, ENT_BASIC, ENT_ADV2, ENT_ADV4, ENT_BASIC_SIMP, ENT_ADV2_SIMP
    )
)
