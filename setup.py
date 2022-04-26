import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abrperf",
    version=os.getenv('CI_COMMIT_TAG'),
    author="Tamás",
    author_email="github.com@jursonovics.com",
    description="ABR loadtester module for locust.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jursonovicst/python-abrperf",
    project_urls={
        "Bug Tracker": "https://github.com/jursonovicst/python-abrperf/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)
