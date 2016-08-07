## How to acquire and use:


```
git clone https://github.com/slasheks/lisk-api.git

cd lisk-api/python2/

python pylisk.py account --wallet 15797964559913448387L

```

## Disclaimer

```
Please be very careful with the options that require secret. There is no turning back. 
```

## General Options

When using a self-signed certificate just specify the certificate

```
python pylisk.py sync -u https://localhost:443 --certificate ".ssl/lisk.crt" 

```

When running the code in testnet use the --testnet or -t option

```
python pylisk.py app_categories --testnet
```

## [Account](examples/Account.md)

Show information of an account based on entering your secret (Requires Secret)

```
python pylisk.py open_account
```

Get the balance of an account by wallet address

```
python pylisk.py balance --wallet 15797964559913448387L 
````

Get the publicKey of an account by wallet address

```
python pylisk.py pubkey --wallet 15797964559913448387L
```

Generate an account based on a secret phrase (Requires Secret)

```
python pylisk.py genpub
```

Get all the account information based on wallet address

```
python pylisk.py account --wallet 15797964559913448387L 
```

Get the delegates of an account by address

```
python pylisk.py delegates_by_account --wallet 15797964559913448387L
```

Vote for accounts in a file. File must have public keys of desired voters (Requires secret)


```
python pylisk.py vote --vote-file 33.txt --vote-yes
```

```
python pylisk.py vote --vote-file 33.txt --vote-no
```

Using --vote-yes will vote for these delegates

Using --vote-no will take away the votes

Example File Layout:

```
15797964559913448387L
14200733803191436160L
14983679022430120939L
genesisDelegate12
genesisDelegate69
genesisDelegate35
12c80468dd0f8ad91277e1c9fc17038951eda05bb27b3415ea9cc433fe44168a
16360b97caa1e3a2ec5eb0fe8c228606da460bde57ae94db9f13514ec595f012
3a0978135245858f00bdea1273c4d7cc8e83f996e4c6ccf315e65eef8bf404cf
```

## [Loader](examples/Loader.md)

Get the status of a node by url

```
python pylisk.py status --url http://localhost:7000
```

```
python pylisk.py status --url https://login.lisk.io
```

```
python pylisk.py status --url https://localhost:443
```

Get the sync status of a host based on url

```
python pylisk.py sync --url https://login.lisk.io
```

```
python pylisk.py sync --url http://localhost:7000
```

```
python pylisk.py sync --url https://localhost:443
```

## [Peers](examples/Peers.md)

Get full peer list

```
python pylisk.py peer_list
```

Get peers filtered

```
python pylisk.py peer_list -p "?version=0.2.0"
```

Get the version of a peer (can be used with the --url flag)

```
python pylisk.py peer_version
```

Get peer information by IP (Not working)

```
python pylisk.py peer_ip
```

## [Blocks](examples/Blocks.md)

Get block by id

```
python pylisk.py blockid -p 9356270975884285392
```

Get all blocks

```
python pylisk.py all_blocks
```

Get blocks filtered (all options apply)

```
python pylisk.py all_blocks --parameter "?offset=0&limit=2"

```

Get fee details
```
python pylisk.py fee
```

Get block height

```
python pylisk.py height
```

My Forged Blocks (custom search)

```
python pylisk.py my_blocks --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

## [Signatures](examples/Signatures.md)

Get second signature of account

```

```

## [Transactions](examples/Transactions.md)

Get information of a block by block ID (supports full sorting options with the --parameters flag)

```
python pylisk.py blocktx --parameters ?blockId=9356270975884285392
````

Send a transaction with 1 Lisk to the user specified (Requires secret)

```
python pylisk.py send --destination-id slasheks_i --amount 1
````

Get information on a transaction ID

```
python pylisk.py get_tx --id 5454912568800551930
```

Get information on an unconfirmed transaction by ID

```
python pylisk.py unconfirmed --id 11723095834372015459
```

Get all unconfirmed transactions

```
python pylisk.py unconfirmed_all
````

## [Delegates](examples/Delegates.md)

Disable forging on the localhost (can be used with the --url flag, Requires secret)

```
python pylisk.py disable_forging
```

Delegate list all

```
python pylisk.py delegate_list
```

Delegate list filtered (order by rank only display 2)

```
python pylisk.py delegate_list -p "?orderBy=rate&limit=2"
```

Enable forging on the localhost (can be used with the --url flag, Requires secret)

```
python pylisk.py enable_forging
```

Get the delegate votes based on public key of an account

```
python pylisk.py delegate_voters --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get forged information on an account based on public key

```
python pylisk.py forged --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Register a delegate name (requires secret)

```
python pylisk.py register_delegate --username slasheks_api
```

## [Contacts](examples/Contacts.md)

Get the contacts of an account by publiKey

```
python pylisk.py contacts --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get unconfirmed contacts based on publicKey

```
python pylisk.py unconfirmed_contacts --key 00520a82e7e37b882eddcce40<snip>4f874c5cfcbc1f6c65a
```

Contact request (requires secret)

```
python pylisk.py add_contact --username slasheks2
```

## [Multisignatures](examples/Multisignatures.md)

Get information on a multisignature account

```
python pylisk.py my_multisig --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd
```

Create a multisignature account

```
python pylisk.py create_multisig --lifetime 1 --minimum 2 --keysgroup slasheks tharude
```

Sign a multisignature transaction

```
python pylisk.py sign_tx --id 8118789159994910817 
```
