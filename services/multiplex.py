from b0mb3r.services.service import Service


class MultiPlex(Service):
    async def run(self):
        await self.post(
            "https://auth.multiplex.ua/login",
            json={"login": phone},
        )
