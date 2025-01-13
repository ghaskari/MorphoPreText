from setuptools import setup, find_packages

setup(
    name="MorphoPreText",
    version="0.1.0",
    author="Ghazal Askari",
    author_email="g.askari1037@gmail.com",
    description="A bilingual text preprocessing toolkit for English and Persian.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ghaskari/MorphoPreText",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "emoji==2.14.0",
        "nltk==3.2.2",
        "pandas==2.2.3",
        "scikit-learn==1.6.0",
        "pyspellchecker==0.8.2",
        "parsivar==0.2.2",
        "spacy==3.8.3",
        "openpyxl==3.1.5",
        "jdatetime==5.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="text preprocessing NLP English Persian bilingual",
)
