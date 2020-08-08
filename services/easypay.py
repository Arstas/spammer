from b0mb3r.services.service import Service


class EasyPay(Service):
    async def run(self):
        await self.post(
            "https://api.easypay.ua/api/auth/register",
            json={"phone": phone, "password": _name},
        )
