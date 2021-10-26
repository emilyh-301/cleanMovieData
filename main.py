# Emily Haigh
# This is a script to change this data for our project
# https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset
import csv

def clean_data():
    DataFile = "data/exampleMovies.csv"

    with open(DataFile, "r") as csvfile:
        DataCaptured = csv.DictReader(csvfile) # delimiter=',', skipinitialspace=True)
        Genres = set()
        for row in DataCaptured:
            lst = row["Genres"].split(",", 1)
            for g in lst:
                if g not in Genres:
                    Genres.add(g)

        print(Genres)
        print(len(Genres))

def output_new_file():
    new_file = "data/newMoviesFile.csv"
    old_file = "data/exampleMovies.csv"

    with open(old_file, "r") as oldcsvfile: #, new_file:
        reader = csv.DictReader(oldcsvfile)
        filename = ['Title', 'Director', 'Rating', 'Time', 'Tomatoes', 'Rom', 'Com', 'Western', 'Action', 'Adv']
        writer = csv.DictWriter(new_file, fieldnames=)
        writer.writeheader()

        for row in reader:
            print(row)
            writer.writerow({
                "Title": row["Title"],
                "Director": row["Director"],
                "Rating": row["Rating"],
                "Time": row["Time"],
                "Tomatoes": row["Tomatoes"],
                #if row["Genres"].split(",").contains("rom"):
                #    "Rom": "1",
            })


def get_col(genre):
    return 1

if __name__ == '__main__':
    output_new_file()

