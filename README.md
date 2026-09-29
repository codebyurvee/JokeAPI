# JokeAPI

A small Python project that fetches a random joke from the Official Joke API
using a reusable `JokeAPI` class.

## Requirements

- Python 3.11+
- `requests`

## Run the project

Install the dependency:

```bash
pip install requests
```

Run the program:

```bash
python3 main.py
```

Example output:

```text
Where do programmers like to hangout?
The Foo Bar.
```

## How it works

`JokeAPI` stores the API URL and the last fetched joke:

```python
from main import JokeAPI

joke_api = JokeAPI("https://official-joke-api.appspot.com/random_joke")
joke_api.get_joke()
joke_api.print_joke()
```