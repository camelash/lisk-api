## How to acquire and use:


```
git clone https://github.com/slasheks/lisk-api.git

cd lisk-api/python2/

python helper.py --option account --wallet 15797964559913448387L

```

## Disclaimer

```
Please be very careful with the options that require secret. There is no turning back. 
```

## [Account](Account.md)

Show information of an account based on entering your secret (Requires Secret)

```
python helper.py --option open_account
```

Get the balance of an account by wallet address

```
python helper.py --option balance --wallet 15797964559913448387L 
````

Get the publicKey of an account by wallet address

```
python helper.py --option pubkey --wallet 15797964559913448387L
```

Generate an account based on a secret phrase (Requires Secret)

```
python helper.py --option genpub
```

Get all the account information based on wallet address

```
python helper.py --option account --wallet 15797964559913448387L 
```

Get the delegates of an account by address

```
python helper.py --option delegates_by_account --wallet 15797964559913448387L
```

Vote for accounts in a file. File must have public keys of desired voters (Requires secret)


```
python helper.py --option vote --vote-file 33.txt --vote-yes
```

```
python helper.py --option vote --vote-file 33.txt --vote-no
```

Using --vote-yes will vote for these delegates

Using --vote-no will take away the votes

Example File Layout:

```
3076e3c07b27833398fe7b92df2db45b975011335cddd32009940ee3effc8e4d
475f2db1fbf22c35caecbee42a38e7b29063b644063514bd3bbaf31f2f9d8115
34ba95be5a20d5407865d7c790a94730c0f138e18e608b74d12c9a7ffd903a34
3076e3c07b27833398fe7b92df2db45b975011335cddd32009940ee3effc8e4d
475f2db1fbf22c35caecbee42a38e7b29063b644063514bd3bbaf31f2f9d8115
34ba95be5a20d5407865d7c790a94730c0f138e18e608b74d12c9a7ffd903a34
3a5e89551d42715772b83baf758bb67b1001234486947786b93cbaf9695ba3b6
2e6b568a370a4f107e4a5124ab680f6bc97bd1634c3a4d83bcfaf49830f24b6a
4fbda6b316fa930c3a93cd5b1d82d5fd107d11d95a238c64af472bb8269778b2
```

## [Loader](Loader.md)

Get the status of a node by url

```
python helper.py --option status --url http://localhost:7000
```

```
python helper.py --option status --url https://login.lisk.io
```

```
python helper.py --option status --url https://localhost:443
```

Get the sync status of a host based on url

```
python helper.py --option sync --url https://login.lisk.io
```

```
python helper.py --option sync --url http://localhost:7000
```

```
python helper.py --option sync --url https://localhost:443
```

## [Peers](Peers.md)

Get full peer list

```
python helper.py -o peer_list
```

Get peers filtered

```
python helper.py -o peer_list -p "?version=0.2.0"
```

Get the version of a peer (can be used with the --url flag)

```
python helper.py -o peer_version
```

Get peer information by IP (Not working)

```
python helper.py -o peer_ip
```

## [Blocks](Blocks.md)

Get block by id

```
python helper.py --option blockid -p 9356270975884285392
```

Get all blocks

```
python helper.py --option all_blocks
```

Get blocks filtered (all options apply)

```
python helper.py --option all_blocks --parameter "?offset=0&limit=2"

```

Get fee details
```
python helper.py --option fee
```

Get block height

```
python helper.py --option height
```

My Forged Blocks (custom search)

```
python helper.py --option my_blocks --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

## [Signatures](Signatures.md)

Get second signature of account

```

```

## [Transactions](Transactions.md)

Get information of a block by block ID (supports full sorting options with the --parameters flag)

```
python helper.py --option blocktx --parameters ?blockId=9356270975884285392
````

Send a transaction with 1 Lisk to the user specified (Requires secret)

```
python helper.py --option send --destination-id slasheks_i --amount 1
````

Get information on a transaction ID

```
python helper.py --option get_tx --id 5454912568800551930
```

Get information on an unconfirmed transaction by ID

```
python helper.py --option unconfirmed --id 11723095834372015459
```

Get all unconfirmed transactions

```
python helper.py -o unconfirmed_all
````

## [Delegates](Delegates.md)

Disable forging on the localhost (can be used with the --url flag, Requires secret)

```
python helper.py -o disable_forging
```

Delegate list all

```
python helper.py -o delegate_list
```

Delegate list filtered (order by rank only display 2)

```
python helper.py -o delegate_list -p "?orderBy=rate&limit=2"
```

Enable forging on the localhost (can be used with the --url flag, Requires secret)

```
python helper.py -o enable_forging
```

Get the delegate votes based on public key of an account

```
python helper.py --option delegate_voters --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get forged information on an account based on public key

```
python helper.py --option forged --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Register a delegate name (requires secret)

```
python helper.py --option register_delegate --username slasheks_api
```

## [Contacts](Contacts.md)

Get the contacts of an account by publiKey

```
python helper.py --option contacts --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Get unconfirmed contacts based on publicKey

```
python helper.py --option unconfirmed_contacts --key 00520a82e7e37b882eddcce4055f04f874c5cfcbcf1b306a63d7552dd1f6c65a
```

Contact request (requires secret)

```
python helper.py -o add_contact --username slasheks2
```
