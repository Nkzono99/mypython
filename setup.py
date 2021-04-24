from setuptools import setup, find_packages


long_description = open('README.md', 'r', encoding='utf-8').read()

setup(
    name="mypython",
    version="0.1.0",
    install_requires=[
    ],
    entry_points={
    },
    author="Nkzono",
    author_email="71783375+Nkzono99@users.noreply.github.com",
    description="A directory structure-aware python execution wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nkzono99/mypython",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
