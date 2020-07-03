import logging
import requests
from configparser import ConfigParser


def get_header(config):
    header = {}
    for (each_key, each_val) in config.items("headers"):
        header[each_key] = each_val
    return header


class Gitee:
    """gitee"""
    def __init__(self, config_path):
        config = ConfigParser()
        config.read(config_path)
        self.headers = get_header(config)
        self.baseurl = config.get("url", "baseurl")

    def to_string(self):
        print(self.headers)
        print(self.baseurl)

    def get_orgs_info(self, org_name):
        orgs_url = self.baseurl + "/orgs/" + org_name
        print(orgs_url)

        response = requests.get(orgs_url)
        temp = response.json()[0]
        print(temp.get("login"))
        print(temp.get("url"))

        reps_url = orgs_url + "/repos"
        response = requests.get(reps_url, headers=self.headers)
        print(response.headers["total_count"])
        print("=================================================")
        for each in response.json():
            print(each.get("human_name") + "\t" + each.get("url"))
