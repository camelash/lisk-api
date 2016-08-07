## Delegates

`python pylisk.py disable_forging`

Password:

Password:

```json
{
  "success": true,
  "address": "5510723892457331004L"
}
```

`python pylisk.py enable_forging`

Password:

Password:

```json
{
  "success": true,
  "address": "5510723892457331004L"
}
```

Return voter addresses

`python pylisk.py delegate_voters --key b2961fd27ba57cc50540d043635f80666e11f143d8fa0fb666fe5cd9495230e9`

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

`python pylisk.py forged --key b57878a79acb36be31171749ec361d16cc0c4a27d2d42f62d6cb0a5405223c69`

```json
{
  "rewards": 617500000000,
  "forged": 751631682963,
  "success": true,
  "fees": 134131682963
}
```

Register delegate name and return confimation

python pylisk.py register_delegate -p slasheks_api

Password:

Password:

```json
{
  "transaction": {
    "fee": 10000000000,
    "senderId": "6135290894472857248L",
    "timestamp": 32455328,
    "requesterPublicKey": null,
    "recipientId": null,
    "senderPublicKey": "41990964448ce75db7400f26daaf2b50eca217ee5357630e8660b146568eb7e0",
    "amount": 0,
    "asset": {
      "delegate": {
        "username": "slasheks_api",
        "publicKey": "41990964448ce75db7400f26daaf2b50eca217ee5357630e8660b146568eb7e0"
      }
    },
    "signature": "3e4643f1aad15d03b2cb233d492cc52cb58e58438b3a078e7f83fd6fccc63cadd7f14d6e7f2bebea2707b172d59915f162098dbb88791112599ada24e1eab706",
    "type": 2,
    "id": "932773045691402128"
  },
  "success": true
}
```

python pylisk.py register_delegate --username slasheks_api

Password:

Password:

```json
{
  "success": false,
  "error": "Account already has a username"
}
```

