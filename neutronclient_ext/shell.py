import sys

from neutronclient.openstack.common import strutils
from neutronclient.shell import NeutronShell, NEUTRON_API_VERSION, COMMAND_V2
from neutronclient.common import exceptions as exc

import client
from commands import CreateZzz

COMMAND_V2["zzz"] = CreateZzz

def main(argv=sys.argv[1:]):
    try:
        return NeutronShell(NEUTRON_API_VERSION).run(map(strutils.safe_decode,
                                                         argv))
    except exc.NeutronClientException:
        return 1
    except Exception as e:
        print unicode(e)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
