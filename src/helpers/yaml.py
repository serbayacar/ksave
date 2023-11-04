import yaml
import json


class YAML:

    @staticmethod
    def fromJSON(path):
        configuration=json.loads(path)
        dump=yaml.dump(configuration)
    
        return dump

    @staticmethod
    def fromObject(res):
        dump=yaml.safe_dump(res.to_dict())

        return dump

