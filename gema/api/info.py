from fastapi import APIRouter

from gema.utils import source_cls_map, dest_cls_map

router = APIRouter()


@router.get("")
async def get_info():
    ret = {"source": [], "dest": {}}
    for k in source_cls_map.keys():
        ret["source"].append(k.value)
    for k, v in dest_cls_map.items():
        ret["dest"][k] = [x.value for x in v.keys()]

    return ret
