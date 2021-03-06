import creds
import acitoolkit

def main():
    sesh = acitoolkit.acitoolkit.Session(creds.URL,creds.LOGIN,creds.PASSWORD,subscription_enabled=False)
    sesh.login()
    ten = acitoolkit.acitoolkit.Tenant("PS_Toolkit_Tenant")
    sus_app = acitoolkit.acitoolkit.AppProfile('sus_app',ten)
    sus_db = acitoolkit.acitoolkit.EPG('sus_db_epg',sus_app)
    sus_web = acitoolkit.acitoolkit.EPG('sus_web_epg',sus_app)
    sus_web_contract = acitoolkit.acitoolkit.Contract("sus_contact",ten)
    sus_web.consume(sus_web_contract)
    sus_db.provide(sus_web_contract)
    ten.push_to_apic(sesh)

if __name__ == "__main__":
    main()