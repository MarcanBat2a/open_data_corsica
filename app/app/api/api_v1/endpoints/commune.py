from app.app.services import commune_services, gare_services, borne_recharge_services
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import io
import pandas as pd

router = APIRouter()
dict_commmune = commune_services.get_all_communes()

@router.get("/")
def read_communes():
    global dict_commmune
    dict_commmune = commune_services.get_all_communes()
    return dict_commmune


@router.get("/gares")
def read_communes_gares():
    list_gares = gare_services.get_all_gare()
    dict_commmune_gare = commune_services.get_gares_for_all_commune(dict_commmune, list_gares)
    return dict_commmune_gare


@router.get("/bornes")
def read_communes_bornes():
    list_bornes = borne_recharge_services.get_all_borne()
    dict_commmune_borne = commune_services.get_bornes_for_all_commune(dict_commmune, list_bornes)
    return dict_commmune_borne


@router.get("/gares/bornes")
def read_communes_bornes():
    list_gares = gare_services.get_all_gare()
    list_bornes = borne_recharge_services.get_all_borne()
    dict_commmune_gare_borne = commune_services.get_gares_for_all_commune(dict_commmune, list_gares)
    dict_commmune_gare_borne = commune_services.get_bornes_for_all_commune(dict_commmune, list_bornes)
    return dict_commmune_gare_borne


@router.get("/export")
def export_comment(extension:str):

    if extension.lower()=="csv":
        stream = io.StringIO()
        dataframe_result = pd.DataFrame(data=dict_commmune.values())
        dataframe_result.to_csv(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/csv"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.csv"
    elif extension.lower()=="excel":
        stream = io.BytesIO()
        writer = pd.ExcelWriter(stream, engine='xls')
        dataframe_result = pd.DataFrame(data=dict_commmune.values())
        dataframe_result.to_excel(writer, index = False)
        writer.save()
        xlsx_data = stream.getvalue()
        response = StreamingResponse(io.BytesIO(xlsx_data), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response.headers["Content-Disposition"] = "attachment; filename=filename=data.xls"
    else:
        stream = io.StringIO()
        dataframe_result = pd.DataFrame(data=dict_commmune.values())
        dataframe_result.to_json(stream, index = False)
        response = StreamingResponse(iter([stream.getvalue()]),
                                media_type="text/json"
        )
        response.headers["Content-Disposition"] = "attachment; filename=data.json"
    return response