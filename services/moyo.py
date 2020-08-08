from b0mb3r.services.service import Service


class Moyo(Service):
    async def run(self):
        await self.post(
            "https://www.moyo.ua/identity/registration",
            data={"firstname": name,"phone": phone,"email": email},
        )
