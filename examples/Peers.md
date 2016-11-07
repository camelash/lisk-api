## Peers

Return peerlist no options (supports sorting options | cut for brevity)

`python pylisk peer_list`

```json
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

`python pylisk peer_version`

```json
{
  "version": "0.1.4",
  "build": "v06:13:55 12/04/2016\n",
  "success": true
}
```

Return peer information (not working)

`python pylisk peer_ip`

```json
{
  "success": false,
  "error": "Missing required property: ip_str"
}
```

