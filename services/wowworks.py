from b0mb3r.services.service import Service


class WOWWOrks(Service):
    async def run(self):
        await self.post(
            "https://api.wowworks.ru/v2/site/send-code",
            json={"phone": phone, "type": 2},
        )
