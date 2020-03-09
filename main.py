import requests
import os
import argparse

def check_tasks(token):

  authoriz_template = "Token {}"
  request_headers = {"Authorization":
    authoriz_template.format(token)}
  request_params = {
  "units": -1
  }
  request_url = 'https://dvmn.org/api/long_polling/'
  #request_url = 'https://dvmn.org/api/user_reviews/'

  response = requests.get(request_url,
    headers = request_headers
    #,     params = request_params
    )
  response.raise_for_status()
  tasks_structure = response.json()

  return tasks_structure


if __name__ == '__main__':
  token = os.getenv("DEVMAN_TOKEN")
  print_info = check_tasks(token)
  print(print_info)
