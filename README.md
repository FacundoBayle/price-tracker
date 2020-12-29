# PriceTracker
Multiple website price tracker.

## Supported Websites
Currently supported websites:
- [Tiendamia](https://tiendamia.com/ar/)
- [MercadoLibre](https://www.mercadolibre.com.ar/)

## Requirements
It is necessary to **install the following libraries** to be able to execute the script:
* requests
~~~
pip install requests
~~~
* BeautifulSoup
~~~
pip install beautifulsoup4
~~~

## Run
Just run **main.py**
~~~
python3 main.py
~~~
#### Credentials
To send mails it is necessary to have the login information. Create a root file **credentials.json** with the following format to be able to log in correctly and send emails.
~~~
{
    "user":"your_mail_account",
    "password":"your_mail_password"
}
~~~

## Mails

#### Price Mail
![price mail](/img/price-mail.png "Price Mail")

#### Error Mail
![error mail](/img/error-mail.png "Error Mail")

## Logging
In order to keep track of the performance of the script, a **log.txt** file was added with the necessary information to be able to debug in case of error.