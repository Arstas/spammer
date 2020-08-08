from b0mb3r.services.service import Service


class Dianet(Service):
    async def run(self):
        await self.post(
            "https://my.dianet.com.ua/send_sms/",
            data={"phone": phone},
        )
