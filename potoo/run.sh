#!/usr/bin/python
from django.core.management import call_command
call_command('syncdb')
call_command('runserver')