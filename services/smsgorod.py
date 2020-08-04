from b0mb3r.services.service import Service


class SMSGorod(Service):
    async def run(self):
        await self.post(
            "http://s
            msgorod.ru/sendsms.php",
            data={"number": phone},
        )
