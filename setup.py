from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nezunect",
    version="0.2.0",
    author="nezumi0627",
    author_email="nezumi.20080627@gmail.com",
    description="A Python client library for the Subnect API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nezumi0627/NEZUNECT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "typing-extensions>=4.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=22.0.0",
            "isort>=5.0.0",
            "mypy>=0.900",
            "flake8>=3.9.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/nezumi0627/NEZUNECT/issues",
        "Source": "https://github.com/nezumi0627/NEZUNECT",
    },
)
