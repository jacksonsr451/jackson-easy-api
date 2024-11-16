from setuptools import setup, find_packages
import os
import shutil

def copy_manage_file():
    if os.path.exists('jackson_easy_api/manage.py'):
        shutil.copy('jackson_easy_api/manage.py', 'manage.py')

setup(
    name="easy-api",
    version="0.1.0",
    description="A FastAPI project generator",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Jackson Severino da Rocha",
    author_email="jacksonsr451@gmail.com",
    url="https://github.com/jacksonsr451/easy-api",
    packages=find_packages(where=".", exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "fastapi",
        "sqlalchemy",
        "alembic",
        "python-decouple",
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    package_data={
        '': ['jackson_easy_api/manage.py'],
    },
    data_files=[('', ['jackson_easy_api/manage.py'])],
)

copy_manage_file()
