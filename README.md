# octanegg

This library is a lightweight API client for [octane.gg](https://octane.gg), a site that provides
statistics on professional Rocket League.

This client implements the API endpoints and options defined 
at https://zsr.octane.gg/. At the time of writing, there seemed to 
be some bugs with the API where certain options are non-functioning. 

## Installation

```bash
git clone https://github.com/amas0/octanegg.git
pip install ./octanegg
```

## Example usage

```python
from octanegg import Octane

client = Octane()
matches_from_2021 = client.get_matches(after='2021-01-01')
```