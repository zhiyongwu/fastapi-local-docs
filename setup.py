from setuptools import setup, find_packages

setup(
    name='fastapi-local-docs',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'fastapi'
    ],
    package_data={
        "fastapi_local_docs": ["static/*"]
    },
)
