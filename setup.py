from setuptools import find_packages, setup
from cicd_demo_philips import __version__

setup(
    name="cicd_demo_notebook_test",
    packages=find_packages(exclude=["tests", "tests.*","unit-tests", "unit-tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="demo",
    author="Kivanc",
)
