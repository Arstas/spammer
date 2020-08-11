from b0mb3r.services.service import Service


class Space(Service):
    async def run(self):
        await self.post(
            "https://smart.space/api/users/request_confirmation_code/",
            json={"mobile": "+" +phone, "action": "confirm_mobile"},
        )
