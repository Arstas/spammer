from b0mb3r.services.service import Service


class PanPizza(Service):
    async def run(self):
        await self.post(
            "https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",
            data={"telephone": "8" + phone9},
        )
