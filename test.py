import Utils.communications as comms
import Utils.Database as db
import os
import json


def test():
    slack = os.environ['SLACK_CHANNEL']
    webhook_url = "https://hooks.slack.com/services/" + slack
    channel = "#developement"  # Replace with the desired channel name or ID
    message = "Project test"

    result = db.test_database()

    # Initialize an empty list to hold the strings
    strings = []

    # Loop over the tuples in the list
    for my_tuple in result:
        # Convert the tuple to a string and append it to the list
        strings.append(str(my_tuple))

    for message in strings:
        comms.send_slack_message(webhook_url, channel, message)



def stringify(my_json):
    with open(my_json, 'r') as f:
        my_json = json.load(f)
    my_json_string = json.dumps(my_json)
    print(my_json_string)
