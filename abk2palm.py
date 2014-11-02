#!/usr/local/bin/python

'''convert native abook address file (.abook.addressbook)to palm addressbook import file
   and write to stdout. The palm fields are (in this order):
   lastname,firstname,title,company,workphone,homephone,fax,other,
   e-mail,address,city,state,zipcode,country,birthday,custom2,
   custom3,custom4
'''

import sys,string

def convert2palm(in_file):
  dict_abook = {}
  i = 0
  for line in open(in_file,"r").readlines():
     i = i + 1
     if i <= 7: continue
     line = line[:-1]
     if line.startswith('['):
        dict_abook = {}
     elif string.find(line,'=') <> -1:
        l = string.split(line,'=')
        #cmd = "dict_abook[" + "'" + l[0] + "']" + " = " + "'" + l[1] + "'"
        cmd = 'dict_abook[' + '"' + l[0] + '"]' + ' = ' + '"' + l[1] + '"'
        exec cmd
     else:
        if len(dict_abook) <> 0:
           dict_palm = {'lastname' : '', 'firstname': '', 'title'   : '', 'company': '', 'workphone': '', 
                        'homephone': '', 'fax'      : '', 'other'   : '', 'e-mail' : '', 'address'  : '',
                        'city'     : '', 'state'    : '', 'zipcode' : '', 'country': '', 'birthday' : '',
                        'custom2'  : '', 'custom3'  : '', 'custom4' : ''}
           if dict_abook.has_key('name')     : dict_palm['lastname']  = dict_abook['name']
           if dict_abook.has_key('email')    : dict_palm['e-mail']    = dict_abook['email']
           if dict_abook.has_key('address')  : dict_palm['address']   = dict_abook['address']
           if dict_abook.has_key('city')     : dict_palm['city']      = dict_abook['city']
           if dict_abook.has_key('state')    : dict_palm['state']     = dict_abook['state']
           if dict_abook.has_key('zip')      : dict_palm['zipcode']   = dict_abook['zip']
           if dict_abook.has_key('country')  : dict_palm['country']   = dict_abook['country']
           if dict_abook.has_key('phone')    : dict_palm['homephone'] = dict_abook['phone']
           if dict_abook.has_key('workphone'): dict_palm['workphone'] = dict_abook['workphone']
           if dict_abook.has_key('fax')      : dict_palm['fax']       = dict_abook['fax']
           if dict_abook.has_key('mobile')   : dict_palm['custom2']   = dict_abook['mobile']
           if dict_abook.has_key('url')      : dict_palm['custom3']   = dict_abook['url']
           if dict_abook.has_key('notes')    : dict_palm['custom4']   = dict_abook['notes']

           print quote(dict_palm['lastname'])  + "," + \
                 quote(dict_palm['firstname']) + "," + \
                 quote(dict_palm['title'])     + "," + \
                 quote(dict_palm['company'])   + "," + \
                 quote(dict_palm['workphone']) + "," + \
                 quote(dict_palm['homephone']) + "," + \
                 quote(dict_palm['fax'])       + "," + \
                 quote(dict_palm['other'])     + "," + \
                 quote(dict_palm['e-mail'])    + "," + \
                 quote(dict_palm['address'])   + "," + \
                 quote(dict_palm['city'])      + "," + \
                 quote(dict_palm['state'])     + "," + \
                 quote(dict_palm['zipcode'])   + "," + \
                 quote(dict_palm['country'])   + "," + \
                 quote(dict_palm['birthday'])  + "," + \
                 quote(dict_palm['custom2'])   + "," + \
                 quote(dict_palm['custom3'])   + "," + \
                 quote(dict_palm['custom4']) 

def quote(s):
  return '"' + s + '"'


print sys.argv
convert2palm(sys.argv[1])
