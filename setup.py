import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="babyplots",
    version="1.7.0",
    author="Nils Trost",
    author_email="nils.trost@hotmail.de",
    description="Python package that allows the use of babyplots visualizations in jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/derpylz/babyplots_py",
    packages=setuptools.find_packages(include=['babyplots', 'babyplots.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "scikit-image",
        "ipython",
        "jinja2",
        "pandas"
    ],
    python_requires='>=3.6',
    include_package_data=True
)