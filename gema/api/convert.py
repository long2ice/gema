from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from gema.schema import ConvertReq, ConvertRes
from gema.utils import get_dest_cls, get_source_cls

router = APIRouter()


@router.post("", response_model=ConvertRes)
async def convert(req: ConvertReq):
    source_cls = get_source_cls(req.source_type)
    sb = source_cls(req.content)
    decoded = sb.decode()
    try:
        dest_cls = get_dest_cls(req.language, req.dest_type)
    except IndexError:
        raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="No such dest")
    db = dest_cls(sb.get_model(decoded), **(req.config or {}))
    return {"content": db.render()}
