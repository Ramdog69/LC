#! /usr/bin/env python3

import configparser

class confParse(object):
   def __init__(self, configfile):
      self.conf = configfile
      cfgParser = configparser.ConfigParser()
      cfgParser.optionxform = str
      cfgParser.read(self.conf)
      self.investor_id = cfgParser.get('AccountData', 'investorId')
      self.authkey = cfgParser.get('AccountData', 'authKey')
      self.dbuser = cfgParser.get('AccountData', 'dbuser')
      self.dbpass = cfgParser.get('AccountData', 'dbpass')
      self.dbhost = cfgParser.get('AccountData', 'dbhost')
      self.dbname = cfgParser.get('AccountData', 'dbname')
      self.dbport = cfgParser.get('AccountData', 'dbport')

   def investorID(self):
      return self.investor_id

   def authKey(self):
      return self.authkey

   def dbconstring(self):
      return self.dbstring

   def db_user(self):
      return self.dbuser

   def db_pass(self):
      return self.dbpass

   def db_host(self):
      return self.dbhost

   def db_name(self):
      return self.dbname

   def db_port(self):
      return int(self.dbport)
