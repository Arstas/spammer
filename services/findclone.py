from b0mb3r.services.service import Service


class FindClone(Service):
    async def run(self):
        await self.post(
            "https://findclone.ru/register",
            params={"phone": "+" + phone},
        )
