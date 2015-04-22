# fifth-row-py
A Python module made to interface with The 5th Row sports data API

# Examples

To begin making requests to the API, create an object of the `FifthRow` class like so
```python
from fifth_row import FifthRow
f = FifthRow(sandbox=True)
```
The class defaults to the real API, but in this example we are using the sandboxed version.

Now that `f` has been instantiated, we can start making requests using `f.get()`
```python
matches = f.get(sport='nba', team='ny', status='upcoming')
```
Now `matches` is a list of `Matchup` objects. These objects hold all the data for every individual match that was returned by our request.

You can access a `Matchup` object's data by the attribute or by treating it like a dictionary
```python
print matches[0].status
# is the same as
print matches[0]['status']
```

Since the get method returns a list, the easiest way to extract each matches information is by iterating through them
```python
for match in matches:
  print match.status
  print match.home
  print match.away
```

And there you have it.
