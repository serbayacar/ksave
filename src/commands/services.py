import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Services:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "services" sub-command
        parser_service = sub_parser.add_parser('services', help='Back up your Kubernetes Services objects')
        parser_service.add_argument('name', nargs='*', help="Specify Service name(s)")
        parser_service.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_service.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Service resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_services = self.api_instance.list_service_for_all_namespaces(limit=500, pretty='true')
                for service in all_services.items:
                    responses.append(service)
            elif args.name is not None:
                for service in args.name :
                    responses.append(self.api_instance.read_namespaced_service(service, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict(), False)
            print(yaml_dump)