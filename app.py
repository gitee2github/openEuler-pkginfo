"""
This is main class for the tool
"""


import logging
import requests
import argparse
import gitee


def main():
    """main function"""
    if not os.path.exists("gitee.conf"):
        logging.error("config file does not exist")
        return
    commands()


def commands():
    """list all commands in tool"""
    my_gitee = gitee.Gitee("gitee.conf")
    parser = argparse.ArgumentParser(description="test argparse")
    parser.add_argument("-O", "--organization", type=str, help="get info about an organization")
    args = parser.parse_args()

    if args.organization:
        my_gitee.get_orgs_info(args.organization)


if __name__ == '__main__':
    main()

