# Cian Parser #

## What is this? ##
This is a parser with which you can easily get data from a website cian.ru.

## Quick Guide ##
This module is based on Selenium-Stealth, using BeautifulSoup as well as Asyncio

Data you can get:
1) Name of apartment
2) The city district in which the housing estate is located
3) Price of the apartment             
4) Time to the subway
5) How to get to the subway          
6) Nearest subway             
7) Price per square meter             
8) Total square footage             
9) Living Space             
10) Floor             
11) Number of stories in the house             
12) Year of delivery of the house                       
13) Surrendered or not             
14) Finishing             
15) Parking             
16) Ceiling Heights            
17) Builder Rating 

----------


### Using ###


Using the library is as simple and convenient as possible:

Let's import it first:
First, import everything from the library (use the `from `...` import *` construct).

Examples of all operations:

Сreate an instance of a class `Cian_Parser` (PATH - file save path, URL - site url):

    parser = Cian_Parser(PATH, URL)

Receive all data of all apartments in CSV format using the `get_data()` function:

    asyncio.run(parser.get_data())

If you want to create your own parser logic, then use the description of the other modules:

Сreate an instance of a class `Pagination` (parser - parser instance from the Flats_Url class, next_button_selector - XPATH pagination buttons)

    pagination = Pagination(parser, next_button_selector)

Checking for next page using the `HasNextPage()` function:

    await pagination.HasNextPage()

Go to next page using the `GoToTheNextPage()` function:

    await pagination.GoToTheNextPage()



## Developer ##
My site: [link](https://ezsmail.github.io/Profile/)
