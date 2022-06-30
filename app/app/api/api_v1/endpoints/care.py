from app.app.services import care_services
from fastapi import APIRouter, status, Response
from fastapi.responses import StreamingResponse
import io
import pandas as pd
import json

router = APIRouter()

@router.get("/")
def read_cares():
    return care_services.get_all_care()


@router.get("/communes")
def read_cares_communes():
    return care_services.get_commune_for_all_care()


@router.get("/export")
def export_comment(extension:str):
    if extension.lower()=="csv":
        stream = io.StringIO()
        dataframe_result = pd.DataFrame(data=care_services.get_all_care())
        dataframe_result.to_csv(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/csv"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    elif extension.lower()=="xlsx":
        stream = io.BytesIO()
        writer = pd.ExcelWriter(stream, engine='xlsxwriter')
        dataframe_result = pd.DataFrame(data=care_services.get_all_care())
        dataframe_result.to_excel(writer, index = False)
        writer.save()
        xlsx_data = stream.getvalue()
        response = StreamingResponse(io.BytesIO(xlsx_data), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response.headers["Content-Disposition"] = "attachment; filename=filename=data.xls"
    else:
        stream = io.StringIO()
        result = json.dump(care_services.get_all_care_to_dict(), stream)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/json"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.json"
    return response