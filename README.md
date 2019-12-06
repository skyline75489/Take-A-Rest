Take A Rest
===========

Sometimes you just need to take a rest.

![rest](function.png)

### Requirments

* macOS / Linux Desktop with `notify-send`
* Python 3.4+
* [schedule](https://github.com/dbader/schedule)
* [pyobjc](https://pyobjc.readthedocs.io/en/latest/) if you are using macOS

### Usage 

	usage: take-a-rest.py [-h] [-v] [-w WORK] [-r REST]

	A tiny reminder that will notify you when you need a rest

	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         show program's version number and exit
	  -w WORK, --work WORK  working duration(in minutes)
	  -r REST, --rest REST  rest interval(in minutes)
