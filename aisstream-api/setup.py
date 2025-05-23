from setuptools import setup

setup(
    name='aisstream.io-example-simple',
    author='aisstream.io',
    version='0.1',
    install_requires=[
        'websockets',
        'asyncio'
    ],
    py_modules=['main', 'main_mmsi_message_filter', 'main_ssl_disabled'],
)
