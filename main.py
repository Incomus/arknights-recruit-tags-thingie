print('importing...')
print('')
from pandas import DataFrame as DataFrame
import os
import json
import requests

def load_json(repo_url, json_path):
    url = f"{repo_url}/raw/main/{json_path}"
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.text)
        return data

git_url = 'https://github.com/Incomus/arknights-recruit-tags-thingie'

tags = load_json(git_url, 'tags.json')
operators_data = load_json(git_url, 'operators.json')

operators_data.sort()
operators_data = [[x[0], x[1], [num + 1 for num in x[2]]] for x in operators_data]
operators_data = [[x[0], x[1], x[2] + [0] + [1]] for x in operators_data]
os.system('mode con: cols=100 lines=800')

while True:
    user_input = input('Debug? 0/1\n')
    if user_input in ('1', '0'):
        break
    os.system('cls')
    print('Invalid input')
    continue
debug = int(user_input)

def comb_tags(tags, operators_data, input_tags, debug=debug):
    combinatory_data = []
    tags_range = range(len(input_tags))
    tags1_range = [0, *tags_range[2:-2]]
    for tag1_index in tags1_range:
        tags2_range = tags_range[tag1_index + 1:-1]
        for tag2_index in tags2_range:
            tags3_range = tags_range[tag2_index + 1:]
            for tag3_index in tags3_range:
                if debug == 1:
                    if input_tags[tag1_index] == 0 and input_tags[tag2_index] == 1:
                        print_tags = input_tags[tag3_index] - 1
                    elif input_tags[tag1_index] in [0, 1]:
                        print_tags = [input_tags[tag2_index] - 1, input_tags[tag3_index] - 1]
                    else:
                        print_tags = [input_tags[tag1_index] - 1, input_tags[tag2_index] - 1,
                                      input_tags[tag3_index] - 1]
                    print('picked', print_tags)
                operators_var = []
                rarity_var = []
                match = False
                for operator_index in range(len(operators_data)):
                    if input_tags[tag1_index] in operators_data[operator_index][2] and \
                            input_tags[tag2_index] in operators_data[operator_index][2] and \
                            input_tags[tag3_index] in operators_data[operator_index][2]:
                        match = True
                        if operators_data[operator_index][0] == 0:
                            if debug == 1:
                                print(f'skipped {print_tags}: matched low rar {operators_data[operator_index][1]}')
                            break
                        if tag1_index == 0 and \
                                tag2_index == 1 and \
                                input_tags[tag3_index] == 29:
                            if debug == 1:
                                print(f'skipped {print_tags}: skip single top op')
                            break
                        if operators_data[operator_index][0] == -1:
                            if debug == 1:
                                print('skipped robot')
                            continue
                        if operators_data[operator_index][0] == 3 and \
                                input_tags[tag1_index] != 29 and \
                                input_tags[tag2_index] != 29 and \
                                input_tags[tag3_index] != 29:
                            if debug == 1:
                                print(f'skipped {operators_data[operator_index][1]}: 6* without top op')
                            continue
                        if rarity_var and min(rarity_var) < operators_data[operator_index][0]:
                            if debug == 1:
                                print(f'skipped {operators_data[operator_index][1]}: higher rarity than min')
                            continue
                        bads = 0
                        for point in combinatory_data:
                            point = [[x for x in point[0] if x not in [0, 1]], point[1], point[2]]
                            if set(point[0]).issubset({input_tags[tag1_index], input_tags[tag2_index],
                                                       input_tags[tag3_index]}):
                                for op in point[2]:
                                    op_tags = [row for row in operators_data if row[1] == op][0][2]
                                    if {input_tags[tag1_index], input_tags[tag2_index],
                                        input_tags[tag3_index]}.issubset(op_tags):
                                        bads = 1
                        if bads == 1:
                            if debug == 1:
                                print(f'skipped {operators_data[operator_index][1]}: is subset')
                            continue
                        operators_var.append(operators_data[operator_index][1])
                        rarity_var.append(operators_data[operator_index][0])
                        if debug == 1:
                            print(f'added {print_tags}: {operators_data[operator_index][1]} is good to go')
                if rarity_var:
                    combinatory_var = [[input_tags[tag1_index], input_tags[tag2_index], input_tags[tag3_index]],
                                       min(rarity_var), operators_var]
                    combinatory_data.append(combinatory_var)
                else:
                    if debug == 1 and match is False:
                        print('no matches')
    combinatory_data = [[[ops for ops in x[0] if ops not in [0, 1]], x[1], x[2]] for x in combinatory_data]
    for point in combinatory_data:
        for i, tag in enumerate(point[0]):
            point[0][i] = tags[tag]
    combinatory_df = DataFrame(combinatory_data, columns=['Tags', 'Rarity', 'Operators'])
    return combinatory_df


def call_menu(type):
    if type == 1:
        print('1 - Run a test with your tags, showing all operators')
        print('2 - Display all combinations')
        print('3 - Quit')
    if type == 2:
        os.system('cls')
        print('Robots desirable? (y/n)')
    if type == 3:
        os.system('cls')
        print(tags_df[1:].reset_index(drop=True)[1:])
        print('')
        print('Choose your tag indexes, input negative index to remove tag, - to remove last index')
        print('')
        print('Tags taken:', user_tags[:])

os.system('cls')
call_menu(1)
while True:
    user_input = input('Select option\n')
    try:
        user_input = int(user_input)
    except ValueError:
        os.system('cls')
        call_menu(1)
        print('Invalid input')
        continue
    if user_input == 3:
        break
    elif user_input == 2:
        os.system('cls')
        print('All non Top Operator combinations')
        print('')
        df = comb_tags(tags, operators_data, range(len(tags[:-2])))
        print(df)
        print('')
        call_menu(1)
        continue
    elif user_input == 1:
        call_menu(2)
        while True:
            user_input = input('Select option\n')
            if user_input in ('y', 'n', '1', '0', ''):
                break
            call_menu(2)
            print('Invalid input')
        if user_input == 'y' or user_input == '1' or user_input == '':
            robot_rar = 2
        else:
            robot_rar = -1
        for operator_index in range(len(operators_data)):
            if 8 in operators_data[operator_index][2]:
                operators_data[operator_index][0] = robot_rar
        tags_df = DataFrame(tags, columns=['Tag', 'Rarity'])
        user_tags = []
        call_menu(3)
        while True:
            while len(user_tags) < 5:
                while True:
                    user_input = input(f'Input tag index # {len(user_tags)+1}: \n')
                    if user_input == '-' and len(user_tags) > 0:
                        user_tags.remove(user_tags[-1])
                        call_menu(3)
                        continue
                    if user_input == '-' and len(user_tags) < 1:
                        call_menu(3)
                        print('No tags to remove')
                        continue
                    try:
                        user_input = int(user_input)
                    except ValueError:
                        call_menu(3)
                        print('Invalid input')
                        continue
                    if user_input in user_tags:
                        call_menu(3)
                        print('Tag index already taken')
                        continue
                    if -user_input in user_tags:
                        user_tags.remove(-user_input)
                        call_menu(3)
                        continue
                    if user_input in range(29)[1:]:
                        break
                    call_menu(3)
                    print('Invalid input')
                user_tags.append(user_input)
                call_menu(3)
            os.system('cls')
            print('Final tags:', user_tags)
            user_tags = [num + 1 for num in user_tags]
            user_tags.append(0)
            user_tags.append(1)
            user_tags.sort()
            df = comb_tags(tags, operators_data, user_tags)
            print('')
            print('Keep in mind, rarity 3 operators can only be rolled with Top Operator tag,'
                  ' not sure about rarity 2 operators'
                  ' and Senior Operator tag')
            print('')
            if df.empty:
                print("------>We ain't found nothin'<------")
            else:
                print(df)
            print('')
            while True:
                print('Run again with same robot rarity? (y/n)')
                user_input = input()
                if user_input in ('y', 'n', '1', '0', ''):
                    break
            if user_input == 'y' or user_input == '1' or user_input == '':
                user_tags = []
                call_menu(3)
                continue
            else:
                os.system('cls')
                call_menu(1)
                break
    else:
        os.system('cls')
        call_menu(1)
        print('invalid input')
