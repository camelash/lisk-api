#!/usr/bin/env python

import json
import re
import sys
import math
import argparse
import time
import csv
import signal
import logging
import getpass
import liskAPI
import datetime


# Read in csv | address | amount | 
# Feed that to sender
# wait 10s then confirm on two different nodes

signal.signal(signal.SIGTSTP, signal.SIG_IGN)

parser = argparse.ArgumentParser(description='Yeah')
parser.add_argument('-s1', '--site1', dest='site1', action='store',
                    default='https://lisknode.io',help='Site1')

parser.add_argument('-s2', '--site2', dest='site2', action='store',
                    default='https://lisk-login.vipertkd.com',help='Site2')

parser.add_argument('-u', '--url', dest='url', action='store',
                    default='http://localhost:7000',
                    help='Url in format: http://localhost:7000')

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

#logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

if not args.infile or not args.logfile:

    print "No file defined"
    print ""
    print "Run like So:"
    print "./jhelper.py -f infile.csv -lf output.log"
    print "Optional:"
    print "-s1 https://lisknode.io"
    print "-s2 https://lisk-login.vipertkd.com"
    print ""
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
api = liskAPI.liskAPI(args.url)

account = api.account('open_account', payl)

if int(account['account']['balance']) < 1:

    print "No lisk in that account"
    sys.exit(1)

sender = liskAPI.liskAPI(args.url)
verify1 = liskAPI.liskAPI(args.site1)
verify2 = liskAPI.liskAPI(args.site2)

try:

    with open(args.infile) as jfhi:

        jcsvr = csv.reader(jfhi)

        # Loop through the csv file and send transactions
        for row in jcsvr:

            # [0] address # [1] amount # [3] txid

            address = row[0]
            amount = row[1]

            amountstr = str(amount)

            strsplit = amountstr.split('.')

            if len(strsplit[1]) > 8:

                print "Invalid decimal places. Ex: 1.12345678"

                exit(1)

            amnt = float(amount) * math.pow(10, 8) # amount times ten to the power of eigth

            sendpayload = {
                'secret' : passphrase,
                'recipientId' : address,
                'amount' : int(math.ceil(amnt))
            }

            try:

                response = sender.transactions('send', sendpayload)
                now = datetime.datetime.now()
                row.insert(0, now.strftime("%Y-%m-%d-%H:%M"))

            except Exception as e:

                print "Error {}".format(e)
                sys.exit(1)

            if response['success'] == False:

                print response
                logging.info(response)
                sys.exit(1)


            logging.info(response)

            tx = response['transactionId']

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

                        now = datetime.datetime.now()
                        print "{} Confirmed transaction {} is on 2 remote nodes"
                            .format(now.strftime("%Y-%m-%d-%H:%M"), tx)

                        with open('successout.csv', 'a') as jfho:

                            jcsvw = csv.writer(jfho)

                            ss = 'success'
                            row.append(ss)
                            logging.info(row)
                            jcsvw.writerow(row)

                        break

                    else:

                        continue


            else:

                print "Transaction Failure"

                sys.exit(1)

except Exception as e:

    raise
    print "Exiting... {}".format(e)
    sys.exit(1)
