from b0mb3r.services.service import Service


class MisterCash(Service):
    async def run(self):
        await self.post(
            "https://my.mistercash.ua/ru/send/sms/registration",
            params={"number": "+"+phone},
        )
