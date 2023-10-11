#!/usr/bin/env python
"""
file: tools
author: adh
created_at: 9/21/23 3:20 PM
"""
from ssvc.decision_points.base import SsvcDecisionPoint
from ssvc.dp_groups.base import SsvcDecisionPointGroup, get_all_decision_points_from
import inspect
import json

def write_json(fname: str, dp: SsvcDecisionPoint) -> None:
    with open(fname, "w") as f:
        print(f"Writing {fname}")
        f.write(dp.to_json(indent=2))
        f.write("\n")


def write_markdown_table(fname: str, dp: SsvcDecisionPoint) -> None:
    with open(fname, "w") as f:
        print(f"Writing {fname}")
        f.write(dp.to_table())
        f.write("\n")


def dump_dp(dp: SsvcDecisionPoint, path: str = None) -> None:
    if path is None:
        # act like we're in a json list
        lines = [f"  {line}" for line in dp.to_json(indent=2).split("\n")]
        print("\n".join(lines) + ",")
    else:
        basename = dp.name.strip().lower().replace(" ", "_")

        json_fname = f"{path}/{basename}.json"
        write_json(json_fname, dp)

        table_fname = f"{path}/{basename}.md"
        write_markdown_table(table_fname, dp)


def group_to_jsonfiles(group: SsvcDecisionPointGroup, path: str = None) -> None:
    for dp in group.decision_points:
        dump_dp(dp, path)


def get_obj_schema(obj):
    props = {}
    jtypes = {str: "string", float: "number",int: "integer",
              dict: "object", list: "array", bool: "boolean",
              None: "null", tuple: "array"}
    if hasattr(obj,'__dataclass_fields__'):
        dcf = getattr(obj,'__dataclass_fields__')
        for k in list(dcf.keys()):
            stype = dcf[k].type
            #stype can be a Class where mtype will be python Type
            mtype = stype.mro()[0]
            props[k] = {}
            if mtype in jtypes:
                props[k]["type"] = jtypes[mtype]
            if dcf[k].metadata.get('description'):
                props[k]["description"] = dcf[k].metadata.get('description')
            else:
                props[k]["description"] = k
            if hasattr(stype,'__args__'):
                if len(stype.__args__) > 0:
                    if inspect.isclass(stype.__args__[0]):
                        childobj = stype.__args__[0]
                        if hasattr(childobj,'schemaprops'):
                            ftype = props[k]["type"]
                            props[k] = childobj.schemaprops(False)
                            props[k]["type"] = ftype
                        props[k]["items"] = {"type": "object"}
                        props[k]["items"]["properties"] = get_obj_schema(childobj)
    return props
        
def get_schema(obj):
    if hasattr(obj,'schemaprops'):
        schema = obj.schemaprops()
        schema['properties'] = get_obj_schema(obj)        
        if 'additionalProperties' in schema and schema['additionalProperties'] == False:
            schema["required"] = list(schema['properties'].keys())
        return schema
    raise('No schemaprops defined for the Object')

def main():
    from ssvc.dp_groups.v1 import SSVCv1
    from ssvc.dp_groups.v2 import SSVCv2
    from ssvc.dp_groups.v2_1 import SSVCv2_1
    from ssvc.dp_groups.cvss.v1 import CVSSv1
    from ssvc.dp_groups.cvss.v2 import CVSSv2
    from ssvc.dp_groups.cvss.v3 import CVSSv3

    # extract all decision points from the groups
    dps = get_all_decision_points_from(
        [SSVCv1, SSVCv2, SSVCv2_1, CVSSv1, CVSSv2, CVSSv3]
    )
    print("[")
    for dp in dps:
        dump_dp(dp, None)
    print("]")

    for obj in [SsvcDecisionPointGroup,SsvcDecisionPoint]:
        print(json.dumps(get_schema(obj),indent=4))

    
if __name__ == "__main__":
    main()
