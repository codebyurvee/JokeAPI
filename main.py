import requests


class JokeAPI:
    def __init__(self, url: str) -> None:
        self.url = url
        self.last_joke: dict[str, str] | None = None

    def get_joke(self) -> None:
        response = requests.get(self.url, timeout=10)
        if response.status_code == 200:
            self.last_joke = response.json()
        else:
            raise RuntimeError(f"Error fetching joke: {response.status_code}")

    def print_joke(self) -> None:
        if self.last_joke is None:
            raise RuntimeError("Fetch a joke before printing it.")

        print(self.last_joke["setup"])
        print(self.last_joke["punchline"])


if __name__ == "__main__":
    joke_api = JokeAPI("https://official-joke-api.appspot.com/random_joke")
    joke_api.get_joke()
    joke_api.print_joke()