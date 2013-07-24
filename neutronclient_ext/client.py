

from neutronclient.v2_0.client import Client, APIParamsCall

@APIParamsCall
def create_zzz(self, body=None):
    """Create zzz client"""
    #return self.post(self.networks_path, body=body)
    return "ok"

Client.create_zzz = create_zzz
