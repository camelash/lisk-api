## Loader

Return the status of the local host

`python pylisk.py status --url http://localhost:7000`

```json
{
  "loaded": true,
  "blocksCount": 0,
  "success": true
}
```

Return the status of origin (login.lisk.io)

`python pylisk.py status --url https://login.lisk.io`

```json
{
  "loaded": true,
  "blocksCount": 0,
  "success": true
}
```

Return the status of the host if https is setup

`python pylisk.py status --url https://localhost:443`
```json
{
  "loaded": true,
  "blocksCount": 0,
  "success": true
}
```

Return the sync status of login.lisk.io

`python pylisk.py sync --url https://login.lisk.io`
```json
{
  "blocks": 0,
  "sync": false,
  "success": true,
  "height": 520790
}
```

Return the sync status of localhost

`python pylisk.py sync --url http://localhost:7000`
```json
{
  "blocks": 0,
  "sync": false,
  "success": true,
  "height": 520790
}
```

Return the sync status of localhost https if setup

`python pylisk.py sync --url https://localhost:443`
```json
{
  "blocks": 0,
  "sync": false,
  "success": true,
  "height": 520790
}
```

