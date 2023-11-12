import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class PersistentVolumeClaim:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "persistentvolumeclaims" sub-command
        parser_peristentvolumeclaims = sub_parser.add_parser('peristentvolumeclaims', help='Back up your Kubernetes PersistentVolumeClaim objects')
        parser_peristentvolumeclaims.add_argument('name', nargs='*', help="Specify peristentvolumeclaims name(s)")
        parser_peristentvolumeclaims.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_peristentvolumeclaims.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all PeristentVolumeClaims resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_peristentvolumeclaims = self.api_instance.list_persistent_volume_claim_for_all_namespaces(limit=500, pretty='true')
                for peristentvolumeclaim in all_peristentvolumeclaims.items:
                    responses.append(peristentvolumeclaim)
            elif args.name is not None:
                for peristentvolumeclaim in args.name :
                    responses.append(self.api_instance.read_namespaced_persistent_volume_claim(peristentvolumeclaim, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict())
            print(yaml_dump)
