import json
import yaml
def  structure(obj):
    if isinstance(obj,dict):
        return{str(k).lower() :structure(v) for k,v in obj.items() }
    if isinstance(obj):
        return(structure(x) for x in obj)
def load_clean(path):
    if path.endswith(".json"):
        data = json.load("example") 
    else:
        data=yaml.safe_load(path)
    clean=structure(data)
    json.dump(clean,  open("tidy.json" ,"w"), indent=2)             