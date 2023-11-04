import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML

class StatefulSets:

    api_instance= K8S().get_apps_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "statefull" sub-command
        parser_statefulset = sub_parser.add_parser('statefulsets', help='statefulsets is cool sub-command')
        parser_statefulset.add_argument('name', nargs='*', help="Specify Statefulset name(s)")
        parser_statefulset.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_statefulset.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Statefulset resources in all namespaces")
        return

    def run(self, args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_statefulsets = self.api_instance.list_stateful_set_for_all_namespaces(limit=500, pretty='true')
                for statefulset in all_statefulsets.items:
                    responses.append(statefulset)
            elif args.name is not None:
                for statefulset in args.name :
                    responses.append(self.api_instance.read_namespaced_stateful_set(statefulset, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling AppsV1Api --\n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)