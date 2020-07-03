import os
import logging
import requests
import argparse
from gitee import Gitee


def main():
    """main function"""
    if not os.path.exists("gitee.conf"):
        logging.error("config file does not exist")
        return
    commands()

def commands():
    gitee = Gitee("gitee.conf")
    parser = argparse.ArgumentParser(description="test argparse")
    parser.add_argument("-O", "--organization", type=str, help="get info about an organization")
    args = parser.parse_args()

    if args.organization:
        gitee.get_orgs_info(args.organization)

main()