python-neutronclient_ext
==================================

This is an example about how to extend neutron client. It allows using the same command for the extended features along with the usual neutron options.

This extension is autodiscovered once installed. To use:

    pip install python_openappsclient
    neutron zzz

To use it inside horizon (from python):

    pip install python_openappsclient

in your python module:

    from neutronclient.v2_0.client import Client
    from neutronclient_ext import client

First, import the neutron Client. Second, override the client to extend it with the new commands.

TODO
====

WORKING ON: complete the compatibility with quantum (the setup is already prepared to require either neutron or quantum).

