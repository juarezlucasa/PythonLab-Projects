# python setup.py sdist
# Luego para instalar en site_packages: python setup.py install
from distutils.core import setup

setup(
    name="prueba1",
    description="Es una prueba de uso",
    version="1.0.0",
    py_modules=["prueba1"],
    author="juarezlucavs",
    author_email="juarezlucas.92@gmail.com",
    url="www.juarezlucavs92.com",
)
