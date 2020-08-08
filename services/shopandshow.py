from b0mb3r.services.service import Service


class ShopAndShow(Service):
    async def run(self):
        await self.post(
            "https://shopandshow.ru/sms/password-request/",
            data={"phone": "+" +phone, "resend": 0},
        )
