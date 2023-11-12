import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class ClusterRoleBinding:

    api_instance= K8S().get_rbac_authorization_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "cronjobs" sub-command
        parser_clusterrolebinding = sub_parser.add_parser('clusterrolebinding', help='clusterrolebinding is cool sub-command')
        parser_clusterrolebinding.add_argument('name', nargs='*', help="Specify ClusterRoleBinding name(s)")
        # parser_clusterrolebinding.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_clusterrolebinding.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all ClusterRoleBinding resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_clusterrolebindings = self.api_instance.list_cluster_role_binding(limit=500, pretty='true')
                for clusterrolebinding in all_clusterrolebindings.items:
                    responses.append(clusterrolebinding)
            elif args.name is not None:
                for clusterrolebinding in args.name :
                    responses.append(self.api_instance.read_cluster_role_binding(clusterrolebinding, pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)
