class Descriptor:
    main = {
        "main_description": "Easily back up your Kubernetes resources as YAML, as it should be.",
        "help_usage": """
        ksave [kubernetes_resource] [resource_name] <args>;
        
        Workloads Resource Lists :
        pods            Backup your pod resources
        deployments
        statefullsets       
        daemonsets
        jobs
        cronjobs

        Volumes Resource Lists :
        persistentVolumes
        persistentVolumeClaims
        storageClass      
    
        Configuration Resource Lists:
        configMaps
        secrets
        """,
    }

    pod = {
        "main_description": "Backup your pod resources",
    }


    @staticmethod
    def get_main_string(arg_name):
        return Descriptor.main.get(arg_name)

    @staticmethod
    def get_pod_string(arg_name):
        return Descriptor.pod.get(arg_name)
