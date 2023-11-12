import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Role:

    api_instance= K8S().get_rbac_authorization_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "cronjobs" sub-command
        parser_role = sub_parser.add_parser('roles', help='role is cool sub-command')
        parser_role.add_argument('name', nargs='*', help="Specify Role name(s)")
        parser_role.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_role.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Role resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_roles = self.api_instance.list_role_for_all_namespaces(limit=500, pretty='true')
                for role in all_roles.items:
                    responses.append(role)
            elif args.name is not None:
                for role in args.name :
                    responses.append(self.api_instance.read_namespaced_role(role, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict())
            print(yaml_dump)
