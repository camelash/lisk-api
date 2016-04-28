#!/usr/bin/env python

import json
import re
import os.path
import argparse
import liskAPI
import getpass



def loader(api,args):
    # Loader - Complete
    print json.dumps(api.loader(args.option), indent=2)

def accountget(api,args):
    payload = {
        'address' : args.wallet
    }

    print json.dumps(api.account(args.option,payload), indent=2)

def check2pass(api,args):

    pass

def accountput(api,args,secret,secret2):

    if args.option == 'open_account' and secret:

        payload = {'secret' : secret}

    elif args.option == 'vote' and secret:

        hex_match = re.compile(r'^[A-Za-z0-9]{64}$')
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

            for pkey in vf_fh:

                key_s = pkey.strip()

                match = re.search(hex_match, key_s)

                if match:

                    pubkey_list.append("{}{}".format(vote_type,key_s))

                else:

                    print "Found a non matching line in the file. Quitting."
                    exit(1)

        if second_passphrase == True:
            payload['secondSecret'] = secret2

        payload = {
                'secret' : secret,
                #'publicKey' : '',
                #'secondSecret' : '',
                'delegates' : pubkey_list
            }

    elif args.option == 'genpub':

        payload = { 'secret' : secret }

    else:
        print "Accounts Errors"
        exit(1)

    print json.dumps(api.account(args.option,payload), indent=2)

def peerget(api,args):

    payload = {
             "ip" : "127.0.0.1",
             "port" : 7000,
             "parameters" : args.q_params
        }
    print json.dumps(api.peers(args.option,payload), indent=2)

def transactionsget(api,args):

        payload = {
                'id':args.all_id,
                 'parameters' : args.q_params
            }

        print json.dumps(api.transactions(args.option,payload), indent=2)

def transactionput(api,args,secret):

        if args.option == 'send' and secret:

            amount = args.amount * 10**8 # amount times ten to the power of eigth

            payload = {
                'secret' : secret,
                'recipientId' : args.dst_id,
                'amount' : int(amount)
                #'publicKey' : args.pubkey # needs pubkey to verify optional
            }

            print json.dumps(api.transactions(args.option,payload), indent=2)

def blocksget(api,args):

    payload = {'parameters' : args.q_params,
            'pubkey' : args.pubkey,
        }

    print json.dumps(api.blocks(args.option,payload), indent=2)

def delegatesget(api,args):

    payload = {
        'pubkey' : args.pubkey, #forged and delegate_voters
        'id' : args.all_id, #delegate_by_tx
        'address' : args.wallet,
        'parameters' : args.q_params
            }
    print json.dumps(api.delegates(args.option,payload), indent=2)

def delegatespost(api,args,secret):

    #For forging
    payload = { 'secret' : secret }
    print json.dumps(api.delegates(args.option,payload), indent=2)

def delegatesput(api,args,secret):

    payload = {
            'secret': secret,
            'username' : args.username
        }
    print json.dumps(api.delegates(args.option,payload), indent=2)

def usernameput(api,args,secret,secret2):

    payload = {
            'secret': secret,
            'username' : args.username
        }

    if args.second_passphrase:

        payload['secondSecret'] = secret2

    print json.dumps(api.usernames(args.option,payload), indent=2)

def contactget(api,args):

    payload = {
            'pubkey' : args.pubkey
        }

    print json.dumps(api.contacts(args.option,payload), indent=2)

def contactput(api,args,secret,secret2):

    payload = {
            'secret' : secret
        }

    if args.second_passphrase == True:

        payload['secondSecret'] = secret2

    if args.username and not args.wallet:

        payload['following'] = "+{}".format(args.username)

    elif args.wallet and not args.username:

        payload['following'] = "+{}".format(args.wallet)

    else:

        print 'Options Missmatch, Please choose a destination wallet or name'
        exit(1)

    print json.dumps(api.contacts(args.option,payload), indent=2)


def main():

    parser = argparse.ArgumentParser(description='LISK API Interface')
    parser.add_argument('-o','--option',dest='option',action='store',
        required=True,help='Query option')

    parser.add_argument('-w','--wallet',dest='wallet',action='store',
        help='Wallet')

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

    parser.add_argument('--username',dest='username',action='store',
        default='',help='Username/delegate name')

    parser.add_argument('-s','--secret',dest='secret',action='store_true',
        default=False,help='secret pass phrase')

    parser.add_argument('-2s','--second-secret',dest='second_passphrase',action='store_true',
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

    passphrase_options = ['enable_forging','disable_forging','send',
        'genpub','open_account','vote','register_delegate',
        'register_username','add_contact']

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

    secret = ''
    secret2 = ''

    if args.secret == True or args.option in passphrase_options:

        secret = getpass.getpass()
        print "Confirming the passphrase. Please type it again."
        secret1 = getpass.getpass()

        # Simple check. needs revamp
        if secret != secret1:

            print "Passprase does not match. Please try again"
            exit(1)

        if args.second_passphrase:

            print "\nPlease enter your second passphrase:"
            secret2 = getpass.getpass()
            print "Confirming the passphrase. Please type it again."
            secret3 = getpass.getpass()

            if secret2 != secret3:

                print "Passprase does not match. Please try again"
                exit(1)


    # Instanciate
    api = liskAPI.liskAPI(args.url)

    targets = {
            'get_lodr' : ['sync','status'],
            'get_acct' : ['balance','account','delegates_by_account','pubkey'],
            'put_acct' : ['genpub','vote','open_account'],
            'get_peer' : ['peer_ip','peer_list','peer_version'],
            'get_txid' : ['blocktx','get_tx','unconfirmed','unconfirmed_all'],
            'put_txid' : ['send'],
            'put_delg' : ['register_delegate'],
            'post_del' : ['disable_forging','enable_forging'],
            'get_delg' : ['forged',"delegate_list","delegate_by_tx","votes_by_account","delegate_voters"],
            'get_blk': ['my_blocks','blockid','all_blocks','fee','height'],
            'put_usrn' : ['register_username'],
            'get_cntc' : ['contacts','unconfirmed_contacts'],
            'put_cntc' : ['add_contact']
        }


    # Main selector
    if args.option in targets['get_lodr']:

        loader(api,args)

    # Accounts - balance and account works
    elif args.option in targets['get_acct']:

        accountget(api,args)

    elif args.option in targets['put_acct']:

        accountput(api,args,secret)

    # Peers - TODO: peer_ip -- DONE: peer_list, peer_version
    elif args.option in targets['get_peer']:

        peerget(api,args)

    # Transactions
    elif args.option in targets['get_txid']:

        transactionsget(api,args)

    elif args.option in targets['put_txid']:

        transactionput(api,args,secret)

    # Blocks
    elif args.option in targets['get_blk']:

        blocksget(api,args)

    #Delegates
    elif args.option in targets['get_delg']:

        delegatesget(api,args)

    elif args.option in targets['post_del']:

        delegatespost(api,args,secret)

    elif args.option in targets['put_delg']:

        delegatesput(api,args,secret)

    # Usernames
    elif args.option in targets['put_usrn']:

        usernameput(api,args,secret,secret2)

    # Contacts
    elif args.option in targets['get_cntc']:

        contactget(api,args)

    elif args.option in targets['put_cntc']:

        contactput(api,args,secret,secret2)

    # Hybrid call, my voters
    elif args.option == 'my_voters':

        print json.dumps(api.my_voters(args.wallet), indent=2)

if __name__ in '__main__':

    main()
