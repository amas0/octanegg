from datetime import date
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

    @staticmethod
    def _date_to_str(d: date) -> str:
        return d.strftime('%Y-%m-%d')

    def _handle_date_params(self, before: Union[str, date, None], after: Union[str, date]) -> dict:
        out = {'after': self._date_to_str(after) if isinstance(after, date) else after}
        if before is not None:
            out['before'] = self._date_to_str(before) if isinstance(before, date) else before
        else:
            out['before'] = self._date_to_str(date.today())
        return out

    def get_events(self, after: Union[str, date], before: Optional[Union[str, date]] = None,
                   name: Optional[str] = None, tier: Optional[str] = None, region: Optional[str] = None,
                   mode: Optional[int] = None, sort: Optional[str] = None, order: Optional[str] = None,
                   page: Optional[int] = None, per_page: Optional[str] = '20') -> list:
        endpoint = f'{API_BASE_URL}/events'
        other_params = {'name', 'tier', 'region', 'mode', 'sort', 'order', 'page'}

        params = self._handle_date_params(before, after)
        params |= {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('events')
        return results

    def get_event(self, event_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/events/{event_id}'
        result = self._get_results(endpoint)
        return result

    def get_matches(self, after: Union[str, date], before: Optional[Union[str, date]] = None,
                    event: Optional[str] = None, stage: Optional[int] = None, substage: Optional[int] = None,
                    sort: Optional[str] = None, order: Optional[str] = None, page: Optional[int] = None,
                    per_page: Optional[str] = '20') -> list:
        endpoint = f'{API_BASE_URL}/matches'
        other_params = {'event', 'stage', 'substage', 'sort', 'order', 'page'}

        params = self._handle_date_params(before, after)
        params |= {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('matches')
        return results

    def get_match(self, match_id: str) -> dict:
        endpoint = f'{API_BASE_URL}/matches/{match_id}'
        result = self._get_results(endpoint)
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
