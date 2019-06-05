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

def all_titles(albums):
    all_titles = []
    for album in albums:
        all_titles.append(album['album'])
    return all_titles
#print(all_titles(top_albums))

def all_artists(albums):
    all_artists = []
    for album in albums:
        all_artists.append(album['artist'])
    return all_artists
print(all_artists(top_albums))

#def artist_most_albums(artists):
    freq = {}
    for artist in artists: 
        if artist in freq:
            freq[artist] += 1
        else:
            freq[artist] = 1
    for 

#we want to take in the list (top_albums) and loop through the data to see how many albums are by each artist 
#--> make a new list with nested dictionaries with this categorization 
#[{'artist': artist name, 'number of songs': number of songs}, repeat]
#sort our new list by number of albums and choose the highest one