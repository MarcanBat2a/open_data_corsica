from app.app.services import gare_services
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import io
import pandas as pd
import json

router = APIRouter()

@router.get("/")
def read_gares():
    return gare_services.get_all_gare()


@router.get("/communes")
def read_gares_communes():
    return gare_services.get_commune_for_all_gare()


@router.get("/export")
def export_comment(extension:str):

    if extension.lower()=="csv":
        stream = io.StringIO()
        dataframe_result = pd.DataFrame(data=gare_services.get_all_gare())
        dataframe_result.to_csv(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/csv"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    elif extension.lower()=="xlsx":
        stream = io.BytesIO()
        writer = pd.ExcelWriter(stream, engine='xlsxwriter')
        dataframe_result = pd.DataFrame(data=gare_services.get_all_gare())
        dataframe_result.to_excel(writer, index = False)
        writer.save()
        xlsx_data = stream.getvalue()
        response = StreamingResponse(io.BytesIO(xlsx_data), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response.headers["Content-Disposition"] = "attachment; filename=filename=data.xls"
    else:
        stream = io.StringIO()
        result = json.dump(gare_services.get_all_gare_to_dict(), stream)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/json"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.json"
    return response