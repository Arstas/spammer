from b0mb3r.services.service import Service


class Imgur](Service):
    async def run(self):
        await self.post(
            "https://api.imgur.com/account/v1/phones/verify",
            json={"phone_number": phone, "region_code": "RU"},
        )
