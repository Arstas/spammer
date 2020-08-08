from b0mb3r.services.service import Service


class City24(Service):
    async def run(self):
        await self.post(
            "https://city24.ua/personalaccount/account/registration",
            data={"PhoneNumber": phone},
        )
