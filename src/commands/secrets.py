import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML

class Secrets:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "statefull" sub-command
        parser_secret = sub_parser.add_parser('secrets', help='secrets is cool sub-command')
        parser_secret.add_argument('name', nargs='*', help="Specify Secret name(s)")
        parser_secret.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_secret.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Secret resources in all namespaces")
        return

    def run(self, args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_secrets = self.api_instance.list_secret_all_namespaces(limit=500, pretty='true')
                for secret in all_secrets.items:
                    responses.append(secret)
            elif args.name is not None:
                for secret in args.name:
                    responses.append(self.api_instance.read_namespaced_secret(secret, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)