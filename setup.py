import setuptools

setuptools.setup(
    include_package_data=True,
    name="Detectar",
    version="0.0.1",
    description="Detectar face de uma pessoa usando uma imagem",
    url="https://www.github.com/matheusmalt/Detectar",
    author="Matheus Malta",
    packages=setuptools.setuptools.find_packages(),
    install_requires=["opencv-python"],
)