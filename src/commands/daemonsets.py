import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class DaemonSets:

    api_instance= K8S().get_apps_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "daemonsets" sub-command
        parser_daemonsets = sub_parser.add_parser('daemonsets', help='daemonsets is cool sub-command')
        parser_daemonsets.add_argument('name', nargs='*', help="Specify Daemonsets name(s)")
        parser_daemonsets.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_daemonsets.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Daemonsets resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_daemonsets = self.api_instance.list_daemon_set_for_all_namespaces(limit=500, pretty='true')
                for daemonset in all_daemonsets.items:
                    responses.append(daemonset)
            elif args.name is not None:
                for daemonset in args.name :
                    responses.append(self.api_instance.read_namespaced_daemon_set(daemonset, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)
