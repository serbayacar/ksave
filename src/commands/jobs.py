import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class Jobs:

    api_instance= K8S().get_batch_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "jobs" sub-command
        parser_jobs = sub_parser.add_parser('jobs', help='Back up your Kubernetes Job objects')
        parser_jobs.add_argument('name', nargs='*', help="Specify Jobs name(s)")
        parser_jobs.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_jobs.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all Jobs resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_jobs = self.api_instance.list_job_for_all_namespaces(limit=500, pretty='true')
                for job in all_jobs.items:
                    responses.append(job)
            elif args.name is not None:
                for job in args.name :
                    responses.append(self.api_instance.read_namespaced_job(job, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict(), False)
            print(yaml_dump)
