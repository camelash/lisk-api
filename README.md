## How to acquire and use:


```
git clone https://github.com/slasheks/lisk-api.git

cd lisk-api/python2/

python pylisk account --wallet 15797964559913448387L

```

## Disclaimer

```
Please be very careful with the options that require secret. There is no turning back. 
```

## General Options

When using a self-signed certificate just specify the certificate

```
python pylisk sync -u https://localhost:443 --certificate ".ssl/lisk.crt" 

```

When running the code in testnet use the --testnet or -t option

```
python pylisk app_categories --testnet
```

## [Account](examples/Account.md)

Show information of an account based on entering your secret (Requires Secret)

```
python pylisk open_account
```

Get the balance of an account by wallet address

```
python pylisk balance --wallet 15797964559913448387L 
````

Get the publicKey of an account by wallet address

```
python pylisk pubkey --wallet 15797964559913448387L
```

Generate an account based on a secret phrase (Requires Secret)

```
python pylisk genpub
```

Get all the account information based on wallet address

```
python pylisk account --wallet 15797964559913448387L 
```

Get the delegates of an account by address

```
python pylisk delegates_by_account --wallet 15797964559913448387L
```

Vote for accounts in a file. File must have public keys of desired voters (Requires secret)


```
python pylisk vote --vote-file 33.txt --vote-yes
```

```
python pylisk vote --vote-file 33.txt --vote-no
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
python pylisk status --url http://localhost:7000
```

```
python pylisk status --url https://login.lisk.io
```

```
python pylisk status --url https://localhost:443
```

Get the sync status of a host based on url

```
python pylisk sync --url https://login.lisk.io
```

```
python pylisk sync --url http://localhost:7000
```

```
python pylisk sync --url https://localhost:443
```

## [Peers](examples/Peers.md)

Get full peer list

```
python pylisk peer_list
```

Get peers filtered

```
python pylisk peer_list -p "?version=0.2.0"
```

Get the version of a peer (can be used with the --url flag)

```
python pylisk peer_version
```

Get peer information by IP (Not working)

```
python pylisk peer_ip
```

## [Blocks](examples/Blocks.md)

Get block by id

```
python pylisk blockid -p 9356270975884285392
```

Get all blocks

```
python pylisk all_blocks
```

Get blocks filtered (all options apply)

```
python pylisk all_blocks --parameter "?offset=0&limit=2"

```

Get fee details
```
python pylisk fee
```

Get block height

```
python pylisk height
```

My Forged Blocks (custom search)

```
python pylisk my_blocks --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

## [Signatures](examples/Signatures.md)

Get second signature of account

```

```

## [Transactions](examples/Transactions.md)

Get information of a block by block ID (supports full sorting options with the --parameters flag)

```
python pylisk blocktx --parameters ?blockId=9356270975884285392
````

Send a transaction with 1 Lisk to the user specified (Requires secret)

```
python pylisk send --destination-id slasheks_i --amount 1
````

Get information on a transaction ID

```
python pylisk get_tx --id 5454912568800551930
```

Get information on an unconfirmed transaction by ID

```
python pylisk unconfirmed --id 11723095834372015459
```

Get all unconfirmed transactions

```
python pylisk unconfirmed_all
````

## [Delegates](examples/Delegates.md)

Disable forging on the localhost (can be used with the --url flag, Requires secret)

```
python pylisk disable_forging
```

Delegate list all

```
python pylisk delegate_list
```

Delegate list filtered (order by rank only display 2)

```
python pylisk delegate_list -p "?orderBy=rate&limit=2"
```

Enable forging on the localhost (can be used with the --url flag, Requires secret)

```
python pylisk enable_forging
```

Get the delegate votes based on public key of an account

```
python pylisk delegate_voters --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get forged information on an account based on public key

```
python pylisk forged --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Register a delegate name (requires secret)

```
python pylisk register_delegate --username slasheks_api
```

## [Contacts](examples/Contacts.md)

Get the contacts of an account by publiKey

```
python pylisk contacts --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get unconfirmed contacts based on publicKey

```
python pylisk unconfirmed_contacts --key 00520a82e7e37b882eddcce40<snip>4f874c5cfcbc1f6c65a
```

Contact request (requires secret)

```
python pylisk add_contact --username slasheks2
```

## [Multisignatures](examples/Multisignatures.md)

Get information on a multisignature account

```
python pylisk my_multisig --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd
```

Create a multisignature account

```
python pylisk create_multisig --lifetime 1 --minimum 2 --keysgroup slasheks tharude
```

Sign a multisignature transaction

```
python pylisk sign_tx --id 8118789159994910817 
```
