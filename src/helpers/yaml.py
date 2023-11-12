import yaml
import json

trim_keys= ["api_version","kind","metadata","spec"]

class YAML:

    @staticmethod
    def fromJSON(path):
        configuration=json.loads(path)
        dump=yaml.dump(configuration)
    
        return dump

    @staticmethod
    def fromObject(obj,trimmed=True):
        if trimmed is True:
            extracted_values = {key: obj.get(key) for key in trim_keys}
            dump=yaml.safe_dump(extracted_values)
        else:
            dump= yaml.safe_dump(obj)

        return "---\n" + dump.strip()

