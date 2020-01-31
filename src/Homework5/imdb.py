"""В файле хранятся данные с сайта IMDB.
Скопированные данные хранятся в файле ./data5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов,
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.
"""

import os


def read_imdb():
    try:
        with open(os.path.join('data5', 'ratings.list')) as file:
            line_count, source_dict = 1, {}
            for line in file:
                if 29 <= line_count < 279:
                    source_dict[' '.join(line.split()[3:-1])] = [line.split()[2], line.split()[-1].strip('()')]
                line_count += 1
            top250_(source_dict.keys(), 'top250_movies.txt')
            ratings_and_years_([i[0] for i in source_dict.values()], 'ratings.txt')
            ratings_and_years_([i[-1] for i in source_dict.values()], 'years.txt')
    except OSError:
        print("No file 'ratings.list'")


def write_file_(str_, name_file):
    with open(os.path.join('data5', name_file), 'w+') as f:
        f.write(str_)


def top250_(source, name_file):
    str_250 = ''
    for key in source:
        str_250 += key + '\n'
    write_file_(str_250, name_file)


def ratings_and_years_(source, name_file):
    str_r_y = ''
    for i in sorted(set(source), reverse=True):
        rank, rank = 0, source.count(i)
        str_r_y += i + '\t' + '}' * rank + str(rank) + '\n'
    write_file_(str_r_y, name_file)


read_imdb()
