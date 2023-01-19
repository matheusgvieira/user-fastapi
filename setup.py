from distutils.util import convert_path
from typing import Dict

from setuptools import find_packages, setup


package_name = "fast_api_usuarios"


main_ns = {}
ver_path = convert_path("app/version.py")
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

requirements = [
    "fastapi==0.89.1",
    "uvicorn==0.20.0",
    "ormar==0.12.0",
    "psycopg2==2.9.5",
    "asyncpg==0.27.0",
]

dev_requirements = [
    "flake8==6.0.0",
    "isort==5.11.4",
    "refurb==1.10.0",
    "mypy==0.991",
    "pytest==6.2.",
    "pytest-cov==2.8.1",
    "pytest-flake8==1.0.6",
    "pytest-mypy==0.8.0",
    "pylint==2.15.10",
    "fastapi==0.89.1",
    "uvicorn==0.20.0",
    "ormar==0.12.0",
]

setup(
    name=package_name,
    package_dir={'app': 'app'},
    packages=find_packages(),
    python_requires=">=3.10.7",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "integration": dev_requirements,
        "unit": dev_requirements,
    },
    version=main_ns["__version__"],
    description=(
        "Api para armazenamento de usuario"
    ),
    long_description=(
        "Api para armazenamento de usuario"
    ),
    author="Matheus Gois Vieira",
    author_email="matheusmaxi9.0@gmail.com",
    url="https://fontes.intranet.bb.com.br/big/big-bbmagic",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python ::3.10.7",
        "Topic :: Scientific/Engineering",
    ],
)
