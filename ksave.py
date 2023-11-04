# !/usr/bin/env python

import argparse
import sys

## Command Imports
from src.commands.pods import Pods
from src.commands.deployments import Deployments
from src.commands.statefulsets import StatefulSets
from src.commands.daemonsets import DaemonSets
from src.commands.jobs import Jobs
from src.commands.cronjobs import CronJobs

class KSave(object):

    def __init__(self):
        # create the top-level parser
        parser = argparse.ArgumentParser(prog='ksave')
        # create sub-parser
        sub_parser = parser.add_subparsers(help='sub-command help',dest="subcommand")
        
        # create sub-commands
        subcommands=dict()
        subcommands["podsCommand"] = Pods(sub_parser)
        subcommands["deploymentsCommand"] = Deployments(sub_parser)
        subcommands["daemonsetsCommand"] = DaemonSets(sub_parser)
        subcommands["statefulsetsCommand"] = StatefulSets(sub_parser)
        subcommands["cronjobsCommand"] = CronJobs(sub_parser)
        subcommands["jobsCommand"] = Jobs(sub_parser)

        ## Finally parse all arguments
        args = parser.parse_args()

        ## Run related object functions
        className = str(args.subcommand) + "Command"
        getattr(subcommands[className], "run")(args)

        return


if __name__ == "__main__":
    KSave()