## Information Gathering

Information gathering is the first important step of ethical hacking process. It is the process of
gathering information about target and its environment. It is a very important step because
after this a clear assessment of a network can be made. Good information gathering can make
the difference between a successful penetration testing and one that has failed to provide
maximum benefit to the client.

## Method Used

The system is built using Django web application framework. Django was originally developed
for the news-oriented site of the world company in Lawrence, Kansas. It simplifies the
development process of complex web applications. Its well-designed framework includes three
major parts: model, view and template. This tool consists of various modules. Each module
performs the duty of fetching a particular record.


## Python

Python is the language used to build Django framework. It is a dynamic scripting language
similar to Perl and Ruby. The principal author of Python is Guido van Rossum. Python supports
dynamic typing and has a garbage collector for automatic memory management. Another
important feature of Python is dynamic name solution which binds the names of functions and
variables during execution.

## Django

Django is an open source web application framework written in Python. The primary goal of
Django is to make the development of complex websites easier. Thus Django emphasizes the
reusability and pluggability of components to ensure rapid developments. The components of
Django used in this project are:


➢ View
View is short form of view file. It is a file containing Python function which takes web
requests and returns web responses. A response can be HTML content or XML documents
or a “404 error” and so on. The logic inside the view function can be arbitrary as long
as it returns the desired response. To link the view function with a particular URL we
need to use a structure called URLconf which maps URLs to view functions
➢ Template
Django’s template is a simple text file which can generate a text-based format like
HTML and XML. The template contains variables and tags. Variables will be replaced by
the result when template is evaluated. Tags control the logic of the template. We can
also modify the variables by using filters.

## Apps

The web application is entirely written in Python 2.7.13. It is an integrated web-based system
combining several individual modules. The sub modules include

➢ A
Module for IPv4 fetching address records of given domain. The returned result includes
the IPv4 address of the domain, geolocation of the server and TTL (Time to live) of the
record.
➢ AAAA
Module for IPv6 fetching address records of given domain. The returned result includes
the IPv6 address of the domain, geolocation of the server and TTL (Time to live) of the
record.
➢ MX
This module collects the mail exchange records which map the given domain name to
its respective message transfer agents. The result includes the MX agent address,
geolocation and TTL of the record.
➢ WHOIS
Implements a WHOIS query and displays the data in tabular format. WHOIS is a query
and response protocol used for querying databases that store the registered users or
assignees of an internet resource such as a domain name, an IP address block, or an
autonomous system.
➢ Blacklist
Check various DNSBL / RBL for blacklisting of given domain or IP address. DNSBL (DNS-
based Blackhole List) or Real-time Blackhole List (RBL) is an effort to stop email
spamming. It is a blacklist of locations on the internet reputed to send email spam.
➢ Reverse
Implement a PTR lookup of the given IP address. PTR record or Pointer record is a pointer
to a canonical name i.e. Domain name. The result includes geolocation, domain name
and TTL of the record.



➢ Scripts
This module consists of the main python scripts used to fetch all the records. The scripts
are implemented using various python libraries.

- a.py, aaaa.py, mx.py, ptr.py,
    These scripts use resolver module of dnspython library to fetch respective DNS
    records. The location of respective server is found using geocoder python library.
    The output is returned in the form of an object/ list of objects.
- blacklist.py
    To check a client against a DNSBL the client IP address’ octets are reversed and
    DNSBL domain is appended to it. Then an A lookup of this name is done. This will
    return either an address, indicating that the client is listed or an “NXDOMAIN”
    (“No such domain”) code, indicating that the client is not. If client is listed, the
    TXT record is fetched to get information about why the client is listed.
- whoisrec.py
    This script implements a WHOIS query using a python-whois library. The raw
    WHOIS data is parsed using regular expressions and returned in a formatted
    manner.
- checkhost.py
    This module is used for checking valid domain names, IPv4 and IPv6 addresses.
    This is implemented using socket library of python and regular expressions.

➢ Access Control
Access control is implemented using Django authentication system built in its default
system configuration. It has a careful implementation of passwords and permissions. The
default admin panel can be accessed in /admin URL. Default superuser username and
password set for this project are admin and longpassword respectively. Superusers can
create new users and manage permissions using groups by logging into the admin panel.
New superusers can be added using manage.py in the project folder.

```$ python manage.py createsuperuser _--username=newsuperuser ```


### Web Components

**• HTML**


For template design.

**• CSS**


For styling.

- **Bootstrap**
    A bootstrap template is used to build the admin panel UI
- **Javascript**
    Various javascript libraries are used in this project. jQuery is used to handle POST and
    GET requests and manage UI elements. Datatables.js us used to generate interactive
    tables with sorting and searching features. Other UI and animations libraries liked
    uniform.js and select2.js are also used.

### Functionalities

- **Fetch multiple records**
    The home page of the web application provides a form to fetch all the different records
    for the given domain or IP address together. It fetches all the records and displays it in
    tabular format
- **Fetch respective records**
    The dedicated pages for each domain query provides a form to fetch the respective
    records. The record is fetched in tabular format.
- **Fetch records for a list of domains**
    The dedicated pages for different queries also provide a file form to input text files with
    a list of space or newline separated domains or IP addresses. The python view function
    reads the file and extracts valid domain names and addresses using checkhost.py and
    fetch records for the same.


### Libraries


➢ dnspython
Package: dnspython 1.15.
Description: A DNS toolkit for Python
➢ geocoder
Package: geocoder-1.23.
Description: Simple and consistent geocoding library written in Python.
➢ python-whois
Package: python-whois-0.6.
Description: Whois querying and parsing of domain registration information.
➢ whitenoise
Package: whitenoise-3.3.
Description: With a couple of lines of config WhiteNoise allows your web app to serve
its own static files, making it a self-contained unit that can be deployed anywhere
without relying on nginx, Amazon S3 or any other external service.

### Dependencies

- certifi==2017.4.
- chardet==3.0.
- click==6.
- decorator==4.0.
- Django==1.11.
- dnspython==1.15.
- future==0.16.
- geocoder==1.22.
- httplib2==0.10.
- idna==2.
- MySQL-python==1.2.
- olefile==0.
    - pyasn1==0.2.
    - pyasn1-modules==0.0.
    - python-whois==0.6.
    - pytz==2017.
    - ratelim==0.1.
    - requests==2.17.
    - rsa==3.4.
    - six==1.10.
    - uritemplate==3.0.
    - urllib3==1.21.
    - whitenoise==3.3.


# Deploying

**settings.py**

Django settings file contains all the configuration of the web application. It is a python module
with module-level variables.

```
SECRET_KEY = '<your-secret-key>'
DEBUG = False
```

The secret ley must be a large random value and it must be kept secret to avoid attacks and
remote code execution. Instead of hardcoding the secret key in settings module, it should be
loaded from an environment variable

```
import os
SECRET_KEY = os.environ['SECRET_KEY']
```

Debug = True enables full tracebacks and errors in browser during development. For production
environment DEBUG is set to false to prevent leaks of information about project, excerpts of
source code, local variables, settings, libraries used, etc.

```
ALLOWED_HOSTS = ['yourdomain.com',
'127.0.0.1',
'localhost',
]
```

When DEBUG = False, Django doesn’t work without ALLOWED_HOSTS being mentioned
explicitly. This setting is required to protect the application against some cross-site reference
attacks.

```
DATABASES = {
                              'default': {
                                                  'ENGINE': 'django.db.backends.mysql',
                                                  'NAME': 'database',
                                                  'USER': 'username',
                                                  'PASSWORD': 'password',
                                                  'HOST': 'hostname'
                                                  'PORT': 'port'
                                                 }
}
```

For using MySQL with Django MySQL-python binding need to be installed and database
credentials supplied to the ‘default’ element is DATABASES variable in settings module. Again
use of environment variables is recommended.


**manage.py**

```
$ python manage.py runserver
```

Runserver command starts the Django development server, a lightweight Web server written in
Python. Server runs on port 8000 by default on localhost.

```
$ python manage.py collectstatic
```

The application need to server additional files such as images, Javascript or CSS. In Django
these are referred to as “static files”. When deploying for production the collectstatic
command collects all static files and store into the static files directory which is mentioned by
STATIC_ROOT in the settings module.

**Deploying with Apache and mod_wsgi**

**Installing mod_wsgi**

- Download the source code tar ball of mod_wsgi from:
    ```https://github.com/GrahamDumpleton/mod_wsgi/releases```
- Unpack it with the command:
    ```$ tar xvfz mod_wsgi-X.Y.tar.gz```
- To setup the package ready for building run the “configure” script from within the
    source code directory.
    ```$ ./configure```
- Once the package has been configured, it can be built by running:
    ```$ make```
- To install the Apache module into the standard location for Apache modules as dictated
    by Apache for your installation, run:
    ```$ make install```
- Load the module into Apache by adding this line to /etc/apache2/apache 2 .conf
    ```LoadModule wsgi_module modules/mod_wsgi.so```
- Restart apache:
    ```$ service restart apache```
- If everything went okay, the following line appears in Apache error log.
    ```Apache/2.4.8 (Unix) mod_wsgi/4.4.21 Python/2.7 configured```


**Creating virtualenv:**

- Create a virtual environment for the project using virtualenv python package.
    ```$ virtualenv venv```
- Activate the virtual environment
    ```$ source venv/bin/activate```
- Go to the project folder and install package requirements from requirements.txt
    ```$ pip install -r requirements.txt```
- Deactivate the venv
    ```$ deactivate```

**Configuring mod_wsgi Daemon mode:**

- Edit apache conf file in /etc/apache2/apache2.conf and add the following lines:

```
WSGIScriptAlias / /path/to/nettools/nettools/wsgi.py
WSGIPythonHome /path/to/venv
WSGIPythonPath /path/to/nettools
<Directory /path/to/nettools/nettools>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
WSGIDaemonProcess nettools.process python-home=/path/to/venv python-
path=/path/to/nettools
WSGIProcessGroup nettools.process
```
- To serve your project in a subdirectory (https://example.com/nettools), you can add
   ``` 
   WSGIScriptAlias to the configuration above:
    WSGIScriptAlias /nettools /path/to/nettools/nettools/wsgi.py process-
    group=nettools.process
   ```
- Restart apache:
    ```$ service restart apache```

**Collecting static files:**

- Run collectstatic command to collect the static files for serving:
    ```$ python manage.py collectstatic```

**Migrating database:**

- Finally run migrate command initialize the database:
    ```$ python manage.py migrate```



