## Transactions

Return transactions per block ID (supports full sorting options)

`python pylisk blocktx --parameters ?blockId=3978197175682889993`

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

`python pylisk send --destination-id slasheks_i --amount 1`

Password: /type passphrase here/

Password: /type passphrase here/

```json
{
  "transactionId": "6881517628096465739",
  "success": true
}
```

Get transaction information by transaction ID

`python pylisk get_tx --id 1242621300313617250`

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

`python pylisk unconfirmed --id 1792913617361330271`

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

`python pylisk unconfirmed_all`

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

