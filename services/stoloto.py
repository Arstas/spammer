from b0mb3r.services.service import Service


class StoLoto(Service):
    async def run(self):
        await self.post(
            "https://www.stoloto.ru/send-mobile-app-link",
            data={"phone": phone},
        )
