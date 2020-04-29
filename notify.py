#! /bin/python3

import argparse
import dateparser
from datetime import datetime
from datetime import timedelta
import subprocess
import os

parser = argparse.ArgumentParser()
parser.add_argument("--todo-dir", type=str)
args = parser.parse_args()

todo_txt_path = os.path.join(args.todo_dir , "todo.txt")


with open(todo_txt_path) as todo_txt:
    todo_txt_content = todo_txt.readlines()

print(todo_txt_content)


for task in todo_txt_content:
    for word in task.split(' '):

        key_value = word.split(':')
        if len(key_value) < 2:
            continue

        if key_value[0] == "due":
            due_date = key_value[1]


        if key_value[0] == "due-time":
            due_time = key_value[1][0:2] + ':' + key_value[1][2:]


    print(due_date)
    print(due_time)
    reminder_time = dateparser.parse("{0} {1}".format(due_date, due_time))
    print(reminder_time)
    
    
    if abs(reminder_time - datetime.now()) < timedelta(minutes=15):
        print("remind!")

        # gotify
        gotify = '{0} {1} '.format("gotify push -p 10", task.rstrip())
        print(gotify)
        
        gotify_process = subprocess.Popen(gotify.split(), stdout=subprocess.PIPE)
        gotify_process.communicate()

        # notify-send
        notify_send = ["notify-send", "--app-name", "TODO", "TODO", task.rstrip()]
        print(notify_send)
        
        notify_send_process = subprocess.Popen(notify_send, stdout=subprocess.PIPE)
        notify_send_process.communicate()
    else:
        print("don't remind!")

