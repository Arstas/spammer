from b0mb3r.services.service import Service


class Sushifuji(Service):
    async def run(self):
        await self.post(
            "https://sushifuji.ru/sms_send_ajax.php",
            data={"name": "false", "phone": phone},
        )
