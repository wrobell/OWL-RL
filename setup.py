from distutils.core import setup
setup(name="RDFClosure",
      description="RDFClosure Library",
      version="5.0.0",
      author="Ivan Herman",
      author_email="ivan@ivan-herman.net",
	  maintainer="Ivan Herman",
	  maintainer_email="ivan@ivan-herman.net",
      packages=['RDFClosure'],
	  requires=['rdflib(>=4.2.2)', 'rdflib_jsonld']
)

