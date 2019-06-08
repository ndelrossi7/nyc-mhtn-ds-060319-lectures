game_dict = {'home': {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players': {'Alan Anderson': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 22,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 1
                                        },
                                        'Reggie Evans': {
                                            'number': 30,
                                            'shoe': 14,
                                            'points': 12,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 12,
                                            'blocks': 12,
                                            'slam_dunks': 7
                                        },
                                        'Brook Lopez': {
                                            'number': 11,
                                            'shoe': 17,
                                            'points': 17,
                                            'rebounds': 19,
                                            'assists': 10,
                                            'steals': 3,
                                            'blocks': 1,
                                            'slam_dunks': 15
                                        },
                                        'Mason Plumlee': {
                                            'number': 1,
                                            'shoe': 19,
                                            'points': 26,
                                            'rebounds': 12,
                                            'assists': 6,
                                            'steals': 3,
                                            'blocks': 8,
                                            'slam_dunks': 5
                                        },
                                        'Jason Terry': {
                                            'number': 31,
                                            'shoe': 15,
                                            'points': 19,
                                            'rebounds': 2,
                                            'assists': 2,
                                            'steals': 4,
                                            'blocks': 11,
                                            'slam_dunks': 1
                                        }
                                        }},
                    'away': {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players': {'Jeff Adrien': {
                                            'number': 4,
                                            'shoe': 18,
                                            'points': 10,
                                            'rebounds': 1,
                                            'assists': 1,
                                            'steals': 2,
                                            'blocks': 7,
                                            'slam_dunks': 2
                                        },
                                        'Bismak Biyombo': {
                                            'number': 0,
                                            'shoe': 16,
                                            'points': 12,
                                            'rebounds': 4,
                                            'assists': 7,
                                            'steals': 7,
                                            'blocks': 15,
                                            'slam_dunks': 10
                                        },
                                        'DeSagna Diop': {
                                            'number': 2,
                                            'shoe': 14,
                                            'points': 24,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 4,
                                            'blocks': 5,
                                            'slam_dunks': 5
                                        },
                                        'Ben Gordon': {
                                            'number': 8,
                                            'shoe': 15,
                                            'points': 33,
                                            'rebounds': 3,
                                            'assists': 2,
                                            'steals': 1,
                                            'blocks': 1,
                                            'slam_dunks': 0
                                        },
                                        'Brendan Haywood': {
                                            'number': 33,
                                            'shoe': 15,
                                            'points': 6,
                                            'rebounds': 12,
                                            'assists': 12,
                                            'steals': 22,
                                            'blocks': 5,
                                            'slam_dunks': 12
                                        }}}}


def num_points_scored(name):
    for line in game_dict: 
        if name in game_dict['home']['players'].keys():
            return game_dict['home']['players'][name]['points']
        else:
            return game_dict['away']['players'][name]['points']

def shoe_size(name):
    for line in game_dict: 
        if name in game_dict['home']['players'].keys():
            return game_dict['home']['players'][name]['shoe']
        else:
            return game_dict['away']['players'][name]['shoe']
        
def team_colors(team):
    for line in game_dict:
        if team in game_dict['home']['team_name']:
            return game_dict['home']['colors']
        else:
            return game_dict['away']['colors']

def team_names():
    team_names = []
    for team in game_dict.keys():
        team_names.append(game_dict[team]['team_name'])
    return team_names

def player_numbers(team):
    numbers = []
    if team in game_dict['home']['team_name']:
        for player in game_dict['home']['players'].values():
            numbers.append(player['number'])
    else:
        for player in game_dict['away']['players'].values():
            numbers.append(player['number'])
    return numbers
    
def player_stats(name):
    for line in game_dict:
        if name in game_dict['home']['players']:
            return game_dict['home']['players'][name]
        else:
            return game_dict['away']['players'][name]

def big_shoe_rebounds():
    players = []
    for team in game_dict.keys():
        for key in game_dict[team]['players'].keys():
            players.append(key)
    size = 0
    name = ' '
    for player in players:
        temp = shoe_size(player)
        if temp > size:
            size = temp
            name = player
    player_stat = player_stats(name)
    return player_stat['rebounds']

# bonus

def most_points_scored():
    players = []
    for team in game_dict.keys():
        for key in game_dict[team]['players'].keys():
            players.append(key)
    size = 0
    name = ' '
    for player in players:
        temp = num_points_scored(player)
        if temp > size:
            size = temp
            name = player
    return name

def winning_team():
    home_team = game_dict['home']['players']
    away_team = game_dict['away']['players']
    score_home = sum([num_points_scored(x) for x in home_team])
    score_away = sum([num_points_scored(x) for x in away_team])
    if score_home > score_away:
        return game_dict['home']['team_name']
    else: 
        return game_dict['away']['team_name']