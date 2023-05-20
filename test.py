import Utils.communications as comms
import os


def test():
    slack = os.environ['Slack']
    webhook_url = "https://hooks.slack.com/services/" + slack
    channel = "#developement"  # Replace with the desired channel name or ID
    message = "Hello, Slack!"

    comms.send_slack_message(webhook_url, channel, message)
