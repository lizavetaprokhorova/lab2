import csv

from typing import List

anime_table = []
with open('anime.csv', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        anime_table.append(row)

property_column_by_name = {anime_table[0][i]: i for i in range(len(anime_table[0]))}

FINISHED = 'Finished', bool
TAGS = 'Tags', list
CONTENT_WARNING = 'Content Warning', list
TYPE = 'Type', str
START_YEAR = 'StartYear', int
STUDIOS = 'Studios', list

print([row[property_column_by_name[TAGS[0]]] for row in anime_table][:10])
print([row[property_column_by_name[CONTENT_WARNING[0]]] for row in anime_table][:10])
print([row[property_column_by_name[STUDIOS[0]]] for row in anime_table][:10])

CRITERIAS = [FINISHED, TAGS, CONTENT_WARNING, TYPE, START_YEAR, STUDIOS]


def cast(string: str, type_: type):
    if type_ in (int, float, str, bool):
        return str(type_(string))
    elif type_ == list:
        return [e.strip() for e in string.split(',')]
    print("Error...")
    exit(0)


recommended_animes = anime_table[1:]
for criteria in CRITERIAS:
    answer = input(f"<<< What {criteria[0]} do you prefer? (found {len(recommended_animes)})\n>>> ")

    if answer == '':
        continue

    answer = cast(answer, criteria[1])

    chosen_animes = []
    for row in recommended_animes:
        if criteria[1] == list:
            for value in answer:
                if value in row[property_column_by_name[criteria[0]]]:
                    chosen_animes.append(row)
                    break
        else:
            if answer == row[property_column_by_name[criteria[0]]]:
                chosen_animes.append(row)

    recommended_animes = chosen_animes


for row in recommended_animes:
    try:
        row[property_column_by_name['Rating Score']] = float(row[property_column_by_name['Rating Score']])
    except:
        row[property_column_by_name['Rating Score']] = 0


recommended_animes.sort(key=lambda anime_row: anime_row[property_column_by_name['Rating Score']])


with open('Top.txt', 'w', encoding='utf-8') as file:
    if len(recommended_animes) > 10:
        for i in range(10):
            file.write(str(i + 1) + ' ' + recommended_animes[i][1] + '\n')
    else:
        for i in range(len(recommended_animes)):
            file.write(str(i + 1) + ' ' + recommended_animes[i][1] + '\n')
