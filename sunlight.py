from b0mb3r.services.service import Service


class Sunlight(Service):
    async def run(self):
        await self.post(
            "https://api.sunlight.net/v3/customers/authorization/", 
            data={"phone": phone},
        )
