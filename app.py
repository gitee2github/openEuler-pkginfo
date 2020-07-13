"""
This is main class for the tool
"""


import os
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
    parser.add_argument("-R", "--repository", type=str, help="get info about a repository")
    parser.add_argument("-c", "--contains", type=str, help="info contains [str/char]")
    parser.add_argument("-s", "--start", type=str, help="info start with [str/char]")
    args = parser.parse_args()

    if args.organization and args.repository:
        my_gitee.get_repos_info(args.organization, args.repository, args.contains, args.start)
    elif args.repository:
        logging.error("Cannot find repository without organization name")
    elif args.organization:
        my_gitee.get_orgs_info(args.organization, args.contains, args.start)
    elif args.contains or args.start:
        logging.error("Cannot get info without organization name or repository name")


if __name__ == '__main__':
    main()
