import httpx


class WBHttpClient:
    def __init__(self, token: str, base_url: str = "https://seller-api.wildberries.ru") -> None:
        self.token = token
        self.base_url = base_url.rstrip("/")

    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": self.token,
            "Content-Type": "application/json",
        }

    async def get(self, path: str, params: dict | None = None) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.base_url}/{path.lstrip('/')}",
                headers=self._headers(),
                params=params,
                timeout=30,
            )
            response.raise_for_status()
            return response.json()

    async def post(self, path: str, json_data: dict | None = None) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/{path.lstrip('/')}",
                headers=self._headers(),
                json=json_data or {},
                timeout=30,
            )
            response.raise_for_status()
            return response.json()
