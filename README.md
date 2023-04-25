# LinuxGPT

A command line tool using AI to harness the power of the CLI with natural language

![LinuxGPT Icon](https://raw.githubusercontent.com/Uglesoft/linuxgpt/main/ICON.png)

## Quickstart

```bash
git clone https://gitlab.com/uglesoft/openware/linuxgpt
cd linuxgpt
bash linuxgpt create a file named after a flower and give it read only permissions
```

## Installation

Navigate to a directory of your choosing and execute the following

```bash
git clone https://gitlab.com/uglesoft/openware/linuxgpt
```

## Configuration

You'll need to add your OpenAI api key to the .env file, and edit your ~/.bashrc file to include the following line

```
export PATH="$PATH:/PATH_TO_LINUXGPT_FOLDER_HERE"
```

And replace PATH_TO_LINUXGPT_FOLDER_HERE with the appropriate path for your system. Something like `/home/username/linuxgpt` is likely.

## Usage

From anywhere on your system as the user you've configured linuxgpt as,

```bash
linuxgpt ${a natural language request describing what you want done goes here}
```

linuxgpt will do it's best to try and perform the task you've requested. It is best at compensating for a lack of syntax knowledge for simple tasks, but can perform more complicated somewhat unreliably.

Example input
```bash
linuxgpt create a file named after a flower and give it read only permissions
```

Example output
```bash
Attempting the following command: touch rose.txt && chmod 444 rose.txt
```

Example input
```bash
linuxgpt show me all folders and files with permissions
```

Example output
```bash
Attempting the following command: ls -al
total 196
drwxrwxr-x 3 chris chris   4096 Apr 23 11:04 .
drwxrwxr-x 7 chris chris   4096 Apr 20 05:56 ..
-rw-rw-r-- 1 chris chris     71 Apr 20 05:46 .env
drwxrwxr-x 8 chris chris   4096 Apr 20 06:18 .git
-rw-rw-r-- 1 chris chris      4 Apr 20 05:54 .gitignore
-rw-rw-r-- 1 chris chris 166530 Apr 20 05:13 ICON.png
-rwxrwxr-x 1 chris chris    215 Apr 20 05:51 linuxgpt
-rw-rw-r-- 1 chris chris   3221 Apr 20 05:46 main.py
-rw-rw-r-- 1 chris chris   2025 Apr 23 11:03 README.md
-r--r--r-- 1 chris chris      0 Apr 23 11:04 rose.txt
```

## Authors

Christian J Kesler, Uglesoft