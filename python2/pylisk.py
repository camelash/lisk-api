#!/usr/bin/env python

import json
import requests
import re
import sys
import math
import os.path
import argparse
import getpass


class liskAPI(object):

    def __init__(self,rturl=''):

        self.headers = {'content-type': 'application/json'}
        self.target_url = rturl

        try:

            r = requests.get("{}/api/loader/status".format(self.target_url))

        except requests.exceptions.ConnectionError as e:

            if 'port=8000' in str(e.message):

                print "Connection error. Cannot communicate with port 8000"
                print "The default option is mainnet for testnet add " \
                      + "--testnet"
                sys.exit(1)

            elif 'port=7000' in str(e.message):

                print "Cannot communicate with port 7000. Is LISK running?"
                sys.exit(1)

            else:

                print "Unknown Connection Error"
                sys.exit(1)


    @staticmethod
    def get_check(url):

        r = requests.get(url)

        if r.status_code == 200:

            return json.loads(r.text)

        else:

            error = {'errcode': r.status_code}

            return error

    @staticmethod
    def put_check(url,payload,headers):

        r = requests.put(url, data=json.dumps(payload),
            headers=headers)

        if r.status_code == 200:

            return json.loads(r.text)

        else:

            error = {
                'errcode': r.status_code,
                'error' : r
                }

            return error

    @staticmethod
    def post_check(url,payload,headers):

        r = requests.post(url, data=json.dumps(payload),
            headers=headers)

        if r.status_code == 200:

            return json.loads(r.text)

        else:

            error = {
                'errcode': r.status_code,
                'error' : r
                }

            return error

    def account(self,rtype,payload={}):

        targets = {
                # Open account in wallet.
                # POST /api/accounts/open
                'open_account' : '/api/accounts/open',
                # Get balance of account.
                # GET /api/accounts/getBalance?address=address
                'balance' : '/api/accounts/getBalance?address=',
                # Get public key of account. 
                # GET /api/accounts/getPublicKey?address=address
                'pubkey' : '/api/accounts/getPublicKey?address=',
                # Will return public key of provided secret key.
                # POST /api/accounts/generatePublicKey
                'genpub' : '/api/accounts/generatePublicKey',
                # Will return account by address.
                # GET /api/accounts?address=address
                'account' : '/api/accounts?address=',
                # Will return account's delegates by address.
                # GET /api/accounts/delegates?address=address 
                'delegates_by_account' : '/api/accounts/delegates?address=',
                # Will vote for selected delegates.
                # PUT /api/accounts/delegates
                'vote' : '/api/accounts/delegates',
            }

        req_methods = {
                'get' : ['balance','account','pubkey','delegates_by_account'],
                'put' : ['vote'],
                'post' : ['genpub','open_account']
            }

        url = self.target_url + targets[rtype]

        if rtype in req_methods['get']:

            if not payload['address']:

                return "Address not defined"

            else:

                url = self.target_url + targets[rtype] + payload['address']

                return self.get_check(url)

        elif rtype in req_methods['put']:

            return self.put_check(url,payload,self.headers)

        elif rtype in req_methods['post']:

            r = requests.post(url, data=json.dumps(payload),
                headers=self.headers)

            return json.loads(r.text)

        else:

            return "Option not recognized"


    def loader(self,rtype):

        targets = {
                # Will return account's delegates by address.
                # GET /api/loader/status
                'status' : '/api/loader/status',
                # Get synchronization status of wallet.
                # GET /api/loader/status/sync
                'sync' : '/api/loader/status/sync',
            }

        url = self.target_url + targets[rtype]

        return  self.get_check(url)


    def transactions(self,rtype,payload={}):

        targets = {
                # Transactions list matched by provided parameters.
                # GET /api/transactions?blockId=blockId&senderId=senderId&
                # recipientId=recipientId&limit=limit&offset=offset&orderBy=field
                'blocktx' : '/api/transactions',
                # Send transaction to broadcast network.
                # PUT /api/transactions
                'send' : '/api/transactions',
                # Transaction matched by id.
                # GET /api/transactions/get?id=id
                'get_tx' : '/api/transactions/get?id=',
                # Get unconfirmed transaction by id.
                # GET /api/transactions/unconfirmed/get?id=
                'unconfirmed' : '/api/transactions/unconfirmed/get?id=',
                # Get list of unconfirmed transactions.
                # GET /api/transactions/unconfirmed
                'unconfirmed_all' : '/api/transactions/unconfirmed',
            }


        req_methods = {
               'get' : ['blocktx','get_tx','unconfirmed','unconfirmed_all'],
               'put' : ['send']
            }

        url = self.target_url + targets[rtype]

        if rtype in req_methods['get']:

            if payload['id'] and not payload['parameters']:

                url += payload['id']

            elif payload['parameters'] and not payload['id']:

                url += payload['parameters']

            elif not payload['id'] and not payload['parameters']:
                pass

            return self.get_check(url)

        elif rtype in req_methods['put']:

            return self.put_check(url,payload,self.headers)

        else:

            return "Option Not Recognized"


    def peers(self,rtype,payload={}):

        targets = {
                # Get peers list by parameters.
                # GET /api/peers?state=state&os=os&shared=shared&
                # version=version&limit=limit&offset=offset&orderBy=orderBy
                'peer_list' : '/api/peers',
                # Get peer by ip and port
                # GET /api/peers/get?ip=ip&port=port
                'peer_ip' : '/api/peers/get?ip="{}"&port={}'.\
                    format(payload['ip'],payload['port']),
                # Get peer version and build time
                # GET /api/peers/version
                'peer_version' : '/api/peers/version',
            }


        url = '{}{}'.format(self.target_url,targets[rtype])

        if payload['parameters']:

             url = '{}{}'.format(url,payload['parameters'])

        return self.get_check(url)


    def blocks(self,rtype,payload={}):

        targets = {
                # Get block by id.
                # GET /api/blocks/get?id=id
                'blockid' : '/api/blocks/get?id=',
                # Get all blocks.
                # GET /api/blocks?generatorPublicKey=generatorPublicKey
                # &height=height&previousBlock=previousBlock&totalAmount=totalAmount
                # &totalFee=totalFee&limit=limit&offset=offset&orderBy=orderBy
                'all_blocks' : '/api/blocks',
                # Get blockchain fee percent
                # GET /api/blocks/getFee
                'fee' : '/api/blocks/getFee',
                # Get blockchain height
                # GET /api/blocks/getHeight
                'height' : '/api/blocks/getHeight',
                #
                'my_blocks' : '/api/blocks?generatorPublicKey=',
            }

        get = ['my_blocks','blockid','all_blocks','fee','height']

        url = self.target_url + targets[rtype]

        if rtype in get:

            if rtype == 'blockid' or rtype == 'all_blocks':

                url += payload['parameters']

            elif rtype == 'my_blocks':

                url += payload['pubkey']

        return self.get_check(url)


    def signatures(self,rtype,payload={}):

	targets = {

            # Get second signature of account.
            # GET /api/signatures/get?id=id
            'get_signature' : '/api/signatures/get?id=',

            # Add second signature to account.
            # PUT /api/signatures
            'gen_2_sig' : '/api/signatures',

        }

        request_method = {
                'get' : ['get_signature'],
                'put' : ['gen_2_sig']
            }

        url = self.target_url + targets[rtype]

        if rtype in request_method['get']:

            url = self.target_url + targets[rtype] + payload['id']

            return self.get_check(url)

        elif rtype in request_method['put']:

            return self.put_check(url,payload,self.headers)

    def delegates(self,rtype,payload={}):

        targets = {

                # Enable delegate on account
                # PUT /api/delegates
                'register_delegate' : '/api/delegates',

                # Get delegates list.
                # GET /api/delegates?limit=limit&offset=offset&orderBy=orderBy
                'delegate_list' : '/api/delegates',

                # Get delegate by transaction id.
                # GET /api/delegates/get?id=transactionId
                'delegate_by_tx' : '/api/delegates/get?id=',

                # Get votes by account address.
                # GET /api/accounts/delegates/?address=address
                'votes_by_account' : '/api/accounts/delegates/?address=',

                # Enable forging
                # POST /api/delegates/forging/enable
                'enable_forging' : '/api/delegates/forging/enable',

                # Disable forging
                # POST /api/delegates/forging/disable
                'disable_forging' : '/api/delegates/forging/disable',

                # Get voters of delegate.
                # GET /api/delegates/voters?publicKey=publicKey
                'delegate_voters' : '/api/delegates/voters?publicKey=',

                # Get forged by account
                # Get amount forged by account.
                'forged' : '/api/delegates/forging/getForgedByAccount?generatorPublicKey=',
            }

        request_method = {
                'get' : ['delegate_list','delegate_by_tx','votes_by_account',
                    'forged','delegate_voters'],
                'put' : ['register_delegate'],
                'post' : ['enable_forging','disable_forging']
                }

        url = self.target_url + targets[rtype]

        if rtype in request_method['get']:

            if rtype == 'delegate_by_tx':

                url += payload['id']

            elif rtype == 'votes_by_account':

                url += payload['address']

            elif rtype == 'delegate_voters' or rtype in 'forged':

                url += payload['pubkey']

            elif rtype == 'delegate_list':

                url += payload['parameters']

            return self.get_check(url)

        elif rtype in request_method['put']:

            if 'secret' in payload and 'username' in payload:

                return self.put_check(url,payload,self.headers)

            else:

                error = {'liskAPI': 'Dictionary does not contain required items'}
                return error

        elif rtype in request_method['post']:

            r = requests.post(url, data=json.dumps(payload),
                headers=self.headers)

            return json.loads(r.text)

    def messages(self,rtype,payload):

        # Not working
        targets = {

                # Send message to recipient.
                # PUT /api/messages
                'send_message' : '/api/messages',
            }

        url = self.target_url + targets[rtype]

        return self.put_check(url,payload,self.headers)

    def usernames(self,rtype,payload):

        targets = {
                # Register username.
                # PUT /api/accounts/username
                'register_username' : '/api/accounts/username'
            }

        url = self.target_url + targets[rtype]

        return self.put_check(url,payload,self.headers)

    def contacts(self,rtype,payload):

        targets = {
                # Add contact
                # PUT /api/contacts
                'add_contact' : '/api/contacts',
                # Get contacts of account by public key.
                # GET /api/contacts/?publicKey=publicKey
                'contacts' : '/api/contacts/?publicKey=',
                # Get unconfirmed contacts of account by public key.
                # /api/contacts/unconfirmed?publicKey=publicKey
                'unconfirmed_contacts' : '/api/contacts/unconfirmed?publicKey='
            }

        request_method = {
                'get' : ['contacts','unconfirmed_contacts'],
                'put' : ['add_contact']
            }

        if rtype in request_method['get']:

            url = '{}{}{}'.format(self.target_url,targets[rtype],payload['pubkey'])

            return self.get_check(url)

        elif rtype in request_method['put']:

            url = '{}{}'.format(self.target_url,targets[rtype])

            return self.put_check(url,payload,self.headers)


    def blockchainapp(self, rtype, payload):

        targets = {
            # Gets a list of apps registered on the network.
            # GET /api/dapps?category=category&name=name&type=type&link=link&
            # limit=limit&offset=offset&orderBy=orderBy
            'app_list' : '/api/dapps',
            # Gets a specific app by id.
            # GET /api/dapps/get?id=id
            'get_app' : '/api/dapps/get?id=',
            # Searches for apps by keyword(s).
            # GET /api/dapps/search?q=q&category=category&installed=installed
            'app_search' : '/api/dapps/search',
            # Returns a list of installed apps on the requested node.
            # GET /api/dapps/installed
            'installed_apps' : '/api/dapps/installed',
            # Returns a list of installed app ids on the requested node.
            # GET /api/dapps/installedIds
            'installed_appsid' : '/api/dapps/installedIds',
            # Returns a list of app ids currently being installed on the requested node.
            # GET /api/dapps/installing
            'installing_apps' : '/api/dapps/installing',
            # Returns a list of app ids currently being uninstalled on the requested node.
            # GET /api/dapps/uninstalling
            'uninstalling_apps' : '/api/dapps/uninstalling',
            # Returns a list of app ids which are currently launched on the requested node.
            # GET /api/dapps/launched
            'launched_apps' : '/api/dapps/launched',
            # Returns a full list of app categories.
            # GET /api/dapps/categories
            'app_categories' : '/api/dapps/categories',
            # Registers a app.
            # PUT /api/dapps
            'register_app' : '/api/dapps',
            # Installs a app by id on the node.
            # POST /api/dapps/install
            'install_app' : '/api/dapps/install',
            # Uninstalls a app by id from the requested node.
            # POST /api/dapps/uninstall
            'uninstall_app' : '/api/dapps/uninstall',
            # Launches a app by id on the requested node.
            # POST /api/dapps/launch
            'launch_app' : '/api/dapps/launch',
            # Stops a app by id on the requested node.
            # POST /api/dapps/stop
            'stop_app' : '/api/dapps/stop',

            }

        request_method = {
            'get' : ['app_list','get_app','app_search','installed_apps','installed_appsid',
                    'installing_apps','uninstalling_apps','launched_apps','app_categories'],
            'put' : ['register_app'],
            'post' : ['install_app','uninstall_app','launch_app','stop_app'],
        }

        url = self.target_url + targets[rtype]

        if rtype in request_method['get']:

            if rtype == 'get_app':

                url += payload['id']

            elif rtype == 'app_list' or rtype == 'app_search':

                url += payload['parameters']

            return self.get_check(url)

        elif rtype in request_method['put']:

            if 'secret' in payload and 'username' in payload:

                error = {'error':'not yet implemented'}
                return error
                return self.put_check(url,payload,self.headers)

            else:

                error = {'liskAPI': 'Dictionary does not contain required items'}
                return error

        elif rtype in request_method['post']:

            error = {'error':'not yet implemented'}
            return error

            r = requests.post(url, data=json.dumps(payload),
                headers=self.headers)

            return json.loads(r.text)


    def multisig(self,rtype,payload):

        targets = {
            # Return multisig transaction that waiting for your signature.
            # GET /api/multisignatures/pending?publicKey=publicKey
            'my_multisig' : '/api/multisignatures/pending?publicKey=',
            # Get accounts of multisignature.
            # GET /api/multisignatures/accounts?publicKey=publicKey
            'multisig_accounts' : '/api/multisignatures/accounts?publicKey=',
            # Sign transaction that wait for your signature.
            # POST /api/multisignatures/sign
            'sign_tx' : '/api/multisignatures/sign',
            # Create a multisignature account.
            # PUT /api/multisignatures
            'create_multisig' : '/api/multisignatures',
        }

        request_method = {
            'get' : ['my_multisig','multisig_accounts'],
            'put' : ['create_multisig'],
            'post' : ['sign_tx'],
        }

        if rtype in request_method['get']:

            url = '{}{}{}'.format(self.target_url, targets[rtype],
                                  payload['pubkey'])

            return self.get_check(url)

        elif rtype in request_method['put']:

            url = '{}{}'.format(self.target_url,targets[rtype])

            return self.put_check(url,payload,self.headers)

        elif rtype in request_method['post']:

            url = '{}{}'.format(self.target_url,targets[rtype])

            return self.post_check(url,payload,self.headers)

    # Custom Wrappers

    def autoaccount(self):
        # Combine account generation and username generation. 
        pass

    def autoname(self, delegate):
        '''Give a username get account information'''

        payload = {'parameters':'/get?username={}'.format(delegate)}
        delegate_info = self.delegates('delegate_list',payload)

        return delegate_info

    def my_voters(self,wallet):

        ## Get my voters
        account_payload = { 'address' : wallet }
        voters_payload = {}

        ## Get the public key
        pkey = self.account('pubkey',account_payload)

        voters_payload['pubkey'] = pkey['publicKey']

        ## Get your voters
        voters = self.delegates('delegate_voters',voters_payload)

        return voters

    def forge_check(self,delegate):
        ''' check forging status '''

        # First grab public key from delegate name
        payload = {'parameters':'/get?username={}'.format(delegate)}
        delegate_info = self.delegates('delegate_list',payload)

        pubkey = delegate_info['delegate']['publicKey']

        response = requests.get('{}/api/delegates/forging/status?publicKey={}'\
                                .format(self.target_url, pubkey))

        return json.loads(response.text)

def loader(api, args):
    '''Loader - sync and status of node'''
    print json.dumps(api.loader(args.option), indent=2)

def forge_check(api, args):
    '''Check forging status'''
    print json.dumps(api.forge_check(args.username), indent=2)

def autoname(api, args):
    '''Get delegate info by delegate name'''
    print json.dumps(api.autoname(args.username), indent=2)

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

    elif args.option == 'genpub' and secret:

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

def multisigget(api, args):
    ''' get multisignature information '''

    payload = {
        'pubkey' : args.pubkey
        }

    print json.dumps(api.multisig(args.option, payload), indent=2)

def multisigput(api, args, secret, secret2):
    ''' put multisignature information '''

    # keys group could be a file or a space separated field with delegatenames
    keysgroup = []
    for delegate in args.keysgroup:

        response = api.autoname(delegate)

        if response['success'] == False:

            print "Error, cannot continue. Delegate {} not found"\
                      .format(delegate)
            sys.exit(1)

        else:

            keysgroup.append('+{}'.format(response['delegate']['publicKey']))

    payload = {
        'secret' : secret,
        'lifetime' : args.lifetime, #request lifetime in hours
        'min' : args.minimum,       #mine sigs needed to approve
        'keysgroup' : keysgroup     #array of pubkeys + or -
        }

    if secret2:

        payload['secondSecret'] = secret2

    print json.dumps(api.multisig(args.option, payload), indent=2)

def multisigpost(api, args, secret, secret2):
    ''' post multisignature information '''

    payload = {
        'secret' : secret,
        'transactionId' : args.all_id
        }

    if secret2:

        payload['secondSecret'] = secret2

    print json.dumps(api.multisig(args.option, payload), indent=2)

def appget(api, args):
    ''' get application information '''

    payload = {
        'id' : args.all_id,
        'parameters' : args.q_params
        }

    if args.option == 'get_app' and not payload['id']:

        print "ID needed --id 12345"
        sys.exit(1)

    elif args.option == 'app_search' and not payload['parameters']:

        print "Parameters needed --parameters ?q=test"
        sys.exit(1)

    print json.dumps(api.blockchainapp(args.option, payload), indent=2)

def usage():

    return '''

    ##### Account options ###################################

    ## Show information of an account (requires secret)
    pylisk open_account

    ## Get the balance of an account by wallet address
    pylisk balance --wallet <wallet address L>

    ## Get the publicKey of an account by wallet address
    pylisk pubkey --wallet <wallet address L>

    ## Generate an account based on secret (requires secret)
    pylisk genpub

    ## Get account information based on wallet address
    pylisk account --wallet <wallet address L>

    ## Get delegates by account wallet address
    pylisk delegates_by_account --wallet <wallet address L>

    ## Vote for accounts in a file.
    ## File can be pubkey, delegate name or wallet address
    pylisk vote --vote-file 33.txt --vote-yes

    ## Unvote
    pylisk vote --vote-file 33.txt --vote-no

    ##### Loader options ####################################

    ## Get full peer list
    pylisk peer_list

    ## Get peers filtered
    pylisk peer_list --parameters "?version=0.5.1b"

    ## Get the version of a peer (can be used with the --url flag)
    pylisk peer_version

    ## Get peer information by IP (work in progress)
    pylisk peer_ip

    ##### Block options #####################################

    ## Get block by id
    pylisk blockid --parameters <block id>

    ## Get all blocks
    pylisk all_blocks

    ## Get blocks fileters by parameters
    pylisk all_blocks --parameters "?offset=0&limit=2"

    ## Get fee details
    pylisk fee

    ## Get block height
    pylisk height

    ## Get my forged blocks (custom search)
    pylisk my_blocks --key <publicKey>

    ##### Transaction options ################################

    ## Get information of a block by blockId
    pylisk blocktx --parameters "?blockId=<block Id>"

    ## Send a transaction with 1 lisk to specified recipient
    pylisk send --destination-id slasheks --amount 1

    ## Get information on a transaction ID
    pylisk get_tx --id <transaction id>

    ## Get information on an unconfirmed transaction by ID
    pylisky unconfirmed --id <transaction id>

    ## Get all unconfirmed transactions
    pylisk unconfirmed_all

    ##### Delegate options #####################################

    ## Disable forging on the localhost (can be used with the --url flag,
    ##  Requires secret)
    pylisk disable_forging

    ## Enable forging on the localhost (can be used with the --url flag,
    ## Requires secret)
    pylisk enable_forging

    ## Delegate list filtered (order by rank only display 2)
    pylisk delegate_list -p "?orderBy=rate&limit=2"

    ## Get the delegate votes based on public key of an account
    pylisk delegate_voters --key <pubKey>

    ## Get forged information on an account based on public key
    pylisk forged --key <pubkey>

    ## Register a delegate name (requires secret)
    pylisk register_delegate --username slasheks_api

    ##### Contacts ############################################

    ## Get the contacts of an account by publiKey
    pylisk contacts --key <pubkey>

    ## Get unconfirmed contacts based on publicKey
    pylisk unconfirmed_contacts --key <pubkey>

    ## Contact request (requires secret)
    pylisk add_contact --username slasheks2

    ##### Multisignature options ##############################

    ## Get information on a multisignature account
    pylisk my_multisig --key <pubkey>

    ## Create a multisignature account
    pylisk create_multisig --lifetime 1 --minimum 2 --keysgroup slasheks gr33nDrag0n 

    ## Sign a multisignature transaction
    pylisk sign_tx --id <txId>

    ##### Blockchain App options ###############################

    ## Get application lisk
    pylisk app_list

    ## Get Blockchain App by Transaction ID
    pylisk get_app --id <txId>

    ## Search for apps (Variable parameter option)
    pylisk app_search --parameter "?q=installed=1"

    ## Get installed blockchain applications
    pylisk installed_apps

    ## Get the IDs of installed blockchain applications
    pylisk installed_appsid

    ## Get apps that are currently installing
    pylisk installing_apps

    ## Get bblockchain applications that are uninstalling
    pylisk uninstalling_apps

    ## Get all the launched apps
    pylisk launched_apps

    ## Get the blockchain application categories
    pylisk app_categories
    '''

def main():
    ''' main fuction logic '''

    parser = argparse.ArgumentParser(description='LISK API Interface',
                                     usage=usage())

    parser.add_argument(dest='option', action='store', help='Query option')

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

    parser.add_argument('-s', '--secret', dest='secret', action='store',
                        help='secret pass phrase')

    parser.add_argument('--certificate', dest='cert', action='store',
                        help='If https unsigned cert, point to local cert')

    parser.add_argument('--vote-no', dest='vote_no', action='store_true',
                        default=False, help='secret pass phrase')

    parser.add_argument('--vote-yes', dest='vote_yes', action='store_true',
                        default=False, help='secret pass phrase')

    parser.add_argument('-p', '--parameters', dest='q_params', action='store',
                        default='', help='query parameters')

    parser.add_argument('-id', '--id', dest='all_id', action='store',
                        default='', help='tx id or block id')

    # Testnet flag
    parser.add_argument('-t', '--testnet', dest='testnet', action='store_true',
                        default=False, help='Changes URL to testnet')

    # Multisig
    parser.add_argument('--lifetime', dest='lifetime', action='store',
                        type=int,help='request lifetime')

    parser.add_argument('--minimum', dest='minimum', action='store',
                        type=int,help='Min amount of signatures needed')

    parser.add_argument('--keysgroup', dest='keysgroup', action='store',
                        nargs='+',help='Min amount of signatures needed')

    args = parser.parse_args()

    passphrase_options = ['enable_forging', 'disable_forging', 'send',
                          'genpub', 'open_account', 'vote', 'register_delegate',
                          'register_username', 'add_contact', 'gen_2_sig',
                          'create_multisig','sign_tx']

    twopassphrase_options = ['vote', 'gen_2_sig', 'open_account', 'send',
                             'create_multisig','sign_tx']

    if not args.option:

        parser.print_help()
        sys.exit(1)

    if args.testnet is True:

        url = args.url.split(':')

        args.url = '{}:{}:{}'.format(url[0],url[1],'7000')

    if args.cert:

        os.environ['REQUESTS_CA_BUNDLE'] = args.cert

    # Instanciate
    api = liskAPI(args.url)

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

    secret = None
    secret2 = None

    if args.secret or args.option in passphrase_options:

        try:

            secret = os.environ['LISK_SECRET']

        except KeyError:

            pass

        if secret:

            pass

        elif args.secret:

            secret = args.secret

        else:

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
        'get_sign' : ['get_signature'],
        'get_delc' : ['forge_check'],
        'get_mlts' : ['my_multisig','multisig_account'],
        'post_mlts' : ['sign_tx'],
        'put_mlts' : ['create_multisig'],
        'get_apps' : ['app_list','get_app','app_search','installed_apps','installed_appsid',
                      'installing_apps','uninstalling_apps','launched_apps','app_categories'],
        'put_apps' : ['register_app'],
        'post_app' : ['install_app','uninstall_app','launch_app','stop_app']
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

    elif args.option in targets['get_mlts']:

        multisigget(api, args)

    elif args.option in targets['put_mlts']:

        multisigput(api, args, secret, secret2)

    elif args.option in targets['post_mlts']:

        multisigpost(api, args, secret, secret2)

    elif args.option in targets['get_apps']:

        appget(api, args)

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

    elif args.option in targets['get_delc']:

        forge_check(api, args)

    elif args.option == 'autoname':

        autoname(api, args)

    else:

        print "Option {} Not found".format(args.option)
        parser.print_help()



if __name__ in '__main__':

    main()
