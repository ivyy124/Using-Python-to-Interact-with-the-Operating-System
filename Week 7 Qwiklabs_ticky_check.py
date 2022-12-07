#!/usr/bin/env python3
import re
import operator
import csv

error = {}
per_user = {}

with open('syslog.log', 'r') as file:
  for line in file:
    result_INFO = re.search(r"ticky: INFO ([\w ']*) \[#\d+\] \(([\w.]+)\)", line)
    result_ERROR = re.search(r"ticky: ERROR ([\w ']*) \(([\w.]+)\)", line)
    if result_INFO:
      username = result_INFO.group(2)
      per_user.setdefault(username, {})
      per_user[username]['INFO'] = per_user[username].get('INFO',0) + 1
    elif result_ERROR:
      username = result_ERROR.group(2)
      errorType = result_ERROR.group(1).strip()
      per_user.setdefault(username, {})
      per_user[username]['ERROR'] = per_user[username].get('ERROR', 0) + 1
      error[errorType] = error.get(errorType, 0) + 1
  file.close()

error_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

with open('error_message.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(['Error', 'Count'])
  writer.writerows(error_list)
  file.close()

with open('user_statistics.csv', 'w') as file:
  writer = csv.writer(file)
  writer.writerow(['Username', 'INFO', 'ERROR'])
  for username in per_user_list:
    writer.writerow([username[0],username[1].get('INFO',0),username[1].get('ERROR',0)])
  file.close()
