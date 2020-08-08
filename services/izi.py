from b0mb3r.services.service import Service


class IZI(Service):
    async def run(self):
        await self.post(
            "https://izi.ua/api/auth/register",
            json={"phone": "+"+phone,"name": name,"is_terms_accepted": True},
        )
