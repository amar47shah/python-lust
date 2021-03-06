
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Little Unix Server Toolkit',
    'author': 'Zed A. Shaw',
    'url': 'http://pypi.python.org/pypi/python-lust',
    'download_url': 'http://pypi.python.org/pypi/python-lust',
    'author_email': 'zedshaw@zedshaw.com',
     'version': '0.1',
     'scripts': [],
     'install_requires': [],
     'packages': ['lust', 'lust.unix', 'lust.log'],
     'name': 'python-lust'
}

setup(**config)
