import argparse
from src.helpers.k8s import K8S
from src.helpers.yaml import YAML


class CronJobs:

    api_instance= K8S().get_batch_v1_api()

    def __init__(self,sub_parser):
        # create the parser for the "cronjobs" sub-command
        parser_cronjobs = sub_parser.add_parser('cronjobs', help='Back up your Kubernetes CronJob objects')
        parser_cronjobs.add_argument('name', nargs='*', help="Specify CronJobs name(s)")
        parser_cronjobs.add_argument('--namespace', dest='namespace', default="default", help="Namespace definition")
        parser_cronjobs.add_argument('--all', '-A', action="store_true", dest='is_all', default=False, help="Get all CronJobs resources in all namespaces")
        return

    def run(self,args):
        # print(args)
        # pass

        responses=[]

        try:
            if args.is_all is True:
                all_cronjobs = self.api_instance.list_cron_job_for_all_namespaces(limit=500, pretty='true')
                for cronjob in all_cronjobs.items:
                    responses.append(cronjob)
            elif args.name is not None:
                for cronjob in args.name :
                    responses.append(self.api_instance.read_namespaced_cron_job(cronjob, args.namespace or "default", pretty='true'))
        except Exception as e:
            print("Exception when calling Kubernetes API Server -- \n" % e)

        for response in responses:
            yaml_dump = YAML().fromObject(response.to_dict(), False)
            print(yaml_dump)