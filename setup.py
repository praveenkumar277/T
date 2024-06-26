from setuptools import setup, find_packages

setup(
    name="TermPYT",
    version="0.1.0",
    author="Praveen Kumar",
    author_email="praveen122187@gmail.com",
    description="",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/praveenkumar277/TermPYT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

