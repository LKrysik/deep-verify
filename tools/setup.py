"""
BMAD Contract Tools - Setup
"""

from setuptools import setup, find_packages

setup(
    name="bmad-contracts",
    version="0.1.0",
    description="Parse, validate, and visualize BMAD workflow contracts",
    author="BMAD Team",
    packages=find_packages(),
    install_requires=[
        "pyyaml>=6.0",
    ],
    entry_points={
        "console_scripts": [
            "bmad-contracts=bmad_contracts.cli:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
