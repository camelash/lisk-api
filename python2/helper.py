#!/usr/bin/env python
'''
Helper script for the LiskAPI python library
'''

import json
import re
import sys
import math
import os.path
import argparse
import getpass
import liskAPI


def loader(api, args):
    '''Loader - sync and status of node'''
    print json.dumps(api.loader(args.option), indent=2)

def accountget(api, args):
    '''get account information'''
    payload = {
        'address' : args.wallet
    }

    print json.dumps(api.account(args.option, payload), indent=2)

def check2pass(api, args):
    '''Check if account has multi-phrase enabled '''

    pass

def accountput(api, args, account_info, secret, secret2):
    '''Account modification options '''

    payload = {}
    payload['secret'] = secret

    if secret2:
        payload['secondSecret'] = secret2

    if args.option == 'open_account' and secret:

        print json.dumps(api.account(args.option, payload), indent=2)

    if args.option == 'genpub' and secret:

        pseudobip = re.compile(r'^((\S{3,10})\s?){12,20}')

        if not re.search(pseudobip, secret) or len(secret) > 100:

            print """
                Secret must me Twelve words or mode and
                less than 100 characters"""
            exit(1)

        response = api.account(args.option, payload)

        key_s = response['publicKey']

        n_addr = api.account('open_account', payload)

        response['address'] = n_addr['account']['address']

        print json.dumps(response, indent=2)

    elif args.option == 'vote' and secret:

        hex_match = re.compile(r'^[A-Za-z0-9]{64}$')
        str_match = re.compile(r'^\S{1,20}$')
        add_match = re.compile(r'^[0-9]{15,20}L$')
        pubkey_list = []
        vote_type = ''

        if args.vote_no is True and not args.vote_yes:

            vote_type = '-'

        elif args.vote_yes is True and not args.vote_no:

            vote_type = '+'
        else:

            print "Vote method is not defined"
            exit(1)

        with open(args.vote_file) as vf_fh:

            for pkey in vf_fh:

                key_s = pkey.strip()

                if not key_s:
                    continue

                if re.search(hex_match, key_s):

                    pubkey_list.append("{}{}".format(vote_type, key_s))

                elif re.search(str_match, key_s) and not re.search(add_match, key_s):

                    name_get = {'parameters' : '/get?username={}'.format(key_s)}
                    n_addr = api.delegates('delegate_list', name_get)

                    try:
                        name_del_pubkey = n_addr['delegate']['publicKey']
                    except:
                        print 'Delegate {} not found. Skipping'.format(key_s)
                        continue

                    pubkey_list.append('{}{}'.format(vote_type, name_del_pubkey))

                elif re.search(add_match, key_s):

                    addr_get = {'address' : key_s}
                    r_addr = api.account('account', addr_get)

                    try:
                        addr_del_pubkey = r_addr['account']['publicKey']
                    except:
                        print 'Address {} not found. Skipping'.format(key_s)
                        continue

                    if addr_del_pubkey is None:
                        continue

                    pubkey_list.append('{}{}'.format(vote_type, addr_del_pubkey))

                else:

                    print "Found a non matching line in the file. Skipping:{}".\
                        format(key_s)

            if len(pubkey_list) <= 101:

                i = 0
                while i < 4:
                    lista = pubkey_list[0:33]
                    del pubkey_list[:33]
                    i += 1

                    if args.vote_yes:
                        pubkey_list_clean = voterscheck(api, account_info, lista,
                                                        vote_type)
                        payload['delegates'] = pubkey_list_clean

                    else:

                        payload['delegates'] = lista

                    if len(lista) == 0:

                        exit(1)

                    else:

                        print json.dumps(api.account(args.option, payload), indent=2)

                exit(1)

            elif len(pubkey_list) > 101:

                print "Voter list contains more than 101 addresses"
                exit(1)

    else:
        print "Accounts Errors"
        exit(1)

def voterscheck(api, account_info, pubkey_list, vote_type):
    ''' Check if account has voted for delegate'''

    account_wallet = str(account_info['account']['address'])
    payload = {'address' : account_wallet}
    voter_votes = api.delegates('votes_by_account', payload)

    for delegate in voter_votes['delegates']:

        delegate_pkey = '{}{}'.format(vote_type, delegate['publicKey'])

        if delegate_pkey in pubkey_list:

            pubkey_list.remove(delegate_pkey)
            print 'Already voted for {}. Removing from list'.format(\
                delegate['username'])

    return pubkey_list

def peerget(api, args):
    '''get peer information'''

    payload = {
        "ip" : "127.0.0.1",
        "port" : 7000,
        "parameters" : args.q_params
        }
    print json.dumps(api.peers(args.option, payload), indent=2)

def transactionsget(api, args):
    '''get transaction information'''

    payload = {
        'id':args.all_id,
        'parameters' : args.q_params
        }

    print json.dumps(api.transactions(args.option, payload), indent=2)

def transactionput(api, args, secret, secret2):
    ''' transaction modification options'''

    if args.option == 'send' and secret:

        amountstr = str(args.amount)

        strsplit = amountstr.split('.')

        if len(strsplit[1]) > 8:

            print "Invalid decimal places. Ex: 1.12345678"

            exit(1)

        amount = args.amount * math.pow(10, 8) # amount times ten to the power of eigth

        payload = {
            'secret' : secret,
            'recipientId' : args.dst_id,
            'amount' : int(math.ceil(amount))
        }

        if secret2:

            payload['secondSecret'] = secret2

        print json.dumps(api.transactions(args.option, payload), indent=2)

def blocksget(api, args):
    '''get block information'''

    payload = {
        'parameters' : args.q_params,
        'pubkey' : args.pubkey,
        }

    print json.dumps(api.blocks(args.option, payload), indent=2)

def delegatesget(api, args):
    '''get delegate information'''

    payload = {
        'pubkey' : args.pubkey, #forged and delegate_voters
        'id' : args.all_id, #delegate_by_tx
        'address' : args.wallet,
        'parameters' : args.q_params
        }
    print json.dumps(api.delegates(args.option, payload), indent=2)

def delegatespost(api, args, secret):
    ''' delegate modification options'''

    #For forging
    payload = {'secret' : secret}
    print json.dumps(api.delegates(args.option, payload), indent=2)

def delegatesput(api, args, secret):
    ''' delegate modification options '''

    payload = {
        'secret': secret,
        'username' : args.username
        }
    print json.dumps(api.delegates(args.option, payload), indent=2)

def usernameput(api, args, secret, secret2):
    ''' username modification options'''

    payload = {
        'secret': secret,
        'username' : args.username
        }

    if secret2:

        payload['secondSecret'] = secret2

    print json.dumps(api.usernames(args.option, payload), indent=2)

def contactget(api, args):
    ''' get contact information '''

    payload = {
        'pubkey' : args.pubkey
        }

    print json.dumps(api.contacts(args.option, payload), indent=2)

def contactput(api, args, secret, secret2):
    ''' contact modification options '''

    payload = {
        'secret' : secret
        }

    if secret2:

        payload['secondSecret'] = secret2

    if args.username and not args.wallet:

        payload['following'] = "+{}".format(args.username)

    elif args.wallet and not args.username:

        payload['following'] = "+{}".format(args.wallet)

    else:

        print 'Options Missmatch, Please choose a destination wallet or name'
        exit(1)

    print json.dumps(api.contacts(args.option, payload), indent=2)


def signatureput(api, args, secret, secret2):
    ''' signature modification options'''

    pseudobip = re.compile(r'^((\S{3,10})\s?){12,20}')

    if not re.search(pseudobip, secret) or len(secret) > 100:

        print """
            Secret must me Twelve words or mode and
            less than 100 characters"""
        exit(1)

    payload = {
        'secret' : secret,
        'secondSecret' : secret2
        }

    print json.dumps(api.signatures(args.option, payload), indent=2)

def main():
    ''' main fuction logic '''

    parser = argparse.ArgumentParser(description='LISK API Interface')
    parser.add_argument('-o', '--option', dest='option', action='store',
                        required=True, help='Query option')

    parser.add_argument('-w', '--wallet', dest='wallet', action='store',
                        help='Wallet')

    parser.add_argument('-k', '--key', dest='pubkey', action='store',
                        help='Public Key')

    parser.add_argument('-u', '--url', dest='url', action='store',
                        default='http://localhost:8000',
                        help='Url in format: http://localhost:8000')

    parser.add_argument('-vf', '--vote-file', dest='vote_file', action='store',
                        default='votelist.txt', help='Load Vote File')

    parser.add_argument('-dstid', '--destination-id', dest='dst_id', action='store',
                        help='Destination Id or address')

    parser.add_argument('-a', '--amount', dest='amount', action='store',
                        type=float, help='amount to send')

    parser.add_argument('--username', dest='username', action='store',
                        default='', help='Username/delegate name')

    parser.add_argument('-s', '--secret', dest='secret', action='store_true',
                        default=False, help='secret pass phrase')

    parser.add_argument('-2s', '--second-secret', dest='second_passphrase',
                        action='store_true', default=False, help='secret pass phrase')

    parser.add_argument('--vote-no', dest='vote_no', action='store_true',
                        default=False, help='secret pass phrase')

    parser.add_argument('--vote-yes', dest='vote_yes', action='store_true',
                        default=False, help='secret pass phrase')

    parser.add_argument('-p', '--parameters', dest='q_params', action='store',
                        default='', help='query parameters')

    parser.add_argument('-id', '--id', dest='all_id', action='store',
                        default='', help='tx id or block id')

    args = parser.parse_args()

    passphrase_options = ['enable_forging', 'disable_forging', 'send',
                          'genpub', 'open_account', 'vote', 'register_delegate',
                          'register_username', 'add_contact', 'gen_2_sig']

    twopassphrase_options = ['vote', 'gen_2_sig', 'open_account', 'send']

    if not args.option:

        parser.print_help()

    # Instanciate
    api = liskAPI.liskAPI(args.url)

    if args.option == 'vote' and args.vote_file:

        if os.path.isfile(args.vote_file) is False and not args.vote_yes\
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

    if args.secret is True or args.option in passphrase_options:

        secret = getpass.getpass()
        print "Confirming the passphrase. Please type it again."
        secret1 = getpass.getpass()

        # Simple check. needs revamp
        if secret != secret1:

            print "Passprase does not match. Please try again"
            exit(1)

        account_payload = {"secret" : secret}
        account_info = api.account('open_account', account_payload)

        if account_info['account']['secondSignature'] == 1 and \
                args.option in twopassphrase_options:

            print "\nPlease enter your second passphrase:"
            secret2 = getpass.getpass()
            print "Confirming the passphrase. Please type it again."
            secret3 = getpass.getpass()

            if secret2 != secret3:

                print "Passprase does not match. Please try again"
                exit(1)


    targets = {
        'get_lodr' : ['sync', 'status'],
        'get_acct' : ['balance', 'account', 'delegates_by_account', 'pubkey'],
        'put_acct' : ['genpub', 'vote', 'open_account'],
        'get_peer' : ['peer_ip', 'peer_list', 'peer_version'],
        'get_txid' : ['blocktx', 'get_tx', 'unconfirmed', 'unconfirmed_all'],
        'put_txid' : ['send'],
        'put_delg' : ['register_delegate'],
        'post_del' : ['disable_forging', 'enable_forging'],
        'get_delg' : ['forged', "delegate_list", "delegate_by_tx",
                      "votes_by_account", "delegate_voters"],
        'get_blk': ['my_blocks', 'blockid', 'all_blocks', 'fee', 'height'],
        'put_usrn' : ['register_username'],
        'get_cntc' : ['contacts', 'unconfirmed_contacts'],
        'put_cntc' : ['add_contact'],
        'put_sign' : ['gen_2_sig'],
        'get_sign' : ['get_signature']
        }


    # Main selector
    if args.option in targets['get_lodr']:

        loader(api, args)

    # Accounts - balance and account works
    elif args.option in targets['get_acct']:

        accountget(api, args)

    elif args.option in targets['put_acct']:

        accountput(api, args, account_info, secret, secret2)

    # Peers - TODO: peer_ip -- DONE: peer_list, peer_version
    elif args.option in targets['get_peer']:

        peerget(api, args)

    # Transactions
    elif args.option in targets['get_txid']:

        transactionsget(api, args)

    elif args.option in targets['put_txid']:

        transactionput(api, args, secret, secret2)

    # Blocks
    elif args.option in targets['get_blk']:

        blocksget(api, args)

    #Delegates
    elif args.option in targets['get_delg']:

        delegatesget(api, args)

    elif args.option in targets['post_del']:

        delegatespost(api, args, secret)

    elif args.option in targets['put_delg']:

        delegatesput(api, args, secret)

    # Usernames
    elif args.option in targets['put_usrn']:

        usernameput(api, args, secret, secret2)

    # Contacts
    elif args.option in targets['get_cntc']:

        contactget(api, args)

    elif args.option in targets['put_cntc']:

        contactput(api, args, secret, secret2)

    elif args.option in targets['put_sign']:

        signatureput(api, args, secret, secret2)

    # Hybrid call, my voters
    elif args.option == 'my_voters':

        if not args.wallet:

            print "No wallet address specified"
            sys.exit(1)

        else:

            #print json.dumps(api.my_voters(args.wallet), indent=2)
            voters = api.my_voters(args.wallet)

            print "{} {} {}".format("Address", "Name", "Balance")
            total_balance = 0

            for voter in voters['accounts']:

                bal = int(voter['balance']) / 100000000
                total_balance += bal

                print "{:25} {:20} {}".format(voter['address'],
                                              voter['username'],
                                              bal)

            print "\nTotal Balance: {} Total Addresses: {}".\
                format(total_balance,len(voters['accounts']))



if __name__ in '__main__':

    main()
