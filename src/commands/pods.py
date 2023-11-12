import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Pods:

    api_instance= K8S().get_core_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "pod" sub-command
        parser_pod = sub_parser.add_parser('pods', help='pods is cool sub-command')
        parser_pod.add_argument('name', nargs='*', help="Specify pod name(s)")
        parser_pod.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_pod.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Pod resources in all namespaces")
        return

    def run(self, args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_pods = self.api_instance.list_pod_for_all_namespaces(limit=500, pretty='true')
                for pod in all_pods.items:
                    responses.append(pod)
            elif args.name is not None:
                for pod in args.name :
                    responses.append(self.api_instance.read_namespaced_pod(pod, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response)
            print(yaml_dump)