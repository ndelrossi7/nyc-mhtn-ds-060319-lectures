def find_by_name(name, albums):  
    for album in albums:
        if name == album['album']:
            return album
    return None
#print(find_by_name('hello world', top_albums))

def find_by_rank(rank, albums):
    for album in albums:
        if rank == album['number']:
            return album['album']
    return None
#print(find_by_rank('1', top_albums))

def find_by_year(year, albums):
    list_by_year = []
    for album in albums:
        if year == album['year']:
            list_by_year.append(album['album'])
    return list_by_year
#print(find_by_year('1966', top_albums))

def find_by_years(start_year, end_year, albums):
    list_by_years = []
    for album in albums:
        if int(start_year) <= int(album['year']) and int(end_year) >= int(album['year']):
            list_by_years.append(album['album'])
    return list_by_years
#print(find_by_years('1966', '1972', top_albums))

def find_by_ranks(start_rank, end_rank, albums):
    list_by_ranks = []
    for album in albums: 
        if int(start_rank) <= int(album['number']) and int(end_rank) >= int(album['number']):
            list_by_ranks.append(album['album'])
    return list_by_ranks
#print(find_by_ranks('1', '5', top_albums))

def all_titles():
    all_titles = []
    for album in top_albums:
        all_titles.append(album['album'])
    return all_titles
#print(all_titles(top_albums))

def all_artists():
    all_artists = []
    for album in top_albums:
        all_artists.append(album['artist'])
    return all_artists
#print(all_artists(top_albums))

def artist_most_albums():
    album_count = {}
    for index in range(0, len(all_artists())): 
        if all_artists()[index] in album_count:
            album_count[all_artists()[index]] += 1
        else: 
            album_count[all_artists()[index]] = 1
    max_albums = max(album_count.values())
    max_albums_artists = []
    for k, v in album_count.items():
        if v == max_albums:
            max_albums_artists.append(k)
    return max_albums_artists

def most_pop_word():
    all_titles_1 = all_titles()
    joined_words = ' '.join(all_titles_1)
    split_words = joined_words.split(' ')
    word_count = {}
    for index in range(0, len(split_words)):
        if split_words[index] in word_count:
            word_count[split_words[index]] += 1
        else:
            word_count[split_words[index]] = 1
    max_words = max(word_count.values())
    max_words_v = []
    for k, v in word_count.items():
        if v == max_words:
            max_words_v.append(k)
    return max_words_v

def most_pop_word_alt():
    all_words = []
    for album in top_albums:
        all_words += album['album'].split()
    from collections import Counter
    return Counter([word.lower() for word in all_words]).most_common(1)

#the following requires an install and import of plotly:
#!pip install plotly==3.3.0
#import plotly
#plotly.offline.init_notebook_mode(connected=True)
def hist_album_decade():
    fifties = len(find_by_years('1950', '1959', top_albums))
    sixties = len(find_by_years('1960', '1969', top_albums))
    seventies = len(find_by_years('1970', '1979', top_albums))
    eighties = len(find_by_years('1980', '1989', top_albums))
    nineties = len(find_by_years('1990', '1999', top_albums))
    thousands = len(find_by_years('2000', '2009', top_albums))
    tens = len(find_by_years('2010', '2019', top_albums))
    decades = [fifties, sixties, seventies, eighties, nineties, thousands, tens]
    labels = ['fifties', 'sixties', 'seventies', 'eighties', 'nineties', 'thousands', 'tens']
    trace0 = {'type': 'bar', 'x': labels, 'y': decades }
    return plotly.offline.iplot([trace0])

#the following requires an install and import of matplotlib:
#from matplotlib import pyplot as plt
#%matplotlib inline
def hist_albums_decade_alt():
    return plt.hist([int(a['year'][:-1] + '0') for a in top_albums], bins = [1950,1960,1970,1980,1990,2000,2010])
hist_albums_dec_alt()   