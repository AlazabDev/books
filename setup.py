setup.pyfrom setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="books",
    version="0.0.1",
    description="Books App for ERPNext",
    author="AlazabDev",
    author_email="admin@alazab.online",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
