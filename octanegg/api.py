from typing import Optional, Union

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
                   order: Optional[str] = None, page: int = 1, per_page: int = 50) -> list:
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
                    page: int = 1, per_page: int = 50) -> list:
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

    def get_games(self, event: Optional[str] = None, match: Optional[str] = None,
                  sort: Optional[str] = None, order: Optional[str] = None, page: Optional[int] = None,
                  per_page: Optional[str] = '20') -> list:
        endpoint = f'{API_BASE_URL}/games'
        other_params = {'event', 'match', 'sort', 'order', 'page'}
        params = {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('games')
        return results

    def get_game(self, game_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/games/{game_id}'
        result = self._get_results(endpoint)
        return result

    def get_players(self, country: Optional[str] = None, tag: Optional[str] = None,
                    team: Optional[str] = None, sort: Optional[str] = None, order: Optional[str] = None,
                    page: Optional[int] = None, per_page: Optional[str] = '20') -> list:
        endpoint = f'{API_BASE_URL}/players'
        other_params = {'country', 'tag', 'team', 'sort', 'order', 'page'}

        params = {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('players')
        return results

    def get_player(self, player_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/players/{player_id}'
        result = self._get_results(endpoint)
        return result

    def get_teams(self, name: Optional[str] = None, sort: Optional[str] = None,
                  order: Optional[str] = None, page: Optional[int] = None,
                  per_page: Optional[str] = '20') -> list:
        endpoint = f'{API_BASE_URL}/teams'
        other_params = {'name', 'sort', 'order', 'page'}

        params = {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('teams')
        return results

    def get_team(self, team_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/teams/{team_id}'
        result = self._get_results(endpoint)
        return result
