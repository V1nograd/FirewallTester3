
import os
from os import path
import re
from pprint import pprint
from datetime import datetime
import requests

# In order to execute script successfuly install all mentioned libraries higher by executing "pip install <name lib>" in cmd which is run by administrator.


def gather_urls(files):
    dict_items_for_test = {}
    for name in files:
        # if path.exists(name) == False:
        #     open(name, 'w')
        if True:
            list_lines = []
            
            file_read = open(name, 'r')
            for line in file_read:
                list_lines.append(line[:-1])
            file_read.close()
        dict_items_for_test.update({name[:-4]: list_lines})
    return dict_items_for_test


def commands_cmd(list_of_bot_access_commands):
    dict_res = {}
    for url in list_of_bot_access_commands:
        os.chdir("C:\\Program Files\\Google\\Chrome\\Application")
        status = os.system(url)
        if status == 0:
            status = 'success'
        else:
            status = 'error'
        name_url = (re.findall('://(.+?)/', url))[0]
        now = (datetime.now()).strftime("%H:%M:%S")
        dict_update = {name_url: [now, status]}
        dict_res.update(dict_update)
    return dict_res


def test_URLs(list_urls):
    dict_res = {}
    for url in list_urls:
        name_url = re.findall('://(.+?)/', url)[0]
        try:
            response = requests.get(url).content.decode('ISO-8859-1')
            res = (re.findall('(incident ID: .+)</iframe>', response))[0]
            print (res)
        except:
            res = 'not riched'
        now = (datetime.now()).strftime("%H:%M:%S")
        dict_update = {name_url: [now, res]}
        dict_res.update(dict_update)
    return dict_res


def WriteToDict(fname, dict_text):
    with open (fname, 'w') as file:
        for key, value in dict_text.items():
            file.write(f'{key}, {value}\n')


def main():

    # Input in the list "files" names of the files from which commands and urls will be gathered.

    files = ['C:\\Users\\User\\Desktop\\WAF Testing\\WAF Testing\\SQL_injection.txt', 'C:\\Users\\User\\Desktop\\WAF Testing\\WAF Testing\\Bot_access.txt',
             'C:\\Users\\User\\Desktop\\WAF Testing\\WAF Testing\\Cross_site_scripting.txt', 'C:\\Users\\User\\Desktop\\WAF Testing\\WAF Testing\\Illegal_resource_access.txt']  # 1.

    ###

    result_of_testing = {}
    dict_items_for_test = gather_urls(files)  # 2.
    for i in dict_items_for_test:

        if 'chrome' in dict_items_for_test[i][1]:  # 3.
            print(dict_items_for_test[i][1])
            res = commands_cmd(dict_items_for_test[i])
            result_of_testing.update({i: res})
        else:  # 4.
            res = test_URLs(dict_items_for_test[i])
            result_of_testing.update({i: res})
    pprint(result_of_testing)
    pprint(WriteToDict('C:\\Users\\User\\Desktop\\WAF Testing\\WAF Testing\\result_of_testingg.txt', result_of_testing))



if __name__ == "__main__":
    main()

# 1. List of files from which urls and commands will be gathered for testing.
# 2. Process of gathering urls and commands.
# 3. Check if it is a command or url by finding key word "chrome" in the first element of the dict key. If True => process of executing commands in the cmd.
# 4. If raw hasn't "chrome" word, than it is associated with the url and the process of URL testing starts. Time and the imperva id code are written down to the result dict.
# 5. Printing result to the console in the readable format.



