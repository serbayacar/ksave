import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class ServiceAccount:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "cronjobs" sub-command
        parser_serviceaccount = sub_parser.add_parser('serviceaccount', help='serviceaccount is cool sub-command')
        parser_serviceaccount.add_argument('name', nargs='*', help="Specify ServiceAccount name(s)")
        parser_serviceaccount.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_serviceaccount.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all ServiceAccount resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_serviceaccounts = self.api_instance.list_service_account_for_all_namespaces(limit=500, pretty='true')
                for serviceaccount in all_serviceaccounts.items:
                    responses.append(serviceaccount)
            elif args.name is not None:
                for serviceaccount in args.name :
                    responses.append(self.api_instance.read_service_account(serviceaccount, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling BatchV1Api --\n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)
