from setuptools import setup, find_packages
import wvcc

setup(
    name="wvcc",
    version=wvcc.__version__,
    long_description=wvcc.__description__,
    url=wvcc.__url__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "pytest",
        "flake8",
        "pytest-cov",
        "flake8-junit-report",
        "flake8-string-format",
        "ruamel.yaml",
        "prospector"
    ],
    tests_require=["pytest"],
)
