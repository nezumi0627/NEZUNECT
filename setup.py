from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nnezunect",
    version="0.3.1",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "urllib3>=1.26.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for interacting with the Subnect API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neuzmi0627/nnezunect",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    keywords="subnect api wrapper social-media",
)
