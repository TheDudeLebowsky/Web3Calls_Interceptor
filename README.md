# WORK IN PROGRESS

## Description

- This script allows easier analysis of eth read calls from a UI. It launches a webdriver instance with metamask pre-installed.
- Every http requests is stored in data/events.csv.
- Press any key + enter on terminal (or close browser) to stop recording
- Events are filtered and saved to data/web3_readcalls.csv
- A dictionnary containing parsed data from web3 calls is created and is attempted to be decoded with available data from config files + 4bytes API

## Prerequesites

- install seleniumBase
- requirements.txt not available yet
- APIs for explorers

## How to use

- To start recording cdb events, launch modules/request_interceptor.py
- To process and filter requests, launch from filter_df.py : extract_web3_readcalls
- To start decoding, launch from filter_df.py : parse_and_decode
- output is stored in data/decoded_events.csv

## Issues

- To work correctly, a datafile with necessary ABI is stored in config/abi_list.py and contract address are stored in the dictionnary from config/addresses.py
- It is important the format is consistent as shown in examples files
- Some decoding errors might arise. Please provide feedback and bugreports in order to fix the issues
- main.py is in progress to allow the full process to be initiated from here
- DO NOT use for a long period until additional request filter add implemented. (2-3 min max) events.json will get massive really fast leading to unexpected errors

## Whats next

- Additional testing to make sure it handles different formatting
- Fix user data dir and allow multiple extensions
