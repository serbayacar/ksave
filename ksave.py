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
from src.commands.secrets import Secrets
from src.commands.configmaps import ConfigMaps
from src.commands.ingress import Ingress
from src.commands.services import Services
from src.commands.storageclass import StorageClass
from src.commands.persistentvolumes import PersistentVolume
from src.commands.persistentvolumeclaims import PersistentVolumeClaim
from src.commands.serviceaccounts import ServiceAccount
from src.commands.roles import Role
from src.commands.rolebindings import RoleBinding
from src.commands.clusterroles import ClusterRole
from src.commands.clusterrolebindings import ClusterRoleBinding

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
        subcommands["secretsCommand"] = Secrets(sub_parser)
        subcommands["configmapsCommand"] = ConfigMaps(sub_parser)
        subcommands["ingressCommand"] = Ingress(sub_parser)
        subcommands["servicesCommand"] = Services(sub_parser)
        subcommands["storageclassCommand"] = StorageClass(sub_parser)
        subcommands["persistentvolumesCommand"] = PersistentVolume(sub_parser)
        subcommands["persistentvolumeclaimsCommand"] = PersistentVolumeClaim(sub_parser)
        subcommands["serviceaccountCommand"] = ServiceAccount(sub_parser)
        subcommands["rolesCommand"] = Role(sub_parser)
        subcommands["rolebindingsCommand"] = RoleBinding(sub_parser)
        subcommands["clusterrolesCommand"] = ClusterRole(sub_parser)
        subcommands["clusterrolebindingsCommand"] = ClusterRoleBinding(sub_parser)

        ## Finally parse all arguments
        args = parser.parse_args()

        ## Run related object functions
        className = str(args.subcommand) + "Command"
        getattr(subcommands[className], "run")(args)

        return


if __name__ == "__main__":
    KSave()