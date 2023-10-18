print('importing...')
print('')
from pandas import DataFrame as DataFrame
import os
os.system('mode con: cols=100 lines=800')
tags = [['None1', 0],
        ['None2', 0],
        ['AoE', 0], # 2
        ['DP-Recovery', 0], # 3
        ['Nuker', 1], # 4
        ['Starter', 0], # 5
        ['Crowd-Control', 2], # 6
        ['DPS', 0], # 7
        ['Robot', 0], # 8
        ['Summon', 2], # 9
        ['Debuff', 1], # 10
        ['Fast-Redeploy', 1], # 11
        ['Shift', 1], # 12
        ['Support', 1], # 13
        ['Defense', 0], # 14
        ['Healing', 0], # 15
        ['Slow', 0], # 16
        ['Survival', 0], # 17
        ['Caster', 0], # 18
        ['Sniper', 0], # 19
        ['Defender', 0], # 20
        ['Specialist', 1], # 21
        ['Guard', 0], # 22
        ['Supporter', 0], # 23
        ['Medic', 0], # 24
        ['Vanguard', 0], # 25
        ['Melee', 0], # 26
        ['Ranged', 0], # 27
        ['Senior', 2], # 28
        ['Top', 3]] # 29
operators_data = [
    [3, 'Phantom', [10, 6, 5, 20, 25, 28]],
    [3, 'Weedy', [11, 6, 5, 20, 25, 28]],
    [3, 'Ceobe', [6, 5, 17, 26, 28]],
    [3, 'Rosa', [6, 5, 18, 26, 28]],
    [1, 'Podenco', [15, 14, 22, 26]],
    [2, 'Tsukinogi', [12, 16, 22, 26, 27]],
    [2, 'Leonhardt', [1, 3, 17, 26, 27]],
    [2, 'Asbestos', [6, 13, 19, 25, 27]],
    [2, 'Elysium', [2, 12, 24, 25, 27]],
    [0, '12F', [4, 17, 26]],
    [0, 'Adnachiel', [6, 18, 26]],
    [0, 'Ansel', [14, 23, 26]],
    [0, 'Beagle', [13, 19, 25]],
    [0, 'Catapult', [1, 18, 26]],
    [0, 'Durin', [4, 17, 26]],
    [0, 'Fang', [2, 24, 25]],
    [0, 'Hibiscus', [14, 23, 26]],
    [0, 'Kroos', [6, 18, 26]],
    [0, 'Lava', [1, 17, 26]],
    [0, 'Melantha', [6, 16, 21, 25]],
    [0, 'Midnight', [6, 21, 25]],
    [0, 'Noir Corne', [4, 19, 25]],
    [0, 'Orchid', [15, 22, 26]],
    [0, 'Plume', [6, 2, 24, 25]],
    [0, 'Popukar', [1, 16, 21, 25]],
    [0, 'Rangers', [4, 18, 26]],
    [0, 'Spot', [13, 14, 19, 25]],
    [0, 'Steward', [6, 17, 26]],
    [0, 'Vanilla', [2, 24, 25]],
    [0, 'Yato', [4, 24, 25]],
    [1, 'Ambriel', [6, 15, 18, 26]],
    [1, 'Beehunter', [6, 21, 25]],
    [1, 'Cuora', [13, 19, 25]],
    [1, 'Dobermann', [6, 12, 21, 25]],
    [1, 'Earthspirit', [15, 22, 26]],
    [1, 'Estelle', [1, 16, 21, 25]],
    [1, 'Frostleaf', [15, 6, 21, 25]],
    [1, 'Gitano', [1, 17, 26]],
    [1, 'Gravel', [10, 13, 20, 25]],
    [1, 'Greyy', [1, 15, 17, 26]],
    [1, 'Gummy', [13, 14, 19, 25]],
    [1, 'Haze', [6, 9, 17, 26]],
    [1, 'Jessica', [6, 16, 18, 26]],
    [1, 'Matoimaru', [16, 6, 21, 25]],
    [1, 'Matterhorn', [13, 19, 25]],
    [1, 'May', [6, 15, 18, 26]],
    [1, 'Meteor', [6, 9, 18, 26]],
    [1, 'Mousse', [6, 21, 25]],
    [1, 'Myrrh', [14, 23, 26]],
    [1, 'Myrtle', [2, 14, 24, 25]],
    [1, 'Perfumer', [14, 23, 26]],
    [1, 'Purestream', [14, 12, 23, 26]],
    [1, 'Rope', [11, 20, 25]],
    [1, 'Scavenger', [2, 6, 24, 25]],
    [1, 'Shaw', [11, 20, 25]],
    [1, 'Cutter', [3, 6, 21, 25]],
    [1, 'Shirayuki', [1, 15, 18, 26]],
    [1, 'Sussurro', [14, 23, 26]],
    [1, 'Utage', [6, 16, 21, 25]],
    [1, 'Vermeil', [6, 18, 26]],
    [1, 'Vigna', [6, 2, 24, 25]],
    [2, 'Astesia', [6, 13, 21, 25, 27]],
    [2, 'Blue Poison', [6, 18, 26, 27]],
    [2, 'Broca', [1, 16, 21, 25, 27]],
    [-1, 'Castle-3', [12, 7, 21, 25]],
    [2, 'Shamare', [9, 22, 26, 27]],
    [2, 'Cliffheart', [11, 6, 20, 25, 27]],
    [2, 'Croissant', [13, 11, 19, 25, 27]],
    [2, 'Executor', [1, 18, 26, 27]],
    [2, 'FEeater', [11, 15, 20, 25, 27]],
    [2, 'Firewatch', [6, 3, 18, 26, 27]],
    [2, 'Glacus', [15, 5, 22, 26, 27]],
    [2, 'GreyThroat', [6, 18, 26, 27]],
    [2, 'Hung', [13, 14, 19, 25, 27]],
    [2, 'Indra', [6, 16, 21, 25, 27]],
    [2, 'Istina', [15, 6, 22, 26, 27]],
    [-1, 'Justice Knight', [12, 7, 18, 26]],
    [-1, 'Lancet-2', [14, 7, 23, 26]],
    [2, 'Leizi', [6, 17, 26, 27]],
    [2, 'Liskarm', [13, 6, 19, 25, 27]],
    [2, 'Manticore', [6, 16, 20, 25, 27]],
    [2, 'Mayer', [8, 5, 22, 26, 27]],
    [2, 'Meteorite', [1, 9, 18, 26, 27]],
    [2, 'Nearl', [13, 14, 19, 25, 27]],
    [2, 'Nightmare', [6, 14, 15, 17, 26, 27]],
    [2, 'Platinum', [6, 18, 26, 27]],
    [2, 'Pramanix', [9, 22, 26, 27]],
    [2, 'Project Red', [10, 5, 20, 25, 27]],
    [2, 'Provence', [6, 18, 26, 27]],
    [2, 'Ptilopsis', [14, 12, 23, 26, 27]],
    [2, 'Reed', [2, 6, 24, 25, 27]],
    [2, 'Sesa', [1, 9, 18, 26, 27]],
    [2, 'Silence', [14, 23, 26, 27]],
    [2, 'Specter', [1, 16, 21, 25, 27]],
    [2, 'Swire', [6, 12, 21, 25, 27]],
    [2, 'Texas', [2, 5, 24, 25, 27]],
    [-1, 'THRM-EX', [3, 7, 20, 25]],
    [2, 'Vulcan', [16, 13, 6, 19, 25, 27]],
    [2, 'Waai Fu', [10, 9, 20, 25, 27]],
    [2, 'Warfarin', [14, 12, 23, 26, 27]],
    [2, 'Zima', [2, 12, 24, 25, 27]],
    [3, 'Aak', [6, 12, 20, 26, 28]],
    [3, 'Bagpipe', [2, 6, 24, 25, 28]],
    [3, 'Blaze', [6, 16, 21, 25, 28]],
    [3, 'Chen', [3, 6, 21, 25, 28]],
    [3, 'Exusiai', [6, 18, 26, 28]],
    [3, 'Hellagur', [6, 16, 21, 25, 28]],
    [3, 'Hoshiguma', [6, 13, 19, 25, 28]],
    [3, 'Ifrit', [1, 9, 17, 26, 28]],
    [3, 'Magallan', [6, 12, 15, 22, 26, 28]],
    [3, 'Mostima', [1, 5, 12, 17, 26, 28]],
    [3, 'Nightingale', [12, 14, 23, 26, 28]],
    [3, 'Saria', [12, 13, 14, 19, 25, 28]],
    [3, 'Schwarz', [6, 18, 26, 28]],
    [3, 'Shining', [12, 14, 23, 26, 28]],
    [3, 'Siege', [2, 6, 24, 25, 28]],
    [3, 'SilverAsh', [6, 12, 21, 25, 28]],
    [3, 'Skadi', [6, 16, 21, 25, 28]]
]
operators_data.sort()
operators_data = [[x[0], x[1], [num + 1 for num in x[2]]] for x in operators_data]
operators_data = [[x[0], x[1], x[2] + [0] + [1]] for x in operators_data]
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
        tags2_range = tags_range[tag1_index+1:-1]
        for tag2_index in tags2_range:
            tags3_range = tags_range[tag2_index+1:]
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
    combinatory_data = [[[ops for ops in x[0] if ops not in [0, 1]], x[1], x[2] ] for x in combinatory_data]
    for point in combinatory_data:
        for i, tag in enumerate(point[0]):
            point[0][i] = tags[tag][0]
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
