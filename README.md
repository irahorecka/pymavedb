# pymavedb

A simple [MaveDB API](https://mavedb.org/api/) wrapper.

## Installation

<em>There is currently no installation method, as the MaveDB team is discussing a proper PyPI library name.</em>

## Background

`pymavedb` is a very lightweight object-oriented wrapper for the Mave database REST API.

The interface maintains a low level of abstraction, extending `requests.models.Response` methods such as `get()`, `post()`, `delete()`, etc.

This library should entirely supplant the necessity to make raw HTTP requests to the MaveDB API.

## Examples

```python
from mavedb import MaveDB

# Providing an authorization token is optional.
mavedb_session = MaveDB(auth_token="my-auth-token")

# Get score sets with universal resource name (URN).
scoreset_urn_00000040_a_4 = mavedb_session.scoresets(urn="urn:mavedb:00000040-a-4")
# .get() is a requests.models.Response object, so you may add arguments as you would with requests.get().
print(scoreset_urn_00000040_a_4.get().json())
```

```python
>>> {'abstract_text': 'This study measured the effect of variants in yeast HSP90 '
                  'under different combinations of temperature (30C or 36C) '
                  'and presence/absence of salt (0.5 M NaCl). The results '
                  'explore the adaptive potential of this essential gene.',
 'contributors': ['0000-0003-1474-605X'],
 [...],
 'variant_count': 189}
```

## Contribute

- [Issues Tracker](https://github.com/irahorecka/pymavedb/issues)
- [Source Code](https://github.com/irahorecka/pymavedb/tree/main/mavedb)

## Support

If you are having issues or would like to propose a new feature, please use the [issues tracker](https://github.com/irahorecka/pymavedb/issues).

## License

The project is licensed under the MIT license.
