# YC-scraper

To use the scraper, type in the command line
python scraper.py

This will scrape the Company Name, Location, YC Profile Page, Domain Name, YC batch, and Industries of all the YC companies within 'https://www.ycombinator.com/companies' and put into a CSV
This will also scrape the Founder info from the YC profile page and put into a separate CSV containing the list of Founders and their bio (if present)

If you wish to specify the batch, type the batch type in the command line 
(Ex. for Summer21 and Winter21)
python scraper.py -S21 -W21

Possible batches include:
[-S21, -W21, -S20, -W20, -S19, -W19, -S18, -W18, -S17, -W17, -S16, -W16, -S15, -W15, -S14, -W14, -S13, -W13, -S12, -W12, -IK12, -S11, -W11, -S10, -W10, -S09, -W09, -S08, -W08, 
-S07, -W07, -S06, -W06, -S05]
There is no limit to the number of batches one would like to put in the command line

The code will automatically create a CSV file, however, if you would like to create a JSON file, change the variable 'USE_JSON' at the top of scraper.py to True



# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
# platform: win-64
argparse=1.4.0=pypi_0
beautifulsoup4=4.9.3=pypi_0
brotlipy=0.7.0=py37h2bbff1b_1003
ca-certificates=2021.7.5=haa95532_1
certifi=2021.5.30=py37haa95532_0
cffi=1.14.6=py37h2bbff1b_0
cryptography=3.4.7=py37h71e12ea_0
idna=3.2=pyhd3eb1b0_0
numpy=1.21.1=pypi_0
openssl=1.1.1k=h2bbff1b_0
pandas=1.3.0=pypi_0
pip=21.1.3=py37haa95532_0
pycparser=2.20=py_2
pyopenssl=20.0.1=pyhd3eb1b0_1
pysocks=1.7.1=py37_1
python=3.7.10=h6244533_0
python-dateutil=2.8.2=pypi_0
pytz=2021.1=pypi_0
selenium=3.141.0=py37hfa6e2cd_1001
setuptools=52.0.0=py37haa95532_0
six=1.16.0=pyhd3eb1b0_0
soupsieve=2.2.1=pypi_0
sqlite=3.36.0=h2bbff1b_0
urllib3=1.26.6=pyhd3eb1b0_1
vc=14.2=h21ff451_1
vs2015_runtime=14.27.29016=h5e58377_2
wheel=0.36.2=pyhd3eb1b0_0
win_inet_pton=1.1.0=py37haa95532_0
wincertstore=0.2=py37_0
