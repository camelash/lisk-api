#!/usr/bin/env python

import json
import requests
import logging

class liskAPI(object):

    def __init__(self,rturl=''):

        self.headers = {'content-type': 'application/json'}
        self.target_url = rturl

        try:

            r = requests.get("{}/api/loader/status".format(self.target_url))

        except requests.exceptions.ConnectionError as e:

            print "Connection error. {}".format(e.message)
            exit(1)


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
