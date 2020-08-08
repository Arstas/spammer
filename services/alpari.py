from b0mb3r.services.service import Service


class Alpari(Service):
    async def run(self):
        await self.post(
            "https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/",
            json={"client_type": "personal", "email": _email, "mobilephone": phone, "deliveryOption": "sms"},
        )
