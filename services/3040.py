from b0mb3r.services.service import Service


class taxi(Service):
    async def run(self):
        await self.post(
            "https://3040.com.ua/taxi-ordering",
            data={"callback-phone": phone},
        )
