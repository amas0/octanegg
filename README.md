# octanegg

This library is a lightweight API client wrapper for [octane.gg](https://octane.gg), a site that provides
statistics on professional Rocket League.

This client implements the API endpoints and options defined 
at https://zsr.octane.gg/. 

It is recommended to have the above documentation open to consult while writing queries. There are a number of options
available for filtering the results of your queries that may not be obvious, such as the appropriate format of event
tiers/regions, that the documentation helps with.

For questions about API usage, the [Octane.gg discord](https://t.co/aikJXkBPQG?amp=1) is a great resource.

## Installation

Simply install the package via pip:

```bash
pip install octanegg
```

## Example usage

Here are a few example queries that could be useful.

#### Counting active teams

A simple one is looking at the currently active teams in the scene. This can be easily accomplished
with the `get_active_teams()` method. Let's answer the questions: how many active teams are there? and 
which region has the most active teams?


```python
from collections import Counter
from octanegg import Octane

with Octane() as client:
    active_teams = client.get_active_teams()
    num_active_teams = len(active_teams)
    region_counts = Counter(team.get('team').get('region') for team in active_teams)

print(f'There are {num_active_teams} currently active teams.')
print('The number of active teams per region is: ')
print(region_counts.most_common())
```

At the time of writing this documentation this outputs:

```
There are 147 currently active teams.
The number of active teams per region is: 
[('EU', 56), ('NA', 40), ('OCE', 25), ('SAM', 14), ('ASIA', 5), ('ME', 5), (None, 2)]
```

We can easily see that EU and NA are the most active regions following by OCE and SAM.

#### Pulling all S-tier 2021 NA games

Perhaps we are interested in exploring how the NA scene played out at the highest level
in 2021. One way we can do so is to look at all the "S-tier" (RLCS level events) games,
which we can pull using the `get_games()` method. For this example, we'll include games 
until the end of RLCS X, which was on 2021-06-20.

An important fact to keep in mind is that the Octane API will paginate the results of
certain queries. So, for retrieving this game data, we need to loop over pages of results.

The below snippet collects all the games we are interested in.

```python
from octanegg import Octane

with Octane() as client:
    games = []
    page = 1
    while True:
        current_page_games = client.get_games(tier='S', region='NA', after='2021-01-01',
                                              before='2021-06-20', page=page)
        if not current_page_games:  # no more games
            break
        games += current_page_games
        page += 1
```

We can use these results to answer simple questions like who played the most games in this time period.

```python
from collections import Counter
from itertools import chain

num_games = len(games)
blue_players = ([player.get('player').get('tag') for player in game.get('blue').get('players')] for game in games)
orange_players = ([player.get('player').get('tag') for player in game.get('orange').get('players')] for game in games)
players = list(chain.from_iterable(blue_players)) + list(chain.from_iterable(orange_players))
player_counts = Counter(players)

print(f'In our time window, there were {num_games} NA S-tier games.')
print(f'The 6 most seen players were: ')
print(player_counts.most_common(6))
```

Our results from running this are:

```
In our time window, there were 304 NA S-tier games.
The 6 most seen players were: 
[('Firstkiller', 82), ('Turinturo', 82), ('Taroco.', 82), ('Squishy', 80), ('GarrettG', 80), ('jstn.', 80)]
```

In this pull we see the rosters of Rogue and NRG played the most S-tier games in the first half of 2021.

These two examples are relatively simple data pulls and there is much more one can do with the API. The best way to 
explore it is to dig in and use it.
