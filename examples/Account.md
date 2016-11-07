(URL default is http://localhost:7000) when not specified


## Account

Return account information given a wallet address

`python pylisk account --wallet 12890373581776525214L`

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

`python pylisk balance --wallet 12890373581776525214L`
```json
{
  "unconfirmedBalance": 59540000000,
  "balance": 59540000000,
  "success": true
}
```

Return publicKey of a given address

`python pylisk pubkey --wallet 12890373581776525214L`
```json
{
  "publicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901",
  "success": true
}
```

Return public key generated given a secret

`python pylisk genpub`

Password: /type pass here/

Password: /type pass here/
```json
{
  "publicKey": "xxxxxpubkeyxxxxxx",
  "success": true
}
```

Return account information by opening

`python pylisk open_account`

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

`python pylisk delegates_by_account --wallet 12475940823804898745L`
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

`python pylisk vote --key`

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

