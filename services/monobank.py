from b0mb3r.services.service import Service


class Monobank(Service):
    async def run(self):
        await self.post(
            "https://www.monobank.com.ua/api/mobapplink/send",
            data={"phone": "+"+phone},
        )
