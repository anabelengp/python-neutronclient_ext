import logging
from neutronclient.neutron import v2_0 as neutronV20

class CreateZzz(neutronV20.CreateCommand):
    """Create zzz things"""

    resource = 'zzz'
    log = logging.getLogger(__name__ + '.CreateZzz')
