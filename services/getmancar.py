from b0mb3r.services.service import Service


class GetManCar(Service):
    async def run(self):
        await self.post(
            "https://crm.getmancar.com.ua/api/veryfyaccount",
            json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"},
        )
