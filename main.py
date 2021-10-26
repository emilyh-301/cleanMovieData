# Emily Haigh
# This is a script to change this data for our project
# https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset
import csv
import shutil
from base64 import encode
from tempfile import NamedTemporaryFile


def clean_data():
    DataFile = "data/IMDbMovies.csv"
    x = 0
    with open(DataFile, "r") as csvfile:
        DataCaptured = csv.DictReader(csvfile) # delimiter=',', skipinitialspace=True)
        Genres = set()
        for row in DataCaptured:
            lst = row["genre"].split(",")
            #x = x + 1
            for g in lst:
                if g.strip() not in Genres:
                    Genres.add(g.strip())

        print(sorted(Genres))
        print(len(Genres))
        #print(x)

def output_new_file():
    new_file = "data/newMoviesFile.csv"
    old_file = "data/exampleMovies.csv"
    temp_file = NamedTemporaryFile(delete = False)

    with open(old_file, "rb") as oldcsvfile, temp_file:
        reader = csv.DictReader(oldcsvfile)
        fieldnames = ['Title', 'Director', 'Rating', 'Time', 'Tomatoes', 'rom', 'com', 'western', 'action', 'adv']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        #writer.writeheader()

        for row in reader:
            #print(row)
            lst = row["genre"].split(",")

            # for g in lst:
            #     writer.writerow({
            #         g: row["Title"],
            #     })

            writer.writerow({
                "Title": row["Title"],
                "Director": row["Director"],
                "Rating": row["Rating"],
                "Time": row["Time"],
                'Tomatoes': row["Tomatoes"],

                # 'Action': "",
                # 'Adult': "",
                # 'Adventure': "",
                # 'Animation': "",
                # 'Biography': "",
                # 'Comedy': "",
                # 'Crime': "",
                # 'Documentary': "",
                # 'Drama': "",
                # 'Family': "",
                # 'Fantasy': "",
                # 'Film-Noir': "",
                # 'History': "",
                # 'Horror': "",
                # 'Music': "",
                # 'Musical': "",
                # 'Mystery': "",
                # 'News': "",
                # 'Reality-TV': "",
                # 'Romance': "",
                # 'Sci-Fi': "",
                # 'Sport': "",
                # 'Thriller': "",
                # 'War': "",
                # 'Western': ""

            })
    shutil.move(temp_file.name, "data/newMoviesFile.csv")


def get_col(genre):
    return 1

if __name__ == '__main__':
    print(type("1".encode("ascii")))
    output_new_file()

