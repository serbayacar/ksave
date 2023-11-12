import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class PersistentVolume:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "persistentvolumes" sub-command
        parser_persistent_volumes = sub_parser.add_parser('persistentvolumes', help='Back up your Kubernetes PersistentVolume objects')
        parser_persistent_volumes.add_argument('name', nargs='*', help="Specify PersistentVolume name(s)")
        # parser_persistent_volumes.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_persistent_volumes.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all PersistentVolume resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_persistent_volumes = self.api_instance.list_persistent_volume(limit=500, pretty='true')
                for persistent_volume in all_persistent_volumes.items:
                    responses.append(persistent_volume)
            elif args.name is not None:
                for persistent_volume in args.name :
                    responses.append(self.api_instance.read_persistent_volume(persistent_volume, pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict())
            print(yaml_dump)
