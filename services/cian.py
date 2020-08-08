from b0mb3r.services.service import Service


class CIAN(Service):
    async def run(self):
        await self.post(
            "https://api.cian.ru/sms/v1/send-validation-code/",
            json={"phone": "+" + phone, "type": "authenticateCode"},
        )
