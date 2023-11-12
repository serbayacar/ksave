import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Ingress:

    api_instance= K8S().get_networking_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "pod" sub-command
        parser_ingress = sub_parser.add_parser('ingress', help='ingresss is cool sub-command')
        parser_ingress.add_argument('name', nargs='*', help="Specify Ingress name(s)")
        parser_ingress.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_ingress.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Ingress resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_ingresses = self.api_instance.list_ingress_for_all_namespaces(limit=500, pretty='true')
                for ingress in all_ingresses.items:
                    responses.append(ingress)
            elif args.name is not None:
                for ingress in args.name :
                    responses.append(self.api_instance.read_namespaced_ingress(ingress, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling AppsV1Api --\n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)