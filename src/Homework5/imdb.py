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
                    source_dict[' '.join(line.split()[3:-1])] = line.split()[2:]
                line_count += 1
            top250_(source_dict)
            ratings_([i[0] for i in sorted(source_dict.values(), reverse=True)])
    except IOError:
        print("No file 'ratings.list'")


def write_file(file_name, str_):
    with open(os.path.join('data5', file_name), 'w+') as f:
        f.write(str_)


def top250_(source):
    str_250 = ''
    for key in source:
        str_250 += key + '\n'
    write_file('top250_movies.txt', str_250)


def ratings_(source):
    str_ratings = ''
    for i in sorted(set(source), reverse=True):
        str_ratings += i + ' ' + '*' * source.count(i) + str(source.count(i)) + '\n'
    write_file('ratings.txt', str_ratings)


read_imdb()
