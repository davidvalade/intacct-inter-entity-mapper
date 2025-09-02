"""Intacct Inter-Entity Account Mapper
Sage Intacct has great functionality to track due-to and due-from balances.
Thinking through the relationship isn't always obvious, so this can help.
Tags: Intacct, inter-entity
"""

#! python3

import sys
import csv

BAR = chr(9608)  # █

print(
    r'''

  __    _ ____    ____    ____    _____   ______
 \  \  //|    \  |    |  |    \  |     \ |   ___|
  \  \// |     \ |    |_ |     \ |      \|   ___|
   \__/  |__|\__\|______||__|\__\|______/|______|

 
'''
)


def export_file():
    """Exports the results to two files. One is a list of accounts, the other
    is a CSV file suitable for import."""
    try:
        with open('iet_config_vs.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(csv_header)
            writer.writerows(csv_data)
    except PermissionError:
        print('\nHey! Looks like you have our CSV open... skipping!')
    except Exception as e:
        print(f'\nUnexpected error ({e}). No CSV created.')
    else:
        print('\nCreated CSV file as a starting point. Find/Replace a few values and you\'re good to import.')

    with open('acct_listing_vs.txt', 'w', encoding='UTF8', newline='') as f:
        f.write('ACCOUNTS\n')
        f.writelines(f'{acct}\n' for acct in sorted(acct_set))


def import_file():
    """If selected, a user can import a TXT file called entitylist.txt for a list."""
    print('Create a TXT file called "entitylist.txt" with one entity per line.')
    choice = input('Press Enter to load or QUIT to stop: ').strip().upper()
    if choice == 'QUIT':
        sys.exit()
    try:
        with open('entitylist.txt', 'r') as f:
            entity_list = [line.strip() for line in f if line.strip()]
            entity_list = sorted(set(entity_list))  # Deduplicate + sort
    except FileNotFoundError:
        print('Sorry, "entitylist.txt" not found.\nCreate that file and try again.')
        sys.exit()
    return entity_list


def getProgressBar(progress, total, barWidth=40):
    """Returns a progress bar string with barWidth segments."""
    progress = max(0, min(progress, total))
    numBars = int((progress / total) * barWidth)

    percent = round(progress / total * 100, 1)
    return f"[{BAR * numBars}{' ' * (barWidth - numBars)}] {percent}% {progress}/{total}"


while True:
    entities = input('Enter number of entities (or QUIT): ').strip().upper()
    if entities == 'QUIT' or not entities:
        print('Quitting!')
        sys.exit()
    if entities.isnumeric() and int(entities) > 0:
        entities = int(entities)
        break

print('Great! Time to plan for inter-entity accounts!')

ENT_BASIC = entities * 2
ENT_ADV2 = entities ** 2 - entities
ENT_ADV4 = entities * (entities - 1) * 2
ENT_BASIC_SIMP = entities
ENT_ADV2_SIMP = (entities ** 2 - entities) // 2

print(f'''
We can set up Basic or Advanced. Many options exist.

For reference, with {entities:,} entities, you could have:
 - Basic: {ENT_BASIC:,} accounts
 - Advanced Two: {ENT_ADV2:,} accounts
 - Advanced Four: {ENT_ADV4:,} accounts
 - Advanced Basic, single Bal Sheet acct: {ENT_BASIC_SIMP:,} accounts
 - Advanced Four, single Bal Sheet acct: {ENT_ADV2:,} accounts
 - Advanced Two, single Bal Sheet acct: {ENT_ADV2_SIMP:,} accounts
 - *** Advanced Simplified Four: {ENT_BASIC:,} accounts

We find that this last option ("Advanced Simplified Four") is the best.
''')

print('''For our entity list, either: 
 - (1) key entity numbers
 - (2) import a list of entity IDs
 - (3) use a dummy list to edit manually later
''')

while True:
    response = input('Pick an option (1, 2, 3) or QUIT: ').strip().upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    if response in ('1', '2', '3'):
        choice = int(response)
        break

if choice == 1:
    entity_list = []
    while len(entity_list) < entities:
        ent = input('Enter an entity ID (or QUIT): ').strip()
        if ent.upper() == 'QUIT':
            sys.exit()
        if ent in entity_list:
            print(f'Sorry, "{ent}" already entered.\nEntities so far: {", ".join(entity_list)}')
            continue
        entity_list.append(ent)
elif choice == 2:
    entity_list = import_file()
else:
    entity_list = [f'ENTITY{x+1}' for x in range(entities)]

acct_set = set()
ent_pair_set = set()
csv_data = []
csv_header = ['ENTITY A', 'ENTITY B', 'ENTITY A IER', 'ENTITY A IEP', 'ENTITY B IER', 'ENTITY B IEP']

counter = 0
for entity_a in entity_list:
    for entity_b in entity_list:
        if entity_a == entity_b:
            continue

        acct_set.add(f'Due from entity {entity_b}')
        acct_set.add(f'Due to entity {entity_b}')
        acct_set.add(f'Due from entity {entity_a}')
        acct_set.add(f'Due to entity {entity_a}')

        pair = (entity_a, entity_b)
        rev_pair = (entity_b, entity_a)
        if pair not in ent_pair_set and rev_pair not in ent_pair_set:
            ent_pair_set.update([pair, rev_pair])
            csv_data.append([
                entity_a,
                entity_b,
                f'Due from entity {entity_b}',
                f'Due to entity {entity_b}',
                f'Due from entity {entity_a}',
                f'Due to entity {entity_a}',
            ])
            counter += 1
            barStr = getProgressBar(counter, ENT_ADV2_SIMP)
            print(f'\r{barStr}', end='', flush=True)

print()
export_file()
