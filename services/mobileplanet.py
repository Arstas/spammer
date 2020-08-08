from b0mb3r.services.service import Service


class MobilePlanet(Service):
    async def run(self):
        await self.post(
            "https://mobileplanet.ua/register",
            data={"klient_name": name,"klientphone": "+" + phone,"klient_email": email},
        )
