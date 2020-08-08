from b0mb3r.services.service import Service


class SuAndShi(Service):
    async def run(self):
        await self.post(
            "https://suandshi.ru/mobile_api/register_mobile_user",
            params={"phone": phone},
        )
