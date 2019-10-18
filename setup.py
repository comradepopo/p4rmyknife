try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    'description': 'P4rmyKnife - The Swiss Army Knife for P4',
    'author': 'Assembla, Inc.',
    'url': 'https://assembla.com/'
    'author_email': 'louis@assembla.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['p4rmyknife'],
    'scripts': [],
    'name': 'p4rmyknife'

setup(name='p4rmyknife',
    description='P4rmyKnife - The Swiss Army Knife for P4',
    author='Assembla, Inc.',
    url='https://assembla.com/'
    author_email='louis@assembla.com',
    version='0.1',
    install_requires=[],
    packages=['p4rmyknife'],
    scripts=[]
)
