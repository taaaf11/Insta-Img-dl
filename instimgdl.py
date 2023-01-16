#!/usr/bin/python
import requests
from sys import argv as cmd_line


# avoiding exception

if len(cmd_line) > 1:

    # help message

    if cmd_line[1] == '-h' or cmd_line[1] == '--help' or cmd_line[1] == '-?':

        print('Syntax: instimgdl.py IMAGE_LINK -name OUTPUT_FILE_NAME')

        print('\t-?,-h,--h\t\tShow this help message and exit'
            '\n\tNOTE: This script can\'t download videos!'
            '\n\tExit Codes:'
            '\n\t\t 0: file downloaded successfully'
            '\n\t\t 0: printed help message and exited'
            '\n\t\t 1: no command line arguments supplied')
        exit(0)


    # url starts with https or not
    # requests generates error when not used with http or https
    if cmd_line[1][:8] == 'https://':

        # if the url ends with forwards slash as: instagram.com/p/01234567891/

        if cmd_line[1][-1] == '/':
            r = requests.get(f'{cmd_line[1]}media/?size=l')

        # else
        else:
            r = requests.get(f'{cmd_line[1]}/media/?size=l')

    else:

        if cmd_line[1][-1] == '/':

            r = requests.get(f'https://{cmd_line[1]}media/?size=l')

        else:

            r = requests.get(f'https://{cmd_line[1]}/media/?size=l')

    file_name = cmd_line[cmd_line.index('-name')+1]

    with open(f'{file_name}', 'wb') as f:
        f.write(r.content)

else:
    exit(1)
