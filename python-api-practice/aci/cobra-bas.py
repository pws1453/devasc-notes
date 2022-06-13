from cobra.mit.access import MoDirectory
from cobra.mit.session import LoginSession
from cobra.mit.request import ConfigRequest
from cobra.model.fv import Tenant
import creds

loginSession = LoginSession(creds.URL, creds.LOGIN, creds.PASSWORD)
moDir = MoDirectory(loginSession)
moDir.login()
# universe directory
uniMo = moDir.lookupByDn('uni')
fvTenantMo = Tenant(uniMo,'cobra_tenant')
cfgReq = ConfigRequest()
cfgReq.addMo(fvTenantMo)
moDir.commit(cfgReq)