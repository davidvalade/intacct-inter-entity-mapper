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
        with open('iet_config_avt.csv', 'w', encoding='UTF8', newline='') as f:
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


def import_file():
    print('Create a TXT file called "entitylist.txt" with one entity listed per line.')
    choice = input('Press enter to load or QUIT to stop: ').upper()
    if choice == 'QUIT':
        sys.exit()
    try:
        with open('entitylist.txt', 'r') as f:
            entity_list = f.readlines()
            entity_list = [line.rstrip() for line in entity_list]
    except FileNotFoundError:
        print('Sorry, "entitylist.txt" not found.')
        print('Create that file and try again.')
        sys.exit()
    return entity_list


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

# fmt: off
ENT_BASIC       = entities * 2
ENT_ADV2        = entities ** 2 - entities
ENT_ADV4        = entities * (entities - 1) * 2
ENT_BASIC_SIMP  = entities
ENT_ADV2_SIMP   = int((entities ** 2 - entities) / 2)
# fmt: on

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

print(
    '''For our entity list, either: 
 - (1) key entity numbers
 - (2) import a list of entity IDs
 - (3) use a dummy list to edit manually later
'''
)

while True:
    print('Pick a option listed (or "quit" to stop):')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    if response in ('1', '2', '3'):
        break
choice = int(response)

entity_list = []
if choice == 1:
    while True:
        if len(entity_list) == entities:
            break
        ent = input('Enter an entity ID (or "QUIT"): ')
        if ent.upper == 'QUIT':
            sys.exit()
        if ent in entity_list:
            print('Sorry, that entity was entered already.')
            print('As a reminder, the entities so far are:', ', '.join(entity_list))
            continue
        entity_list.append(ent)
elif choice == 2:
    entity_list = import_file()
elif choice == 3:
    entity_list = ['ENTITY{}'.format(x + 1) for x in range(entities)]

acct_list = []
ent_pairs = []
csv_header = ['ENTITY A', 'ENTITY B', 'ENTITY A IER', 'ENTITY A IEP', 'ENTITY B IER', 'ENTITY B IEP']
csv_data = []
for from_entity in entity_list:
    for to_entity in entity_list:
        if from_entity != to_entity:
            if 'Due from entity {}'.format(to_entity) not in acct_list:
                acct_list.append('Due from entity {}'.format(to_entity))
            if 'Due to entity {}'.format(to_entity) not in acct_list:
                acct_list.append('Due to entity {}'.format(to_entity))
            if 'Due from entity {}'.format(from_entity) not in acct_list:
                acct_list.append('Due from entity {}'.format(from_entity))
            if 'Due to entity {}'.format(from_entity) not in acct_list:
                acct_list.append('Due to entity {}'.format(from_entity))
            if '{}/{}'.format(from_entity, to_entity) not in ent_pairs:
                ent_pairs.append('{}/{}'.format(from_entity, to_entity))
                ent_pairs.append('{}/{}'.format(to_entity, from_entity))
                csv_data.append(
                    [
                        from_entity,
                        to_entity,
                        'Due from entity {}'.format(to_entity),
                        'Due to entity {}'.format(to_entity),
                        'Due from entity {}'.format(from_entity),
                        'Due to entity {}'.format(from_entity),
                    ]
                )
export_file()
