from b0mb3r.services.service import Service


class Menu(Service):
    async def run(self):
        await self.post(
            "https://www.menu.ua/kiev/delivery/registration/direct-registration.html",
            data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password},
        )
