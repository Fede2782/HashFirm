# HashFirm
Discover which firmwares are being tested in Samsung servers. This script uses data which is available to public here https://fota-cloud-dn.ospserver.net/firmware/(CSC)/(MODEL)/version.test.xml.
They are just MD5 hashes so this script does MD5 to all the combinations of a given range and checks if they are present in the public data.

ITV and EUX are officially the only CSCs that are supported at the moment. (Even though other CSCs that use the XX (AP+CP)/OXM (CSC) blocks are supported too).

The time it takes to complete the decryption depends on your CPU speed. A lot of RAM might be required in case of large 

## Features
- ☑️ Beta (Z) flag to include all Z builds of CSC+AP
- ☑️ Works also for tablets and devices without CP block
- ☑️ Handles year change and feature bit change
- ☑️ Easy to use and works on any recent Linux-based distribution with basically no dependencies (md5sum, python3, sed, grep)

## How to use
```bash hashfirm_wrapper.sh <MODEL (string eg. SM-A346B)> <CSC (string eg. EUX)> <START (string eg. U9CXK1)> <END (string eg. U9CXK3)> <HAS_MODEM (bool eg. True)> <CHECK_BETA (bool eg. True)```

Remember that Betas (Z) do increment the major letter so you have to consider it and set the beta option to true like the second example. 

Remember that some AP updates do not increment CP or CSC. If the start value you use if higher than the CP or CSC, since they weren't updated, you won't find anything.

## Examples
![Screenshot 2025-01-30 181619](https://github.com/user-attachments/assets/66c8d13f-9f28-48ac-bbc7-65aaf2b6a7d6)
![Screenshot 2025-01-30 180121](https://github.com/user-attachments/assets/08439f61-0b8f-4669-a662-246f9d2e371a)
![Screenshot 2025-01-30 191613](https://github.com/user-attachments/assets/26743a3c-1215-4c52-a858-6c8623220435)

