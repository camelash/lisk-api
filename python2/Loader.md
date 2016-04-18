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

