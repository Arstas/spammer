from b0mb3r.services.service import Service


class SBIS(Service):
    async def run(self):
        await self.post(
            "https://online.sbis.ru/reg/service/",
            json={"jsonrpc":"2.0", "protocol":"5", "method":"Пользователь.ЗаявкаНаФизика", "params":{"phone":phone}, "id":"1"},
        )
