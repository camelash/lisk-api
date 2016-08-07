#!/bin/bash 

echo "python pylisk.py --option account --wallet 3129082046836520604L --testnet"
python pylisk.py --option account --wallet 3129082046836520604L --testnet
echo "python pylisk.py -o sync -u https://localhost:443 --certificate ".ssl/lisk.crt"  --testnet"
python pylisk.py -o sync -u https://localhost:443 --certificate ".ssl/lisk.crt"  --testnet
echo "python pylisk.py --option app_categories --testnet --testnet"
python pylisk.py --option app_categories --testnet --testnet
echo "python pylisk.py --option open_account --testnet"
python pylisk.py --option open_account --testnet
echo "python pylisk.py --option balance --wallet 3129082046836520604L  --testnet"
python pylisk.py --option balance --wallet 3129082046836520604L  --testnet
echo "python pylisk.py --option pubkey --wallet 3129082046836520604L --testnet"
python pylisk.py --option pubkey --wallet 3129082046836520604L --testnet
echo "python pylisk.py --option genpub --testnet"
python pylisk.py --option genpub --testnet
echo "python pylisk.py --option account --wallet 3129082046836520604L  --testnet"
python pylisk.py --option account --wallet 3129082046836520604L  --testnet
echo "python pylisk.py --option delegates_by_account --wallet 3129082046836520604L --testnet"
python pylisk.py --option delegates_by_account --wallet 3129082046836520604L --testnet
echo "python pylisk.py --option vote --vote-file 33.txt --vote-yes --testnet"
python pylisk.py --option vote --vote-file 33.txt --vote-yes --testnet
echo "python pylisk.py --option vote --vote-file 33.txt --vote-no --testnet"
python pylisk.py --option vote --vote-file 33.txt --vote-no --testnet
echo "python pylisk.py --option status --url http://localhost:7000 --testnet"
python pylisk.py --option status --url http://localhost:7000 --testnet
echo "python pylisk.py --option status --url https://login.lisk.io"
python pylisk.py --option status --url https://login.lisk.io 
echo "python pylisk.py --option status --url https://localhost:443 --testnet"
python pylisk.py --option status --url https://localhost:443 --testnet
echo "python pylisk.py --option sync --url https://login.lisk.io "
python pylisk.py --option sync --url https://login.lisk.io 
echo "python pylisk.py --option sync --url http://localhost:7000 --testnet"
python pylisk.py --option sync --url http://localhost:7000 --testnet
echo "python pylisk.py --option sync --url https://localhost:443 --testnet"
python pylisk.py --option sync --url https://localhost:443 --testnet
echo "python pylisk.py --option peer_list --testnet"
python pylisk.py --option peer_list --testnet
echo "python pylisk.py --option peer_list -p "?version=0.2.0" --testnet"
python pylisk.py --option peer_list -p "?version=0.2.0" --testnet
echo "python pylisk.py --option peer_version --testnet"
python pylisk.py --option peer_version --testnet
echo "python pylisk.py --option peer_ip --testnet"
python pylisk.py --option peer_ip --testnet
echo "python pylisk.py --option blockid -p 9356270975884285392 --testnet"
python pylisk.py --option blockid -p 9356270975884285392 --testnet
echo "python pylisk.py --option all_blocks --testnet"
python pylisk.py --option all_blocks --testnet
echo "python pylisk.py --option all_blocks --parameter "?offset=0&limit=2" --testnet"
python pylisk.py --option all_blocks --parameter "?offset=0&limit=2" --testnet
echo "python pylisk.py --option fee --testnet"
python pylisk.py --option fee --testnet
echo "python pylisk.py --option height --testnet"
python pylisk.py --option height --testnet
echo "python pylisk.py --option my_blocks --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option my_blocks --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option blocktx --parameters ?blockId=9356270975884285392 --testnet"
python pylisk.py --option blocktx --parameters ?blockId=9356270975884285392 --testnet
echo "python pylisk.py --option send --destination-id slasheks_i --amount 1 --testnet"
python pylisk.py --option send --destination-id slasheks_i --amount 1 --testnet
echo "python pylisk.py --option get_tx --id 5454912568800551930 --testnet"
python pylisk.py --option get_tx --id 5454912568800551930 --testnet
echo "python pylisk.py --option unconfirmed --id 11723095834372015459 --testnet"
python pylisk.py --option unconfirmed --id 11723095834372015459 --testnet
echo "python pylisk.py --option unconfirmed_all --testnet"
python pylisk.py --option unconfirmed_all --testnet
echo "python pylisk.py --option disable_forging --testnet"
python pylisk.py --option disable_forging --testnet
echo "python pylisk.py --option delegate_list --testnet"
python pylisk.py --option delegate_list --testnet
echo "python pylisk.py --option delegate_list -p "?orderBy=rate&limit=2" --testnet"
python pylisk.py --option delegate_list -p "?orderBy=rate&limit=2" --testnet
echo "python pylisk.py --option enable_forging --testnet"
python pylisk.py --option enable_forging --testnet
echo "python pylisk.py --option delegate_voters --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option delegate_voters --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option forged --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option forged --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option register_delegate --username slasheks_api --testnet"
python pylisk.py --option register_delegate --username slasheks_api --testnet
echo "python pylisk.py --option contacts --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option contacts --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option unconfirmed_contacts --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option unconfirmed_contacts --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option add_contact --username slasheks2 --testnet"
python pylisk.py --option add_contact --username slasheks2 --testnet
echo "python pylisk.py --option my_multisig --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet"
python pylisk.py --option my_multisig --key dc63877fbdfb538ff1d0ddecb979887f826998ab6907dca0a91e05c98d1602cd --testnet
echo "python pylisk.py --option create_multisig --lifetime 1 --minimum 2 --keysgroup slasheks tharude --testnet"
python pylisk.py --option create_multisig --lifetime 1 --minimum 2 --keysgroup slasheks tharude --testnet
echo "python pylisk.py --option sign_tx --id 8118789159994910817  --testnet"
python pylisk.py --option sign_tx --id 8118789159994910817  --testnet
