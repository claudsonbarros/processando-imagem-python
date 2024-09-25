from setuptools import setup, find_packages

setup(
    name="imagem_processor",
    version="0.0.1",
    author="claudsonbarros",
    author_email="claudson.s.b@gmail.com",
    description="Pacote para processamento de imagem em Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/claudsonbarros/processando-imagem-python"
    packages=find_packages(),
    install_requires=requirements
)

