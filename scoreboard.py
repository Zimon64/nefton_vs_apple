import pandas as pd
from datetime import datetime

def scoreboard(name, score):
    try:
        score_list = pd.read_csv('score_list.csv', encoding='utf-8')
    except FileNotFoundError:
        # If the file doesn't exist, create a new DataFrame
        score_list = pd.DataFrame(columns=['Nr.', 'Name', 'Score', 'Date'])

    now = datetime.now()
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
    score_list['Nr.'] = range(1, len(score_list) + 1)

    top_ten = score_list.head(10)
    max_score = score_list.loc[score_list['Score'].idxmax()]

    score_list.to_csv('score_list.csv', index=False)

    return score_list, top_ten, max_score

if __name__ == "__main__":
    name = input('Enter your name: ')
    score = int(input('Enter your score: '))
    score_list, top_ten, max_score = scoreboard(name, score)
    print(top_ten.to_string(index=False))
