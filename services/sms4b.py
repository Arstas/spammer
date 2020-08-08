from b0mb3r.services.service import Service


class SMS4B(Service):
    async def run(self):
        await self.post(
            "https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + phone, "ajax_demo_send": "1"},
        )
