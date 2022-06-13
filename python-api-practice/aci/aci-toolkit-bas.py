import creds
from acitoolkit.acitoolkit import *

def main():
    sesh = Session(creds.URL,creds.LOGIN,creds.PASSWORD,subscription_enabled=False)
    sesh.login()
    ten = Tenant("PS_Toolkit_Tenant")
    sus_app = AppProfile('sus_app',ten)
    sus_db = EPG('sus_db_epg',sus_app)
    sus_web = EPG('sus_web_epg',sus_app)
    sus_web_contract = Contract("sus_contact",ten)
    sus_web.consume(sus_web_contract)
    sus_db.provide(sus_web_contract)
    ten.push_to_apic(sesh)

if __name__ == "__main__":
    main()