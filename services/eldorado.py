from b0mb3r.services.service import Service


class Eldorado(Service):
    async def run(self):
        await self.post(
            "https://api.eldorado.ua/v1/sign/",
            params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"},
        )
