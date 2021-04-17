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

    def _get_results(self, endpoint: str, params: dict) -> dict:
        res = self.session.get(endpoint, params=params)
        res.raise_for_status()
        return res.json()

    @staticmethod
    def _date_to_str(d: date) -> str:
        return d.strftime('%Y-%m-%d')

    def get_events(self, after: Union[str, date], before: Optional[Union[str, date]] = None,
                   name: Optional[str] = None, tier: Optional[str] = None, region: Optional[str] = None,
                   mode: Optional[int] = None, sort: Optional[str] = None, order: Optional[str] = None,
                   page: Optional[int] = None, per_page: Optional[str] = None):
        endpoint = f'{API_BASE_URL}/events'
        params = {
            'after': self._date_to_str(after) if isinstance(after, date) else after,
            'per_page': '20' if per_page is None else per_page  # This option seems broken, setting it anyways
        }
        if before is not None:
            params['before'] = self._date_to_str(before) if isinstance(before, date) else before
        else:
            params['before'] = self._date_to_str(date.today())

        other_params = {'name', 'tier', 'region', 'mode', 'sort', 'order', 'page'}
        params |= {k: v for k, v in locals().items() if (k in other_params) and (v is not None)}

        results = self._get_results(endpoint, params).get('events')
        return results
