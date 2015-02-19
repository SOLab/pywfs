import string

from paver.easy import *
from paver.setuputils import *
import paver.doctools
from paver.release import setup_meta

__version__ = (0,0,1)

options = environment.options
setup(**setup_meta)

options(
    setup=Bunch(
        name='pywfs',
        version='.'.join(str(d) for d in __version__),
        description='WFS request handler',
        long_description='''
pywfs is a library that can handle WFS requests.
        ''',
        keywords='wfs features opendap dods dap data science climate oceanography meteorology',
        classifiers=filter(None, map(string.strip, '''
            Development Status :: 5 - Production/Stable
            Environment :: Web Environment
            Framework :: Paste
            Intended Audience :: Developers
            Intended Audience :: Science/Research
            License :: OSI Approved :: MIT License
            Operating System :: OS Independent
            Programming Language :: Python
            Topic :: Internet
            Topic :: Internet :: WWW/HTTP :: WSGI
            Topic :: Scientific/Engineering
            Topic :: Software Development :: Libraries :: Python Modules
        '''.split('\n'))),
        author='Termina1',
        author_email='terminal2010@gmail.com',
        url='http://solab.rshu.ru',
        license='MIT',

        packages=find_packages(),
        package_data=find_package_data("pywfs", package="pywfs",
                only_in_packages=False),
        include_package_data=True,
        zip_safe=False,
        namespace_packages=['pywfs'],

        dependency_links=[],
        install_requires=[
            'xmltodict',
            'pytest'
        ]
    ),
    minilib=Bunch(
        extra_files=['doctools', 'virtual']
    ),
)


@task
@needs(['generate_setup', 'setuptools.command.sdist'])
def sdist():
    """Overrides sdist to make sure that our setup.py is generated."""
    pass