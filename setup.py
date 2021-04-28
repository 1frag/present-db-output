from setuptools import setup

setup(
    name="present-db-output",
    version="0.0.1",
    py_modules=["ipdo"],
    license="BSD",
    author="Alexey Piskunov",
    author_email="piskunov.alesha@gmail.com",
    description="Convert database output",
    install_requires=["click==7.1.2"],
    entry_points=dict(console_scripts=["ipdo = ipdo:cli"]),
)
