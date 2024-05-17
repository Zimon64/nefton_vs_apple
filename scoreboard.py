import pandas as pd
from datetime import datetime

score_list = pd.read_csv('score_list.csv')

now = datetime.now()

name_input = input('Gebe deinen Namen ein: ')
name = str(name_input)
score = 420


def scoreboard(name, score):
    current_time = now.strftime('%Y-%m-%d %H:%M:%S')

    if name in score_list['Name'].values:
        current_index = score_list.index[score_list['Name'] == name].tolist()[0]
        if score_list.at[current_index, 'Score'] < score:
            score_list.at[current_index, 'Score'] = score
            score_list.at[current_index, 'Date'] = current_time

    else:
        current_score = [int(len(score_list) + 1), name, score, current_time]
        score_list.loc[len(score_list)] = current_score

    score_list.sort_values(['Score', 'Date'], inplace=True, ascending=[False, True])
    score_list['Nr.'] = sorted(score_list['Nr.'])

    top_ten = score_list[score_list['Nr.'] <= 10]
    max_score = score_list.loc[score_list['Score'].idxmax()]

    return score_list, top_ten, max_score


score_list, top_ten, max_score = scoreboard(name, score)

# print('personal high score:')
# print(score_list[score_list['Name'] == name].to_string(index=False))
#  print('\nhigh score:')
# print(max_score)
print('\ntop 10 leaderboard')
print(top_ten.to_string(index=False))

score_list.to_csv('score_list.csv', index=False)
