import requests
import os
import argparse

def check_tasks(token):

    authoriz_template = "Token {}"
    request_headers = {"Authorization":
      authoriz_template.format(token)}
    request_url = 'https://dvmn.org/api/long_polling/'
  #request_url = 'https://dvmn.org/api/user_reviews/'

    request_params = ""

    while True:

        response = requests.get(request_url,
            headers = request_headers,
            params = request_params
            timeout = 60
        )
        response.raise_for_status()
        tasks_structure = response.json()
        if tasks_structure.status == "found":
            timestamp = tasks_structure.last_attempt_timestamp
        else:
            timestamp = tasks_structure.timestamp_to_request

        request_params = {
            "timestamp": timestamp
        }

    return tasks_structure


if __name__ == '__main__':
    token = os.getenv("DEVMAN_TOKEN")
    print_info = check_tasks(token)
    print(print_info)


