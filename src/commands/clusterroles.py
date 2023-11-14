import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class ClusterRole:

    api_instance= K8S().get_rbac_authorization_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "clusterrole" sub-command
        parser_clusterrole = sub_parser.add_parser('clusterroles', help='Back up your Kubernetes ClusterRole objects')
        parser_clusterrole.add_argument('name', nargs='*', help="Specify ClusterRole name(s)")
        # parser_clusterrole.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_clusterrole.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all ClusterRole resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_clusterroles = self.api_instance.list_cluster_role(limit=500, pretty='true')
                for clusterrole in all_clusterroles.items:
                    responses.append(clusterrole)
            elif args.name is not None:
                for clusterrole in args.name :
                    responses.append(self.api_instance.read_cluster_role(clusterrole, pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict(), False)
            print(yaml_dump)
