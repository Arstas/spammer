from b0mb3r.services.service import Service


class Cabinet(Service):
    async def run(self):
        await self.post(
            "https://cabinet.wi-fi.ru/api/auth/by-sms",
            data={"msisdn": phone}, headers={"App-ID": "cabinet"},
        )
