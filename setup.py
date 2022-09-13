from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in myapp/__init__.py
from myapp import __version__ as version

setup(
	name="myapp",
	version=version,
	description="for demo",
	author="riddhi",
	author_email="riidhi@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
