import setuptools


def choose_network_client(requires):
    import pkg_resources
    for req in requires:
        try:
            pkg_resources.require(req)
            return [req]
        except pkg_resources.DistributionNotFound:
            pass
        pass
    print "To use this app one of the following packages have to be installed - %s" % requires
    import os
    os._exit(os.EX_OK)
    pass

setuptools.setup(
    name="python-neutronclient_ext",
    version="0.0.1",
    author="anabelengp",
    author_email="anabelengp@gmail.com",
    url="https://github.com/anabelengp/python_neutronclient_ext.git",
    description="Neutron client extension example",
    license="",
    packages=["neutronclient_ext"],
    install_requires=choose_network_client(["python-neutronclient", "python-quantumclient"]),
    classifiers=[
        "Programming Language :: Python",
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'neutron = neutronclient_ext.shell:main',
        ]
    }

)
