#!/usr/bin/python
import slackweb
import sys, re

ignoreds = [
 'last message repeated',
 '\/kernel',
 'file:',
 'mib2d',
 'gstatd:',
 'dcd',
 'l2cpd',
 'lldpd',
 'xntpd',
 'mgd',
 'ffp',
 'sshd',
 'LBCM-L2,pfe_bcm_l2_mac_add',
 'downward spike received from pfe',
 'RT_FLOW',
 'PARSE_WARN_NO_ROUTER_AD_CFG',
 'CHASSISD_HWDB_ERROR',
 'DYNAMIC_VPN',
]

ignored_regex  = '|'.join(ignoreds)
ignored = re.compile(ignored_regex)

def send_slack(msg):
  sc = slackweb.Slack(url="https://hooks.slack.com/services/XXXXX/XXXXXX/XXXXXX")
  sc.notify(channel="#network-logs", text=msg, username='NetBot')


for line in sys.stdin:
  if not ignored.search(line):
    send_slack(line)

sys.exit(0)
