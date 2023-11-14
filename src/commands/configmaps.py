import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML

class ConfigMaps:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "configmap" sub-command
        parser_configmap = sub_parser.add_parser('configmaps', help='Back up your Kubernetes ConfigMap objects')
        parser_configmap.add_argument('name', nargs='*', help="Specify Configmap name(s)")
        parser_configmap.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_configmap.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Configmap resources in all namespaces")
        return

    def run(self, args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_configmaps = self.api_instance.list_config_map_for_all_namespaces(limit=500, pretty='true')
                for configmap in all_configmaps.items:
                    responses.append(configmap)
            elif args.name is not None:
                for configmap in args.name :
                    responses.append(self.api_instance.read_namespaced_config_map(configmap, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict(), False)
            print(yaml_dump)