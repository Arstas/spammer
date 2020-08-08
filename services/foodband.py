from b0mb3r.services.service import Service


class FoodBand(Service):
    async def run(self):
        await self.post(
            "https://foodband.ru/api/",
            params={"call": "customers/sendVerificationCode", "phone": phone, "g-recaptcha-response": ""},
        )
