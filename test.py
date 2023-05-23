import traceback

import Utils.communications as comms
import Utils.Database as db
import os
import json
import Stockdata.StockProcess as sp
import Utils.communications as comms


def test():
    try:
        slack = os.environ['SLACK_CHANNEL']
        webhook_url = "https://hooks.slack.com/services/" + slack
        channel = "#developement"  # Replace with the desired channel name or ID
        message = "Project test"

        sp.maintain_stocks_data()
    except Exception as e:
        print(f"Error: test: {e}")
        traceback.print_exc()


def stringify(my_json):
    with open(my_json, 'r') as f:
        my_json = json.load(f)
    my_json_string = json.dumps(my_json)
    print(my_json_string)


def data_maintenance():
    try:
        sp.maintain_stocks_data(270)
        message = "Data maintenance executed successfully"
    except Exception as e:
        print(f"Error data_maintenance: {e}")
        traceback.print_exc()
        message = "Problem with Data maintenance"

    try:
        slack = os.environ['SLACK_CHANNEL']
        webhook_url = "https://hooks.slack.com/services/" + slack
        channel = "#developement"  # Replace with the desired channel name or ID
        comms.send_slack_message(webhook_url, channel, message)
    except Exception as e:
        print(f"Error sending Slack message:{e}")
        traceback.print_exc()