from setuptools import setup, find_packages

setup(
    name="image_processor",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",  # Biblioteca usada para manipular imagens
    ],
    author="Seu Nome",
    author_email="seu.email@example.com",
    description="Um pacote para processamento de imagens com filtros e transformações.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seuusuario/image_processor",  # Coloque o repositório do GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
