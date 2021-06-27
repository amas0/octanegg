from typing import Optional

import requests

API_BASE_URL = 'https://zsr.octane.gg'


class Octane:
    def __init__(self):
        self.session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_traceback):
        self.close()

    def close(self):
        self.session.close()

    def _get_results(self, endpoint: str, params: Optional[dict] = None) -> dict:
        res = self.session.get(endpoint, params=params)
        res.raise_for_status()
        return res.json()

    def get_events(self, name: Optional[str] = None, tier: Optional[str] = None, region: Optional[str] = None,
                   mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                   after: Optional[str] = None, date: Optional[str] = None, sort: Optional[str] = None,
                   order: Optional[str] = None, page: int = 1, per_page: int = 100) -> list:
        endpoint = f'{API_BASE_URL}/events'
        param_names = {'name', 'tier', 'region', 'mode', 'group', 'before', 'after', 'date', 'sort',
                       'order', 'page'}

        params = {'perPage': per_page}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('events')
        return results

    def get_event(self, event_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/events/{event_id}'
        result = self._get_results(endpoint)
        return result

    def get_event_matches(self, event_id: str) -> list:
        endpoint = f'{API_BASE_URL}/events/{event_id}/matches'
        result = self._get_results(endpoint).get('matches')
        return result

    def get_event_participants(self, event_id: str) -> list:
        endpoint = f'{API_BASE_URL}/events/{event_id}/participants'
        result = self._get_results(endpoint).get('participants')
        return result

    def get_matches(self, event: Optional[str] = None, stage: Optional[int] = None, qualifier: Optional[bool] = None,
                    tier: Optional[str] = None, region: Optional[str] = None, mode: Optional[int] = None,
                    group: Optional[str] = None, before: Optional[str] = None, after: Optional[str] = None,
                    best_of: Optional[int] = None, reverse_sweep: Optional[bool] = None,
                    reverse_sweep_attempt: Optional[bool] = None, player: Optional[str] = None,
                    team: Optional[str] = None, sort: Optional[str] = None, order: Optional[str] = None,
                    page: int = 1, per_page: int = 100) -> list:
        endpoint = f'{API_BASE_URL}/matches'
        param_names = {'event', 'stage', 'qualifier', 'tier', 'region', 'mode', 'group', 'before', 'after',
                       'player', 'team', 'sort', 'order', 'page'}

        params = {'bestOf': best_of, 'reverseSweep': reverse_sweep, 'reverseSweepAttempt': reverse_sweep_attempt,
                  'perPage': per_page}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('matches')
        return results

    def get_match(self, match_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/matches/{match_id}'
        result = self._get_results(endpoint)
        return result

    def get_match_games(self, match_id: str) -> list:
        endpoint = f'{API_BASE_URL}/matches/{match_id}/games'
        result = self._get_results(endpoint).get('games')
        return result

    def get_games(self, event: Optional[str] = None, stage: Optional[int] = None, match: Optional[str] = None,
                  qualifier: Optional[bool] = None, tier: Optional[str] = None, region: Optional[str] = None,
                  mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                  after: Optional[str] = None, best_of: Optional[int] = None,
                  player: Optional[str] = None, team: Optional[str] = None, sort: Optional[str] = None,
                  order: Optional[str] = None, page: int = 1, per_page: int = 100) -> list:
        endpoint = f'{API_BASE_URL}/games'
        param_names = {'event', 'stage', 'match', 'qualifier', 'tier', 'region', 'mode', 'group',
                       'before', 'after', 'player', 'team', 'sort', 'order', 'page'}

        params = {'bestOf': best_of, 'perPage': per_page}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('games')
        return results

    def get_game(self, game_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/games/{game_id}'
        result = self._get_results(endpoint)
        return result

    def get_players(self, tag: Optional[str] = None, country: Optional[str] = None,
                    team: Optional[str] = None, sort: Optional[str] = None, order: Optional[str] = None,
                    page: int = 1, per_page: int = 100) -> list:
        endpoint = f'{API_BASE_URL}/players'
        param_names = {'country', 'tag', 'team', 'sort', 'order', 'page'}

        params = {'perPage': per_page}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('players')
        return results

    def get_player(self, player_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/players/{player_id}'
        result = self._get_results(endpoint)
        return result

    def get_teams(self, name: Optional[str] = None, sort: Optional[str] = None,
                  order: Optional[str] = None, page: Optional[int] = None,
                  per_page: Optional[int] = 100) -> list:
        endpoint = f'{API_BASE_URL}/teams'
        param_names = {'name', 'sort', 'order', 'page'}

        params = {'perPage': per_page}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('teams')
        return results

    def get_team(self, team_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/teams/{team_id}'
        result = self._get_results(endpoint)
        return result

    def get_active_teams(self):
        endpoint = f'{API_BASE_URL}/teams/active'
        result = self._get_results(endpoint).get('teams')
        return result

    def get_player_records(self, type: str, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                           match: Optional[str] = None, qualifier: Optional[bool] = None, winner: Optional[bool] = None,
                           nationality: Optional[str] = None, tier: Optional[str] = None, region: Optional[str] = None,
                           mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                           after: Optional[str] = None, best_of: Optional[int] = None, player: Optional[str] = None,
                           team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/records/players'
        param_names = {'type', 'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier',
                       'region', 'mode', 'group', 'before', 'after', 'player', 'team'}

        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('records')
        return results

    def get_team_records(self, type: str, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                         match: Optional[str] = None, qualifier: Optional[bool] = None, winner: Optional[bool] = None,
                         nationality: Optional[str] = None, tier: Optional[str] = None, region: Optional[str] = None,
                         mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                         after: Optional[str] = None, best_of: Optional[int] = None,
                         team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/records/teams'
        param_names = {'type', 'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier',
                       'region', 'mode', 'group', 'before', 'after', 'player', 'team'}

        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('records')
        return results

    def get_game_records(self, event: Optional[str] = None, stage: Optional[int] = None, match: Optional[str] = None,
                         qualifier: Optional[bool] = None, tier: Optional[str] = None, region: Optional[str] = None,
                         mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                         after: Optional[str] = None, best_of: Optional[str] = None, player: Optional[str] = None,
                         team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/records/games'
        param_names = {'event', 'stage', 'match', 'qualifier', 'tier', 'region', 'mode', 'group',
                       'before', 'after', 'player', 'team'}

        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('records')
        return results

    def get_series_records(self, event: Optional[str] = None, stage: Optional[int] = None, match: Optional[str] = None,
                           qualifier: Optional[bool] = None, tier: Optional[str] = None, region: Optional[str] = None,
                           mode: Optional[int] = None, group: Optional[str] = None, before: Optional[str] = None,
                           after: Optional[str] = None, best_of: Optional[str] = None, player: Optional[str] = None,
                           team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/records/series'
        param_names = {'event', 'stage', 'match', 'qualifier', 'tier', 'region', 'mode', 'group',
                       'before', 'after', 'player', 'team'}

        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('records')
        return results

    def get_player_stats(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                         match: Optional[str] = None, qualifier: Optional[bool] = None,
                         winner: Optional[bool] = None, nationality: Optional[str] = None, tier: Optional[str] = None,
                         region: Optional[str] = None, mode: Optional[int] = None, group: Optional[str] = None,
                         before: Optional[str] = None, after: Optional[str] = None, best_of: Optional[int] = None,
                         player: Optional[str] = None, team: Optional[str] = None):
        endpoint = f'{API_BASE_URL}/stats/players'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'player', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_player_stats_by_team(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                                 match: Optional[str] = None, qualifier: Optional[bool] = None,
                                 winner: Optional[bool] = None, nationality: Optional[str] = None,
                                 tier: Optional[str] = None, region: Optional[str] = None, mode: Optional[int] = None,
                                 group: Optional[str] = None, before: Optional[str] = None, after: Optional[str] = None,
                                 best_of: Optional[int] = None, player: Optional[str] = None,
                                 team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/players/teams'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'player', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_player_stats_by_opponents(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                                      match: Optional[str] = None, qualifier: Optional[bool] = None,
                                      winner: Optional[bool] = None, nationality: Optional[str] = None,
                                      tier: Optional[str] = None, region: Optional[str] = None,
                                      mode: Optional[int] = None, group: Optional[str] = None,
                                      before: Optional[str] = None, after: Optional[str] = None,
                                      best_of: Optional[int] = None, player: Optional[str] = None,
                                      team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/players/opponents'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'player', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_player_stats_by_event(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                                  match: Optional[str] = None, qualifier: Optional[bool] = None,
                                  winner: Optional[bool] = None, nationality: Optional[str] = None,
                                  tier: Optional[str] = None, region: Optional[str] = None, mode: Optional[int] = None,
                                  group: Optional[str] = None, before: Optional[str] = None,
                                  after: Optional[str] = None, best_of: Optional[int] = None,
                                  player: Optional[str] = None, team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/players/events'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'player', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_team_stats(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                       match: Optional[str] = None, qualifier: Optional[bool] = None,
                       winner: Optional[bool] = None, nationality: Optional[str] = None, tier: Optional[str] = None,
                       region: Optional[str] = None, mode: Optional[int] = None, group: Optional[str] = None,
                       before: Optional[str] = None, after: Optional[str] = None, best_of: Optional[int] = None,
                       team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/teams'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_team_stats_by_opponents(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                                    match: Optional[str] = None, qualifier: Optional[bool] = None,
                                    winner: Optional[bool] = None, nationality: Optional[str] = None,
                                    tier: Optional[str] = None, region: Optional[str] = None,
                                    mode: Optional[int] = None, group: Optional[str] = None,
                                    before: Optional[str] = None, after: Optional[str] = None,
                                    best_of: Optional[int] = None,
                                    team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/teams/opponents'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results

    def get_team_stats_by_event(self, stat: str, event: Optional[str] = None, stage: Optional[int] = None,
                                match: Optional[str] = None, qualifier: Optional[bool] = None,
                                winner: Optional[bool] = None, nationality: Optional[str] = None,
                                tier: Optional[str] = None, region: Optional[str] = None, mode: Optional[int] = None,
                                group: Optional[str] = None, before: Optional[str] = None,
                                after: Optional[str] = None, best_of: Optional[int] = None,
                                team: Optional[str] = None) -> list:
        endpoint = f'{API_BASE_URL}/stats/teams/events'
        param_names = {'stat', 'event', 'stage', 'match', 'qualifier', 'winner', 'nationality', 'tier', 'region',
                       'mode', 'group', 'before', 'after', 'team'}
        params = {'bestOf': best_of}
        params |= {k: v for k, v in locals().items() if (k in param_names) and (v is not None)}

        results = self._get_results(endpoint, params).get('stats')
        return results
