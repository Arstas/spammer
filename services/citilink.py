from b0mb3r.services.service import Service


class Citilink(Service):
    async def run(self):
        await self.post(
            "https://www.citilink.ru/registration/confirm/phone/+"
            + phone + "/",
        )
