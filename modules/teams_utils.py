import requests
import json
import datetime
from lib.dt_funcs import TPTZ

# MS TEAMS 頻道hook url
teams_pipeline_test_webhook_url='xxxxxxxx'

teams_pipeline_success_webhook_url='xxxxxx'

teams_pipeline_failed_webhook_url='xxxxxx'

class TeamsWebhookException(Exception):
    """custom exception for failed webhook call"""
    pass

class TeamsMessage:
    def __init__(self, hookurl, process_id, start_time, success_status,pipeline_url=''):
        success_payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0076D7",
            "summary": "Pipeline status alert message    ",
            "sections": [
                {
                    "activityTitle": "Pipeline Success Notification",
                    "facts": [
                        {
                            "name": "Activity name:",
                            "value": process_id
                        },
                        {
                            "name": "Activity status:",
                            "value": "Success"
                        },
                        {
                            "name": "Execution duration (s):",
                            "value": (datetime.datetime.now(tz=TPTZ)-start_time).seconds
                        },
                        {
                            "name": "Notification time (UTC+8):",
                            "value": datetime.datetime.now(tz=TPTZ).strftime('%Y-%m-%d %H:%M:%S')
                        },
                        {
                            "name": "Data Factory name:",
                            "value": "datateam-synapse-workspace"
                        }
                    ],
                    "markdown": True
                }
            ],
            "potentialAction": [
                {
                    "@type": "OpenUri",
                    "name": "View Pipeline",
                    "targets": [{
                        "os": "default",
                        "uri": pipeline_url
                    }]
                }
            ]
        }
        failed_payload={
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": "0076D7",
            "summary": "Pipeline status alert message    ",
            "sections": [
                {
                    "activityTitle": "Pipeline Fail Alert    ",
                    "facts": [
                        {
                            "name": "Activity name:",
                            "value": process_id
                        },
                        {
                            "name": "Activity status:",
                            "value": "Failed"
                        },
                        {
                            "name": "Notification time (UTC+8):",
                            "value": datetime.datetime.now(tz=TPTZ).strftime('%Y-%m-%d %H:%M:%S')
                        },
                        {
                            "name": "Data Factory name:",
                            "value": "datateam-synapse-workspace"
                        }
                    ],
                    "markdown": True
                }
            ],
            "potentialAction": [
                {
                    "@type": "OpenUri",
                    "name": "View Pipeline",
                    "targets": [{
                        "os": "default",
                        "uri": pipeline_url
                    }]
                }
            ]
        }
        
        if success_status:
            self.payload=success_payload
        else:
            self.payload=failed_payload
        
        self.hookurl = hookurl

    def text(self, mtext):
        self.payload["text"] = mtext

    def send(self):
        headers = {"Content-Type":"application/json"}
        r = requests.post(
                url=self.hookurl,
                json=self.payload,
                headers=headers, timeout=60)
            
        if r.status_code == 200: 
            return True
        else:
            raise TeamsWebhookException(r.raise_for_status())