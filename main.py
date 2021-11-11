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
    new_file = "data/IMDbMoviesCleaned.csv"
    old_file = "data/IMDbMovies.csv"
    #temp_file = NamedTemporaryFile(delete = False)

    with open(new_file, "w") as new_file:
        reader = csv.DictReader(open(old_file))
        fieldnames = ['imdb_title_id', 'title', 'original_title', 'description', 'Action', 'Adult', 'Adventure',
                      'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy',
                      'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Reality-TV', 'News',
                      'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            desc = row['description'].split(' ')
            if len(desc) < 11:
                continue

            lst = set()
            lstgenres = row["genre"].split(",")
            for g in lstgenres:
                if g.strip not in lst:
                    lst.add(g.strip())
            rom = 0
            com = 0
            western = 0
            action = 0
            adv = 0
            adult = 0
            animation = 0
            bio = 0
            crime = 0
            doc = 0
            drama = 0
            fam = 0
            fantasy = 0
            filmnoir = 0
            history = 0
            horror = 0
            music = 0
            mystery = 0
            realitytv = 0
            news = 0
            scifi = 0
            sport = 0
            war = 0
            thriller = 0
            if "Adult" in lst: adult = 1
            if "Romance" in lst: rom = 1
            if "Comedy" in lst: com = 1
            if "Western" in lst: western = 1
            if "Action" in lst: action = 1
            if "Adventure" in lst: adv = 1
            if "Animation" in lst: animation = 1
            if "Biography" in lst: bio = 1
            if "Crime" in lst: crime = 1
            if "Documentary" in lst: doc = 1
            if "Drama" in lst: drama = 1
            if "Family" in lst: fam = 1
            if "Fantasy" in lst: fantasy = 1
            if "Film-Noir" in lst: filmnoir = 1
            if "History" in lst: history = 1
            if "Horror" in lst: horror = 1
            if "Music" in lst: music = 1
            if "Musical" in lst: music = 1
            if "Mystery" in lst: mystery = 1
            if "Reality-TV" in lst: realitytv = 1
            if "News" in lst: news = 1
            if "Sci-Fi" in lst: scifi = 1
            if "Sport" in lst: sport = 1
            if "War" in lst: war = 1
            if "Thriller" in lst: thriller = 1

            if realitytv == 1 or news == 1:
                continue

            writer.writerow({
                "imdb_title_id": row["imdb_title_id"],
                "title": row["title"],
                "original_title": row["original_title"],
                "description": row["description"],
                "Action": action,
                "Adult": adult,
                "Adventure": adv,
                'Animation': animation,
                'Biography': bio,
                "Comedy": com,
                'Crime': crime,
                'Documentary': doc,
                'Drama': drama,
                'Family': fam,
                'Fantasy': fantasy,
                'Film-Noir': filmnoir,
                'History': history,
                'Horror': horror,
                'Music': music,
                'Mystery': mystery,
                "Romance": rom,
                'Sci-Fi': scifi,
                'Sport': sport,
                'Thriller': thriller,
                'War': war,
                "Western": western,
            })

def get_col(genre):
    return 1

if __name__ == '__main__':
    print("start of program")
    output_new_file()

