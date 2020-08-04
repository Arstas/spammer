from b0mb3r.services.service import Service


class BelkaCar(Service):
    async def run(self):
        await self.post(
            "https://belkacar.ru/get-confirmation-code",
            data={"phone": phone}, headers={},
        )
