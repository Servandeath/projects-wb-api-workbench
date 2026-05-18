class SessionKeyStorage:
    def __init__(self) -> None:
        self._tokens: dict[str, str] = {}

    def save_token(self, key_name: str, token: str) -> None:
        if not key_name:
            raise ValueError("Key name is required")

        if not token:
            raise ValueError("Token is required")

        self._tokens[key_name] = token

    def get_token(self, key_name: str) -> str | None:
        return self._tokens.get(key_name)

    def delete_token(self, key_name: str) -> None:
        self._tokens.pop(key_name, None)

    def clear(self) -> None:
        self._tokens.clear()
