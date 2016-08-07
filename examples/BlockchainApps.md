Get the application list of localhost

```
python pylisk.py app_list 
```
```json
{
  "dapps": [
    {
      "category": 8, 
      "name": "mschmoock/sdk", 
      "tags": "test", 
      "link": "https://github.com/m-schmoock/lisk-dapps-sdk/archive/development.zip", 
      "transactionId": "366869793417060333", 
      "icon": null, 
      "type": 0, 
      "description": "Test forked SDK example"
    }, 
    {
      "category": 0, 
      "name": "bitbooks", 
      "tags": "bitbooks", 
      "link": "https://github.com/VivekAusekar/liskApp/archive/stage.zip", 
      "transactionId": "14602496231523117483", 
      "icon": "https://iconverticons.com/img/logo.png", 
      "type": 0, 
      "description": "bitbooks"
    }, 
    {
      "category": 4, 
      "name": "d3", 
      "tags": null, 
      "link": "https://github.com/d3/d3/releases/download/v4.2.1/d3.zip", 
      "transactionId": "17251328029729996639", 
      "icon": "http://www.webopixel.net/blog/wp-content/uploads/2014/04/d3-icon.png", 
      "type": 0, 
      "description": "test"
    }, 
    {
      "category": 4, 
      "name": "tota11y", 
      "tags": null, 
      "link": "https://github.com/Khan/tota11y/archive/master.zip", 
      "transactionId": "4212567360883087316", 
      "icon": "http://wwwhere.io/img/thumbs/tota11y.jpg", 
      "type": 0, 
      "description": "test"
    }
  ], 
  "success": true
}
```
Get Blockchain App by Transaction ID
```
python pylisk.py get_app --id 17251328029729996639 
```
```json
{
  "dapp": {
    "category": 4, 
    "name": "d3", 
    "tags": null, 
    "link": "https://github.com/d3/d3/releases/download/v4.2.1/d3.zip", 
    "transactionId": "17251328029729996639", 
    "icon": "http://www.webopixel.net/blog/wp-content/uploads/2014/04/d3-icon.png", 
    "type": 0, 
    "description": "test"
  }, 
  "success": true
}
```

Search for apps (Variable parameter option)

```
python pylisk.py app_search --parameter "?q=installed=1" 

```
```json
{
  "dapps": [], 
  "success": true
}
```

Get installed blockchain applications

```
python pylisk.py installed_apps 

```

```json
{
  "dapps": [], 
  "success": true
}
```

Get the IDs of installed blockchain applications
```
python pylisk.py installed_appsid 
```
```json
{
  "ids": [], 
  "success": true
}
```

```
python pylisk.py installing_apps  
```
```json
{
  "installing": [], 
  "success": true
}
```

Get bblockchain applications that are uninstalling
```
python pylisk.py uninstalling_apps 
```
```json
{
  "uninstalling": [], 
  "success": true
}
```

Get all the launched apps
```
python pylisk.py launched_apps     
```
```json
{
  "launched": [], 
  "success": true
}
```

Get the blockchain application categories

```
python pylisk.py app_categories 
```
```json
{
  "categories": {
    "Networking": 5, 
    "Finance": 2, 
    "Entertainment": 1, 
    "Science": 6, 
    "Miscellaneous": 4, 
    "Utilities": 8, 
    "Games": 3, 
    "Social": 7, 
    "Education": 0
  }, 
  "success": true
}
```

