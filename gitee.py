"""
This is gitee.com helper
"""

import logging
import requests
from configparser import ConfigParser


def get_header(config):
    """url header"""
    header = {}
    for (each_key, each_val) in config.items("headers"):
        header[each_key] = each_val
    return header


class Gitee(object):
    """gitee"""
    def __init__(self, config_path):
        config = ConfigParser()
        config.read(config_path)
        self.headers = get_header(config)
        self.baseurl = config.get("url", "baseurl")

    def get_orgs_info(self, org_name):
        """get organization info"""
        orgs_url = self.baseurl + "/orgs/" + org_name

        response = requests.get(orgs_url)
        temp = response.json()
        print("orgs:\t" + temp.get("login"))
        print("url:\t" + temp.get("url"))

        reps_url = orgs_url + "/repos"
        response = requests.get(reps_url, headers=self.headers)
        total_page = response.headers["total_page"]
        print("There are " + response.headers["total_count"] + " repositories in " + temp.get("login"))
        print("=================================================")
        
        page = 1
        while (page <= int(total_page)):
            response = requests.get(reps_url + "?page=" + str(page), headers=self.headers)
            page += 1
            for each in response.json():
                print(each.get("human_name") + "\n\t" + each.get("url"))
