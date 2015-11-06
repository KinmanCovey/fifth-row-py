#!usr/env/bin python
'''
Python module for The 5th Row Sports Data API
Made by Kinman Covey

BREAKDOWN:

    FifthRow - the main class for the api. create an object of this class to
    start using the API.

        .get - the method to make requests. returns a list of Matchup objects

    Matchup - a class made to represent a matchup retrieved from the API
    endpoint. extracts values from the dictionary and stores them in easy to
    access attributes.

'''
import json
from httplib import HTTPConnection
from contextlib import closing

class TokenError(Exception):
    pass

class FifthRow:

    def __init__(self, sandbox=True, token=None):
        self.sandbox = sandbox

        if self.sandbox is False:
            self.url = 'api.the5throw.com'
            if token is None:
                raise TokenError('token parameter must be a valid token')
            else:
                self.token = str(token)
                
        elif self.sandbox is True:
            self.url = 'sandbox.the5throw.com'
            self.token = 'sandbox'
        else:
            raise TypeError('sandbox parameter must be a boolean')

    # all purpose get method for the API calls.
    # returns a dict of matches
    def get(self, sport=None, team=None, status=None):
        #check parameters and start building the api request
        url_request = ''

        if sport is not None:
            url_request += '/' + str(sport)

        if team is not None:
            url_request += '/' + str(team)

        if status is not None:
            url_request += '/' + str(status)

        # make the HTTP request to the API with the request url
        with closing(HTTPConnection(self.url)) as conn:
            conn.connect()
            headers = {'Content-Type' : 'application/x-www-form-urlencoded'}
            param = 'token=' + self.token

            conn.request('POST', url_request, param, headers)
            resp = conn.getresponse()

            data = json.load(resp, 'UTF-8')
            conn.close()
            
            matchups = []

            if isinstance(data, dict):
                if 'message' in data:
                    matchup = NoMatchup(data)
                else:
                    matchup = Matchup(data)
                
                matchups.append(matchup)

            else:
                for entry in data:
                    matchup = Matchup(entry)
                    matchups.append(matchup)
                        
        return matchups

class NoMatchup:

    def __init__(self, dict_):

        self._data = dict_
        self.message = dict_['message']

    def __getitem__(self, key):
        return self._date[key]

class Matchup:

    def __init__(self, dict_):

        self._data = dict_
        self.status = str(dict_['status'])
        self.sport = str(dict_['sport'])
        self.home_team = str(dict_['home']['team'])
        self.home_code = str(dict_['home']['code'])
        self.away_team = str(dict_['away']['team'])
        self.away_code = str(dict_['away']['code'])
        self.begins_date = None
        self.begins_time = None
        self.begins_iso = None
        self.winner = None
        self.winner_code = None
        self.point_difference = None
        self.home_score = None
        self.away_score = None
        self.time_remaining = None

        if self.status is 'upcoming':
            self.begin_date = str(dict_['begins']['date'])
            self.begin_time = str(dict_['begins']['time'])
            self.begin_iso = str(dict_['begins']['iso'])
        elif self.status is 'final':
            self.winner = str(dict_['winner']['team'])
            self.winner_code = str(dict_['winner']['code'])
            self.point_difference = str(dict_['winner']['difference'])
        elif self.status is 'active':
            self.home_score = str(dict_['home']['score'])
            self.away_score = str(dict_['away']['score'])
            self.time_remaining = str(dict_['remaining'])
            
    def __getitem__(self, key):
        return self._data[key]
