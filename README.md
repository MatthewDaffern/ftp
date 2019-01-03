About this project
==================
This is an FTP honeypot server

## Why I create this project?
Because I want to be able to steal FTP passwords(legally of course!) without having to download additional packages.

I should just be able to get reverse-shell, set up a listener on my target machine and execute my script.

But, when googling FTP honeypots, All of the ones I could easily find had external dependencies that made them impossible to use for stuff like HTB, and forced the target machine to essentially reach out, or install additional packages.

Well, I fixed that issue.

## Dependencies
None. The upstream repository created a client for this, and it originalyl was just a FTP server.

## Tested on
`Python2.7` & `python3.5`

## Usage
```bash
$ python lol_server.py
```

>Note:
When you run ftp_server.py you may need permission because the ftp server port default run on 20 & 21, may you can run `sudo python ftp_server.py`

When dropping this, you'll need a sudoer privileges or a root account.


## Platform
Currently can only run on Linux like OS e.g Ubuntu, Mac OSX etc.


