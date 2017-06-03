URL = {
    'base': 'https://{proxy}.api.riotgames.com/{url}',
    'OPGG': 'https://api.champion.gg/v2/champions/{champID}/{champROLE}/matchups?elo={playerELO}&api_key={APIKEY}',
    'summoner_by_name': '/lol/summoner/v{version}/summoners/by-name/{names}',
    'static_data': '/lol/static-data/v{version}/champions',
    'matches_id': '/lol/match/v{version}/matches/{matchId}'
}

playerELO = {
    'noplayerELO': '',
    'yesplayerELO': '?elo={ELO}'
}

API_VERSIONS = {
    'summoner': '3',
    'static': '3',
    'match': '3'
}

REGIONS = {
    'north_america': 'na1',
    'europe_nordic_and_east': 'eun1',
    'europe_west': 'euw1'
}
