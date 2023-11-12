import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class StorageClass:

    api_instance= K8S().get_storage_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "cronjobs" sub-command
        parser_storageclass = sub_parser.add_parser('storageclass', help='storageclass is cool sub-command')
        parser_storageclass.add_argument('name', nargs='*', help="Specify StorageClass name(s)")
        # parser_storageclass.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_storageclass.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all StorageClass resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_storageclasses = self.api_instance.list_storage_class(limit=500, pretty='true')
                for storageclass in all_storageclasses.items:
                    responses.append(storageclass)
            elif args.name is not None:
                for storageclass in args.name :
                    responses.append(self.api_instance.read_storage_class(storageclass, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)
