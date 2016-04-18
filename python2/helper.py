#!/usr/bin/env python

import json
import re
import os.path
import argparse
import liskAPI
import getpass

def main():

    parser = argparse.ArgumentParser(description='LISK API Interface')
    parser.add_argument('-o','--option',dest='option',action='store',
        required=True,help='Query option')

    parser.add_argument('-w','--wallet',dest='wallet',action='store',
        default='2994830225868734490L',help='Wallet')

    parser.add_argument('-k','--key',dest='pubkey',action='store',
        help='Public Key')

    parser.add_argument('-u','--url',dest='url',action='store',
        default='http://localhost:7000',help='Url in format: http://localhost:7000')

    parser.add_argument('-vf','--vote-file',dest='vote_file',action='store',
        default='votelist.txt',help='Load Vote File')

    parser.add_argument('-dstid','--destination-id',dest='dst_id',action='store',
        help='Destination Id or address')

    parser.add_argument('-a','--amount',dest='amount',action='store',
        type=float,help='amount to send')

    parser.add_argument('-s','--secret',dest='secret',action='store_true',
        default=False,help='secret pass phrase')

    parser.add_argument('--vote-no',dest='vote_no',action='store_true',
        default=False,help='secret pass phrase')

    parser.add_argument('--vote-yes',dest='vote_yes',action='store_true',
        default=False,help='secret pass phrase')

    parser.add_argument('-p','--parameters',dest='q_params',action='store',
        default='',help='query parameters')

    parser.add_argument('-id','--id',dest='all_id',action='store',
        default='',help='tx id or block id')

    args = parser.parse_args()

    passphrase_options = ['enable_forging','disable_forging','send','genpub','open_account','vote']
    if not args.option:
        parser.print_help()

    if args.option == 'vote' and args.vote_file:

        if os.path.isfile(args.vote_file) == False and not args.vote_yes\
                and not args.vote_no:
            print "\nFile not found or key not defined\n\n\
                   python helper.py --option vote --vote-file 1.txt\n\n\
                    file layout:\n\
                    pubkey\n\
                    pubkey\n\
                    pubkey\
                    "
            exit(1)

    if args.secret == True or args.option in passphrase_options:
        secret = getpass.getpass()
        secret1 = getpass.getpass()

        # Simple check. needs revamp
        if secret != secret1:
            print "Passprase does not match. Please try again"
            exit(1)

    opt = args.option
    wallet = args.wallet
    url = args.url
    pubkey = args.pubkey
    payload = {}
    hex_match = re.compile(r'^[A-Za-z0-9]{64}$')

    # Instanciate
    api = liskAPI.liskAPI(url)

    get_lodr = ['sync','status']
    get_acct = ['balance','account','delegates_by_account','pubkey']
    put_acct = ['genpub','vote','open_account']
    get_peer = ['peer_ip','peer_list','peer_version']
    get_txid = ['blocktx','get_tx','unconfirmed','unconfirmed_all']
    put_txid = ['send']
    post_del = ['disable_forging','enable_forging']
    get_delg = ['forged',"delegate_list","delegate_by_tx","votes_by_account","delegate_voters"]
    get_blk = ['my_blocks','blockid','all_blocks','fee','height']


    # Loader - Complete
    if opt in get_lodr:
        print json.dumps(api.loader(opt), indent=2)

    # Accounts - balance and account works
    elif opt in get_acct:

        payload = {
            'address' : wallet
        }

        print json.dumps(api.account(opt,payload), indent=2)


    elif opt in put_acct:

        if opt == 'open_account' and secret:

            payload = {'secret' : secret}

        elif opt == 'vote' and secret:

            pubkey_list = []
            vote_type = ''

            if args.vote_no == True and not args.vote_yes:
                vote_type = '-'
            elif args.vote_yes == True and not args.vote_no:
                vote_type = '+'
            else:
                print "Vote method is not defined"
                exit(1)

            with open(args.vote_file) as vf_fh:

                for pubkey in vf_fh:

                    key_s = pubkey.strip()

                    match = re.search(hex_match, key_s)

                    if match:
                        pubkey_list.append("{}{}".format(vote_type,key_s))
                    else:
                        print "Found a non matching line in the file. Quitting."

            payload = {
                    'secret' : secret,
                    #'publicKey' : '',
                    #'secondSecret' : '',
                    'delegates' : pubkey_list
                }

        elif opt == 'genpub':
            payload = { 'secret' : secret }

        else:
            print "Accounts Errors"
            exit(1)

        print json.dumps(api.account(opt,payload), indent=2)

    # Peers - TODO: peer_ip -- DONE: peer_list, peer_version
    elif opt in get_peer:
        payload = {
                 "ip" : "127.0.0.1",
                 "port" : 7000,
                 "parameters" : args.q_params
            }
        print json.dumps(api.peers(opt,payload), indent=2)

    # Transactions
    elif opt in get_txid:
        payload = {'id':args.all_id}
        print json.dumps(api.transactions(opt,payload), indent=2)

    elif opt in put_txid:
        if opt == 'send' and secret:
            # SEND SOME LISK BRAH!!!
            amount = args.amount * 10**8 # amount times ten to the power of eigth

            payload = {
                'secret' : secret,
                'recipientId' : args.dst_id,
                'amount' : amount
                #'publicKey' : pubkey
            }
            print json.dumps(api.transactions(opt,payload), indent=2)

    # Blocks
    elif opt in get_blk:
        payload = {'id' : args.all_id,
                'pubkey' : pubkey,
            }
        print json.dumps(api.blocks(opt,payload), indent=2)

    #Delegates
    elif opt in get_delg:
        payload = {
            'pubkey' : pubkey, #forged and delegate_voters
            'id' : args.all_id, #delegate_by_tx
            'address' : wallet
                }
        print json.dumps(api.delegates(opt,payload), indent=2)

    elif opt in post_del:
        #For forging
        payload = { 'secret' : secret }
        print json.dumps(api.delegates(opt,payload), indent=2)

    # Hybrid call, my voters
    elif opt == 'my_voters':

        print json.dumps(api.my_voters(wallet), indent=2)

if __name__ in '__main__':

    main()
