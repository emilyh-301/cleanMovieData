# Emily Haigh
# This is a script to change this data for our project
# https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset
import csv

def clean_data():
    DataFile = "path to my file"
    DataCaptured = csv.reader(DataFile, delimiter=',', skipinitialspace=True)

    Genres = set()
    for row in DataCaptured:
        if row[6] not in Genres:
            Genres.add(row[6])

    print(Genres)

def output_new_file():
    new_file = ""
    old_file = ""
    old_data = csv.reader(old_file, delimiter=',', skipinitialspace=True)
    new_data = csv.writer(new_file, ',')

    #we need the number of cols for the genres

    for row in new_data:
        genres = list(old_data[row][6])
        for g in genres:
            new_data[row][get_col(g)] = '1'

def get_col(genre):
    return 1

if __name__ == '__main__':
    clean_data()



