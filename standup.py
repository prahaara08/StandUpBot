import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

def post_message(channel, text):
    try:
        response = client.chat_postMessage(channel=channel, text=text)
    except SlackApiError as e:
        print(f"Error posting message: {e}")

def remind_team_members():
    # List of channel IDs or user IDs
    team_members = ["U12345678", "U23456789", "U34567890"]
    reminder_message = "Please post your standup update!"

    for member in team_members:
        post_message(member, reminder_message)

if __name__ == "__main__":
    remind_team_members()
