Get the contacts of an account by publiKey

```
python pylisk.py contacts --key a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901
```

```json
{
  "following": [], 
  "followers": [
    {
      "username": "slasheks_delegate", 
      "address": "14815679130724076642L"
    }
  ], 
  "success": true
}
```

Get unconfirmed contacts based on publicKey

```
python pylisk.py unconfirmed_contacts --key a6ed31b0dce156779b77f8e1c723af0ce04dbb74520979b76866da56ede4462f
```

```json
{
  "success": true, 
  "contacts": [
    {
      "fee": 100000000, 
      "senderId": "5510723892457331004L", 
      "timestamp": 32968283, 
      "requesterPublicKey": null, 
      "recipientId": null, 
      "senderPublicKey": "a6ed31b0dce156779b77f8e1c723af0ce04dbb74520979b76866da56ede4462f", 
      "amount": 0, 
      "asset": {
        "contact": {
          "address": "+12890373581776525214L"
        }
      }, 
      "signature": "b9d47702e61b1000fb53d5263de5eaebc736bb481cd0ad525e9542f950383e5fa3817a45829809f2f0c3ccefd2ec8dd47852a95e52dafc6a3190cd958138620e", 
      "type": 5, 
      "id": "12143395574924480545"
    }
  ]
}
```

Contact request (requires secret)

```
python pylisk.py add_contact --username slasheks_api
Password: 
Confirming the password. Please type it again.
Password: 
```

```json
{
  "transaction": {
    "fee": 100000000, 
    "senderId": "12890373581776525214L", 
    "timestamp": 32971717, 
    "requesterPublicKey": null, 
    "recipientId": null, 
    "senderPublicKey": "a69ed828f28695a03558d5c29f96081d20d1ecc0e046e8622793ab2662629901", 
    "amount": 0, 
    "asset": {
      "contact": {
        "address": "+6135290894472857248L"
      }
    }, 
    "signature": "92f8bfdc49aa275167630ceffad6d5edfd7c122c3f17057190321ff9b86438c397c59c792359ec264aa6b1b9d77f2af5337015aa32d67b36a718b6517e6f410f", 
    "type": 5, 
    "id": "9570751988579397710"
  }, 
  "success": true
}
```
