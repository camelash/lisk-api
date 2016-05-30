#!/usr/bin/env python

import json
import re
import sys
import math
import argparse
import time
import csv
import logging
import getpass
import liskAPI

# Read in csv | address | amount | 
# Feed that to sender
# wait 10s then confirm on two different nodes

parser = argparse.ArgumentParser(description='Yeah')
parser.add_argument('-f', '--file', dest='infile', action='store',
                    help='Input File')
parser.add_argument('-lf','--log-file',dest='logfile',action='store',
                    default='',help='Logging')
args = parser.parse_args()

logger = logging.getLogger(__name__)

LEVELS = {'info':logging.INFO}

logging.basicConfig(level=LEVELS['info'],
                    format='%(asctime)s %(funcName)s %(message)s ',
                    filename=args.logfile,
                    datefmt='%m/%d/%Y %I:%M:%S %p')

if not args.infile or not args.logfile:

    print "No file defined"
    print "Run like So: ./jhelper.py -f infile.csv -lf output.log"
    print "Infile should have the following format"
    print "address,amount"
    sys.exit(1)

#mainnet
try:

    passphrase = getpass.getpass()

except KeyboardInterrupt:

    print "\nAborting..."
    sys.exit(1)


payl = {'secret':passphrase}
api = liskAPI.liskAPI('http://127.0.0.1:8000')

account = api.account('open_account', payl)

if int(account['account']['balance']) < 1:

    print "No lisk in that account"
    sys.exit(1)

sender = liskAPI.liskAPI('http://127.0.0.1:8000')
verify1 = liskAPI.liskAPI('https://06.lskwallet.space')
verify2 = liskAPI.liskAPI('https://lisknode.io')

try:

    with open(args.infile) as jfhi, open('successout.csv', 'a') as jfho:
    
        jcsvr = csv.reader(jfhi)
        jcsvw = csv.writer(jfho)
    
        # Loop through the csv file and send transactions
        for row in jcsvr:
    
            # [0] address # [1] amount # [3] txid
    
            address = row[0]
            amount = float(row[1])
            print amount
    
            # Send the transaction
            amountstr = str(amount)
    
            strsplit = amountstr.split('.')
    
            if len(strsplit[1]) > 8:
    
                print "Invalid decimal places. Ex: 1.12345678"
    
                exit(1)
    
            monies = float(amount)
            amnt = monies * math.pow(10, 8) # amount times ten to the power of eigth
    
            sendpayload = {
                'secret' : passphrase,
                'recipientId' : address,
                'amount' : int(math.ceil(amnt))
            }
    
            try:

                response = sender.transactions('send', sendpayload)

            except Exception as e:

                print "Error {}".format(e)
                sys.exit(1)
    
            if response['success'] == 'False':

                print response
                logging.info(response)
                sys.exit(1)
                

            logging.info(response)
            tx = response['transactionId']

            logging.info(response)
    
            payload = {
                'id': tx,
                'parameters' : ''
            }

            localstuck = sender.transactions('unconfirmed', payload)

            while True:

                if not localstuck['success']:

                    continue

                else:

                    break

    
            time.sleep(20)

            if response['success']:
    
                row.append(tx)
    
                while True:

                    confirmation1 = verify1.transactions('get_tx', payload)
                    confirmation1u = verify1.transactions('unconfirmed', payload)
    
                    confirmation2 = verify2.transactions('get_tx', payload)
                    confirmation2u = verify2.transactions('unconfirmed', payload)
    
                    if (confirmation1['success'] or confirmation1u['success'])\
                        and (confirmation2['success'] or confirmation2u['success']):
    
                        print "Confirmed transaction {} is on login4/6".format(tx)
                        break
    
                    else:
    
                        continue
    

                if confirmation1['success'] and confirmation2['success']:
    
                    ss = 'success'
                    row.append(ss)
                    jcsvw.writerow(row)
    
                else:
    
                    ss = 'failure'
                    row.append(ss)
                    jcsvw.writerow(row)
    
            else:
    
                print "Transaction Failure"
    
                sys.exit(1)

except Exception as e:    

    raise
    print "Exiting... {}".format(e)
    sys.exit(1)
