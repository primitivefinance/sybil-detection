# sybil-detection
- `git clone https://github.com/primitivefinance/sybil-detection.git`
- Create a file and name it `.env`
- add a line with information `ETHERSCAN_API=` and set it equal to your etherscan api key
  - If you don't have one you can make one for free [here](https://etherscan.io/myapikey)
- add a second line in the `.env` file with the text `CONTRACT_TO_LOOK_AT=` followed by the contract you want to investigate
- run with `python main.py`

You may need to install relevant dependancies with `pip`
