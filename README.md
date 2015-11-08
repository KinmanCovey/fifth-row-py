# fifth-row-py [![Build Status](https://travis-ci.org/KinmanCovey/fifth-row-py.svg?branch=master)](https://travis-ci.org/KinmanCovey/fifth-row-py)
A Python module made to interface with [The 5th Row](http://www.the5throw.com) sports data API

# Project Status
I started this project for two reasons:
  1. To support a great company with a great API and great service. They're doing God's work over there.
  2. To practice writing Pythonic programs (feel free to let me know how I did with that)

The project is still a work in progress and will be (hopefully) gaining new features in the near future. The unit tests currently only test a few things about the classes, but I will be writing more tests as I get the time.

# Examples

To begin making requests to the API, create an object of the `FifthRow` class like so
```python
from fifth_row import FifthRow
f = FifthRow()
```
The class defaults to the sandboxed API, so passing no parameters to the constructor is fine for experimenting.

Now that `f` has been instantiated, we can start making requests using `f.get()`
```python
matches = f.get(sport='nba', team='ny', status='upcoming')
```
`f.get()` returns a generator filled with `Matchup` objects. These objects hold all the data for every individual match that was returned by our request.

In the event that the API can't find any matchups that meet your request, the method will return a generator containing one `NoMatchup` object. The `NoMatchup` object has one attribute, `message`, that contains the response returned from the API.

The API response objects are similar to this (taken straight from their docs)
```javascript
{
  home: { team: ..., code: ... },
  away: { team: ..., code: ... },
  begins: { date: ..., time: ..., iso: ... },
  sport: ...,
  status: "upcoming"
}
```
The `Matchup` objects extract this data and store it in properly named attributes. For instance, the matches home team value can be found in the `Matchup` object at its attribute `home_team`. For the away team the value is stored in, you guessed it, the `away_team` attribute.

Since the `get` method returns a generator, the easiest way to extract each matches information is by iterating through them
```python
for match in FifthRow.get('nba'):
  print match.status
  print match.home
  print match.away
  if match.status is 'upcoming':
    print match.begin_date
```

And there you have it.
