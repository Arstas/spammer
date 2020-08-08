from b0mb3r.services.service import Service


class Kaspi(Service):
    async def run(self):
        await self.post(
            "https://kaspi.kz/util/send-app-link",
            data={"address": phone},
        )
