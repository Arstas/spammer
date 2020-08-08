from b0mb3r.services.service import Service


class Hmara(Service):
    async def run(self):
        await self.post(
            "https://api.hmara.tv/stable/entrance",
           params={"contact": phone},
        )
