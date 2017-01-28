#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import string
import numpy as np
import time

#today = str(time.strftime("%Y-%m-%d"))
today = str(time.strftime("%d.%m.%Y"))
todayURL = str(time.strftime("%d-%m-%Y"))

# --------------- dump -------------------- #

import os
#url = "http://sojp.wios.warszawa.pl/?page=raport-godzinowy&data=%s&site_id=13&csq_id=1414&dane=w1" % todayURL
url = "http://powietrze.gios.gov.pl/pjp/current/station_details/table/550/1/0"

#print url
#exit(1)
#27.01.2017

#cmd = os.popen("lynx -dump '%s' | grep %s | sed -e 's/,/./g'" % (url, today))
cmd = os.popen('cat dump.txt | grep %s | sed -e "s/,/./g"' % (today))

raw = cmd.read()
cmd.close()

print raw
exit(1)


# ----------- processing ------------------- #

raw = re.sub(' +',' ', raw )
out = [x.strip().split(" ") for x in raw.split('\n') ]
print out
exit(1)

for line in raw.split('\n'):
	line = re.sub(' +',' ',line.strip())
        values_tmp=string.split(line, " ")
        #print values_tmp, len(values_tmp)
        if len(values_tmp) > 2:
           values = values_tmp
           #print values

if values == "":
    print "??"
else:

    '''
    ['Data,', 'godzina', 'PM10', 'SO2', 'NO2', 'O3', 'PM25']
    ['2014-12-16', '09:00', '35.5', '7.6', '32.2', '4.2', '32.3']
    '''


    binsPM10=np.array(range(10,220,10))
    binsPM25=np.array(range(5,120,5))
    binsNO2 =np.array(range(10,220,10))

    letters='ABCDEFGHIJKLMNOPQRSTUWX-=!'

    x = np.array([float(values[2])])
    binPM10 = int(np.digitize(x, binsPM10))
    binPM10Lit=letters[binPM10]


    x = np.array([float(values[3])])
    binPM25 = int(np.digitize(x, binsPM25))
    binPM25Lit=letters[binPM25]

    x = np.array([float(values[5])])
    binNO2 = int(np.digitize(x, binsNO2))
    binNO2Lit=letters[binNO2]



    #print values[0:2]
    #print "PM10:  ", values[2], binPM10
    #print "PM2.5: ", values[6], binPM25

    #print str("%.0f" % round(float(values[2]))) + "(" + str(binPM10) + ") " + str("%.0f" % round(float(values[6]))) + "(" +  str(binPM25) + ")"

    print str(binPM10Lit) + "" + str(binPM25Lit) + str(binNO2Lit)