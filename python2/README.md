## Account 

(URL default is http://localhost:7000) when not specified

Return account information given a wallet address

`python helper.py --option account --wallet 12890373581776525214L`

```json
{
  "account": {
    "username": "slasheks_pi", 
    "multisignatures": [], 
    "unconfirmedBalance": 59540000000, 
    "secondPublicKey": "", 
    "unconfirmedSignature": false, 
    "publicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
    "address": "12890373581776525214L", 
    "balance": 59540000000, 
    "secondSignature": false, 
    "u_multisignatures": []
  }, 
  "success": true
}
```

Return the balance of a given address

`python helper.py --option balance --wallet 12890373581776525214L`      
```json
{
  "unconfirmedBalance": 59540000000, 
  "balance": 59540000000, 
  "success": true
}
```

Return publicKey of a given address

`python helper.py --option pubkey --wallet 12890373581776525214L`     
```json
{
  "publicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
  "success": true
}
```

Return public key generated given a secret

`python helper.py --option genpub`

Password: /type pass here/

Password: /type pass here/
```json
{
  "publicKey": "xxxxxpubkeyxxxxxx", 
  "success": true
}
```

Return account information by opening

`python helper.py --option open_account`

Password: /type pass here/

Password: /type pass here/
```json
{
  "account": {
    "multisignatures": [], 
    "unconfirmedBalance": 0, 
    "secondPublicKey": "", 
    "unconfirmedSignature": false, 
    "publicKey": "de352b0df39042e201d31564049023af58a106c6d904b74a68aa65012852997f", 
    "address": "7465198732553521929L", 
    "balance": 0, 
    "secondSignature": false, 
    "u_multisignatures": []
  }, 
  "success": true
}
```

Will return account's delegates by address.

`python helper.py --option delegates_by_account --wallet 12475940823804898745L`
```json
{
  "delegates": [
    {
      "username": "genesisDelegate53", 
      "producedblocks": 4519, 
      "missedblocks": 97, 
      "publicKey": "07868b5b97233eb5ce301edfd16601e1ecf2661481b39a0bdea59391104dc42c", 
      "rate": 131, 
      "address": "12138388235771861080L", 
      "vote": 22815624351740, 
      "productivity": "97.89", 
      "virgin": false
    }, 
    {
      "username": "genesisDelegate98", 
      "producedblocks": 4538, 
      "missedblocks": 82, 
      "publicKey": "14566e853bf1d3c597078383156f880d28d0260e4f32fc96cfcb8e4c8811abe1", 
      "rate": 142, 
      "address": "2994830225868734490L", 
      "vote": 19999677780175, 
      "productivity": "98.22", 
      "virgin": false
    }
    ]
}
```
Vote for accounts, API supports vote as list from pubkey file. 

`python helper.py --option vote --key`

Password: /type pass here/

Password: /type pass here/
```json
{
  "transaction": {
    "recipientUsername": "slasheks_pi", 
    "fee": 100000000, 
    "senderId": "12890373581776525214L", 
    "timestamp": 32230261, 
    "requesterPublicKey": null, 
    "recipientId": "12890373581776525214L", 
    "senderPublicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
    "amount": 0, 
    "asset": {
      "votes": [
        "+4546776eef10327a5f5c0e7ec6d1d57e47c8b55887a753f98194668f1a3d8525"
      ]
    }, 
    "signature": "b553aacfd5ad5728cb16dc5d9afff5c55d20b8c60076350ce311491f9d3514bc44e3b7266e585b477dee787f72ddfb87f1d506a2d34263dc1c6851c613fe1603", 
    "type": 3, 
    "id": "16948475056663240797"
  }, 
  "success": true
}
```

## Loader

Return the status of the local host

`python helper.py --option status --url http://localhost:7000`

```json
{
  "loaded": true, 
  "blocksCount": 0, 
  "success": true
}
```

Return the status of origin (login.lisk.io)

`python helper.py --option status --url https://login.lisk.io`

```json
{
  "loaded": true, 
  "blocksCount": 0, 
  "success": true
}
```

Return the status of the host if https is setup

`python helper.py --option status --url https://localhost:443`
```json
{
  "loaded": true, 
  "blocksCount": 0, 
  "success": true
}
```

Return the sync status of login.lisk.io

`python helper.py --option sync --url https://login.lisk.io`            
```json
{
  "blocks": 0, 
  "sync": false, 
  "success": true, 
  "height": 520790
}
```

Return the sync status of localhost

`python helper.py --option sync --url http://localhost:7000`
```json
{
  "blocks": 0, 
  "sync": false, 
  "success": true, 
  "height": 520790
}
```

Return the sync status of localhost https if setup

`python helper.py --option sync --url https://localhost:443`
```json
{
  "blocks": 0, 
  "sync": false, 
  "success": true, 
  "height": 520790
}
```

## Transactions

Return transactions per block ID

`python helper.py --option blocktx --id 3978197175682889993`
```json
{
  "count": 2, 
  "success": true, 
  "transactions": [
    {
      "signSignature": "", 
      "fee": 10000000, 
      "timestamp": 32240352, 
      "blockId": "3978197175682889993", 
      "senderId": "12890373581776525214L", 
      "recipientId": "9315820719019880567L", 
      "senderPublicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
      "height": "522109", 
      "amount": 10000, 
      "signatures": null, 
      "recipientUsername": "", 
      "confirmations": "49", 
      "signature": "4c6132f00e28af989d439fe2133dd45391ef63acb4e428a1bffc13c39f328bd2f05a0bebdcd42bcc8354f28f9fbd632b9a2a06b98ea0c3b8efe90535ff3d2b07", 
      "senderUsername": "", 
      "type": 0, 
      "id": "11264692208725315602", 
      "asset": {}
    }, 
    {
      "signSignature": "", 
      "fee": 10000000, 
      "timestamp": 32240815, 
      "blockId": "3978197175682889993", 
      "senderId": "12890373581776525214L", 
      "recipientId": "11827477847453495423L", 
      "senderPublicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
      "height": "522109", 
      "amount": 10000, 
      "signatures": null, 
      "recipientUsername": "Tharude_US_DDoS", 
      "confirmations": "49", 
      "signature": "b797cec7400032c2c92c34c5174575bc9d8d8cb0f490edacdeb8e91148cace4ac503744133876a8030904785a43562b2443c838fdd8b4a40e251b99d1c1ab00d", 
      "senderUsername": "", 
      "type": 0, 
      "id": "3442323236802374321", 
      "asset": {}
    }
  ]
}
```
Return confirmation of send transaction

`python helper.py --option send --destination-id slasheks_i --amount 1`

Password: /type passphrase here/

Password: /type passphrase here/

```json
{
  "transactionId": "6881517628096465739", 
  "success": true
}
```

Get transaction information by transaction ID

`python helper.py --option get_tx --id 1242621300313617250`

```json
{
  "transaction": {
    "signSignature": "", 
    "fee": 10000000, 
    "timestamp": 32238819, 
    "blockId": "8519725616070594374", 
    "senderId": "12890373581776525214L", 
    "recipientId": "12890373581776525214L", 
    "senderPublicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
    "height": "521924", 
    "amount": 10000, 
    "signatures": null, 
    "recipientUsername": "slasheks_pi", 
    "confirmations": "3197", 
    "signature": "6ec49c3678667691fb8f20ef69f9938b8260d266d1c684c57769ec58b925c70b1a4f9e0c6f93a097e915c2294fd25336b1adf4b26f6cfeb79d5099dbb8db1808", 
    "senderUsername": "", 
    "type": 0, 
    "id": "1242621300313617250", 
    "asset": {}
  }, 
  "success": true
}
```

Get unconfirmed transaction by ID

`python helper.py --option unconfirmed --id 1792913617361330271`

```json
{
  "transaction": {
    "fee": 1000000000, 
    "timestamp": 31941578, 
    "senderId": "11152787807674929625L", 
    "senderPublicKey": "c7af3423700526b7d09e91e0675c50d8e726abe5d91c5aa56fb967ec7d4edd4f", 
    "amount": 0, 
    "asset": {
      "multisignature": {
        "lifetime": 24, 
        "keysgroup": [
          "+39039034afe044ddc87ff83bd7a64f64ddf966fe3bafd8571dc2a29d0c15c320"
        ], 
        "min": 2
      }
    }, 
    "signature": "62da329d08e089855ebcf68011c29a2580652018ab683995304467ca8ae0c654f5619f925f2812bd11719fa10364d4bab265df8e048e595a5985821186957a03", 
    "type": 8, 
    "id": "1792913617361330271"
  }, 
  "success": true
}
```

Return all unconfirmed transactions

`python helper.py -o unconfirmed_all`

```json
{
  "success": true, 
  "transactions": [
    {
      "fee": 1000000000, 
      "timestamp": 31941578, 
      "senderId": "11152787807674929625L", 
      "senderPublicKey": "c7af3423700526b7d09e91e0675c50d8e726abe5d91c5aa56fb967ec7d4edd4f", 
      "amount": 0, 
      "asset": {
        "multisignature": {
          "lifetime": 24, 
          "keysgroup": [
            "+39039034afe044ddc87ff83bd7a64f64ddf966fe3bafd8571dc2a29d0c15c320"
          ], 
          "min": 2
        }
      }, 
      "signature": "62da329d08e089855ebcf68011c29a2580652018ab683995304467ca8ae0c654f5619f925f2812bd11719fa10364d4bab265df8e048e595a5985821186957a03", 
      "type": 8, 
      "id": "1792913617361330271"
    }, 
    {
      "signSignature": "1e6530d48c8e13b6c60b25cd38186c18b7482d5a02026e4c871cbbf37e716b731d8b986247d2c4736c4bd4622ed88dab0962e84c7c99f4a4c336cf3025a44604", 
      "fee": 1000000000, 
      "timestamp": 31966929, 
      "senderId": "17868584131599322862L", 
      "senderPublicKey": "050d622b094f9fd32017bdff517135cb30d643e63e30f7564254ef814c63c0eb", 
      "amount": 0, 
      "asset": {
        "multisignature": {
          "lifetime": 24, 
          "keysgroup": [
            "+b854553437c6e92f35a33779d27c6edb6da208d1ff603a35a021fd63229a0af6"
          ], 
          "min": 2
        }
      }, 
      "signature": "4113bf020ec34af313e13f36939a9302bc1f069f8b9c1fda4174690e4c1ceaeb62ea2915587b581a1ff0ea0cd10885008c80beb98704aed04c8f31ed23c92f0b", 
      "type": 8, 
      "id": "11902071062126798855"
    }, 
    {
      "signSignature": "2d4b3fa794028ad72da93948636a025a6c8423fd3893fea80ba34121f006eaca734c71836929afbde6e228edd285d24d11c5db1aee8f76b78765292b99fd3d09", 
      "fee": 10000000, 
      "senderId": "13728860908239205171L", 
      "timestamp": 32026635, 
      "recipientUsername": "irty", 
      "recipientId": "165482363070033519L", 
      "senderPublicKey": "a3f633e6a07e3c9ba7aadb97b953b8ec5de436ba700de337a7c91bbd50507fc1", 
      "amount": 1000000000, 
      "asset": {}, 
      "signature": "42ae56f9b30398e64781ef1a8792a776d853a87f379941ab9aa31d158900b20a5cb91363d717ff0e08297b752ada76e47c67a793fbae00c392df76e9b991990e", 
      "type": 0, 
      "id": "11784021429142792183"
    }
  ]
}
```

## Peers

Return peerlist no options (cut for brevity)

`python helper.py -o peer_list`

```
{
  "peers": [
    {
      "ip": "1.2.3.4", 
      "state": 1, 
      "version": "0.1.1", 
      "sharePort": 0, 
      "os": "linux3.2.0-4-amd64", 
      "port": 1
    }, 
    {
      "ip": "1.1.1.1", 
      "state": 1, 
      "version": "0.1.1", 
      "sharePort": 0, 
      "os": "linux3.2.0-4-amd64", 
      "port": 1
    }

    ---snip---

    ]
} 
``` 

Return version running on target

`python helper.py -o peer_version`

```json
{
  "version": "0.1.4", 
  "build": "v06:13:55 12/04/2016\n", 
  "success": true
}
```

Return peer information (not working)

`python helper.py -o peer_ip`

```json
{
  "success": false, 
  "error": "Missing required property: ip_str"
}
```

## Delegates

`python helper.py -o disable_forging`

Password: 

Password: 

```json
{
  "success": true, 
  "address": "5510723892457331004L"
}
```

`python helper.py -o enable_forging`

Password: 

Password: 

```json
{
  "success": true, 
  "address": "5510723892457331004L"
}
```

Return voter addresses 

`python helper.py --option delegate_voters --key b2961fd27ba57cc50540d043635f80666e11f143d8fa0fb666fe5cd9495230e9`

```json
{
  "accounts": [
    {
      "balance": 50000, 
      "address": "7354580958703219990L"
    }, 
    {
      "balance": 29207874, 
      "address": "12701582741679139012L"
    }, 
    {
      "balance": 90000000, 
      "address": "4683502206571402547L"
    } 
    ]
}
```

Return forged amount and rewards

`python helper.py --option forged --key b57878a79acb36be31171749ec361d16cc0c4a27d2d42f62d6cb0a5405223c69`

```json
{
  "rewards": 617500000000, 
  "forged": 751631682963, 
  "success": true, 
  "fees": 134131682963
}
```
