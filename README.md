# smtp-reputation-monitor
Simple Python script to monitor IP SMTP reputation score. Designed to
be easily used with other monitoring/alerting tools such as Zabbix. Should work
on any system with Python 2.x/3.x


Description
---------
Script will check what is SMTP reputation of given IP.
Detailed mode (-d) diplays RBL name and score.


Requirements
---------
There are none. :-)
It's written with portability in mind, so tried to use as much already availabe
modules as possible.


Configuration
---------
TODO


Examples
---------
- python rblcheck.py -i 1.2.3.4 - checks reputation of IP 1.2.3.4


Usage
---------
- clone this repository
- run the script (with proper arguments, check examples)


Contribution
---------
Help is always welcome, so clone this repository, send pull requests or create
issues if you find any bugs.


License
---------
See LICENSE file.
