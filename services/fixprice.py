from b0mb3r.services.service import Service


class FixPrice(Service):
    async def run(self):
        await self.post(
            "https://fix-price.ru/ajax/registerphone_code.php",
            data={"register_call": "Y", "action": "getCode", "phone": "+" + phone},
        )
