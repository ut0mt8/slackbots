#!/usr/bin/python
import slackweb
from sys import argv

def send_slack(json):
  attachments = []
  sc = slackweb.Slack(url="https://hooks.slack.com/services/XXXXXX/XXXXXX/XXXXXXX")
  attachments.append(json)
  sc.notify(channel="#network-traps", username='NetBot', attachments=attachments)

msg = ' '.join(argv[1:])
if 'Up ' in msg:
  json = {"color": "#36a64f", "text": msg}
  send_slack(json)
elif 'Down ' in msg:
  json = {"color": "#a6364f", "text": msg}
  send_slack(json)
else:
  json = {"color": "#cccccc", "text": msg}
  send_slack(json)
