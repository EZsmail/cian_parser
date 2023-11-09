from setuptools import setup

with open('README.md', encoding='utf8') as file:
    read_me_description = file.read()
    
setup(
    name='parser_cian',
    version='0.0.5',
    description='Parser for easy data retrieval from cian.ru',
    url='https://github.com/EZsmail/cian_parser',
    author='Anatoly Gvozdev',
    author_email='tolagvgvgvgv@gmail.com',
    license='MIT',
    packages=['parser_cian'],
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='python parser requests cian realestate beautifulsoup dataset',
    install_requires=['beautifulsoup4', 'selenium', 'lxml', 'selenium-stealth', 'aiogram'],
)
    
