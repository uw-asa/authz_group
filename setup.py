from setuptools import setup, find_packages
import os

install_requires = ['Django']
if os.environ.get("DJANGO_VERSION"):
    install_requires = ['Django=%s' % os.environ.get("DJANGO_VERSION")]

setup(
    name='AuthZ-Group',
    version='1.2.0',
    description='Group interface and implementations',
    install_requires=install_requires,
    packages=find_packages(exclude=["project"]),
    include_package_data=True,  # use MANIFEST.in during install
    author = "Patrick Michaud",
    author_email = "pmichaud@uw.edu",
    license = "Apache 2.0",
    keywords = "django groups authorization",
    url = "https://github.com/vegitron/authz_group/"
)
