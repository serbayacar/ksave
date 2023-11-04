import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Deployments:

    api_instance= K8S().get_apps_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "pod" sub-command
        parser_deployment = sub_parser.add_parser('deployments', help='deployments is cool sub-command')
        parser_deployment.add_argument('name', nargs='*', help="Specify Deployment name(s)")
        parser_deployment.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_deployment.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Deployment resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_deployments = self.api_instance.list_deployment_for_all_namespaces(limit=500, pretty='true')
                for deployment in all_deployments.items:
                    responses.append(deployment)
            elif args.name is not None:
                for deployment in args.name :
                    responses.append(self.api_instance.read_namespaced_deployment(deployment, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling AppsV1Api --\n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)