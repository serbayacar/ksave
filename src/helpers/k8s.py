from kubernetes import client, config
from os import environ
import datetime


# Loads Kubernetes Config file
config.load_kube_config(config_file = environ.get('KUBECONFIG'))

class K8S:

    @staticmethod
    def get_core_v1_api():
        return client.CoreV1Api()
    
    @staticmethod
    def get_apps_v1_api():
        return client.AppsV1Api()

    @staticmethod
    def get_batch_v1_api():
        return client.BatchV1Api()

    @staticmethod
    def get_networking_v1_api():
        return client.NetworkingV1Api()

    @staticmethod
    def get_storage_v1_api():
        return client.StorageV1Api()