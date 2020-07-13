"""
This is gitee.com helper
"""

import logging
import requests
import utils
from configparser import ConfigParser


class Gitee(object):
    """gitee"""
    def __init__(self, config_path):
        config = ConfigParser()
        config.read(config_path)
        self.headers = utils.get_header(config)
        self.baseurl = config.get("url", "baseurl")

    def get_orgs_info(self, org_name, contains, start):
        """get organization info"""
        orgs_url = self.baseurl + "/orgs/" + org_name

        response = requests.get(orgs_url, params=utils.get_param(1), headers=self.headers)
        temp = response.json()
        print("orgs:\t" + temp.get("login"))
        print("url:\t" + temp.get("url"))
        print("=================================================")

        reps_url = orgs_url + "/repos"
        response = requests.get(reps_url, params=utils.get_param(1), headers=self.headers)
        total_page = response.headers["total_page"]

        page = 1
        count = 0
        while page <= int(total_page):
            response = requests.get(reps_url, params=utils.get_param(page), headers=self.headers)
            page += 1
            for each in response.json():
                print_each = True
                temp = each.get("human_name").split("/")[-1]
                if contains is not None:
                    print_each = utils.is_contains(temp, contains)
                if print_each and start is not None:
                    print_each = utils.is_start_with(temp, start)
                if print_each:
                    pirint(temp + "\n\t" + each.get("url"))
                    count += 1
        print("=================================================")
        print("Find " + str(count) + " satisfied")

    def get_repos_info(self, org_name, repo_name, contains, start):
        """get repository info"""
        repo_url = self.baseurl + "/repos/" + org_name.lower() + "/" + repo_name
        response = requests.get(repo_url, params=utils.get_param(1), headers=self.headers)
        if response is None:
            logging.error("url does not exist")
            return
        if contains is None and start is None:
            print(org_name + "\t" + repo_name)
        else:
            print(org_name + "\t" + repo_name + "\t" + contains + "\t" + start)
