import settings
import datetime as date
from src import parserXLSX
import calendar
import sys
from connectOracle import utils
from loguru import logger

def makeFile(seq : str, value : str) -> str:

    #data 6
    year = date.datetime.now().year
    month = (date.datetime.now().month) - 1
    if (month == 0):
        month = 12
        year -= 1
    lastDay = calendar.monthrange(year, month)[1]
    content = str(lastDay) +""+  str(month).zfill(2) +""+ str(year)[-2::]

    #num lancamento 7
    content += "1729909"

    #tipo de lancamento 1
    content += "V"

    #codigo historico 4
    content += "0000"

    #descrição
    description = "Reconhecimento da provisao de ferias ja pagas ref competencia " + str(month).zfill(2) + "/" + str(year)
    for i in range(0, 100 - len(description)):
        description += " "
    content += description

    #valor do lancamento
    content += value.zfill(15)

    #valor do lancamento FCM
    content += "000000000000000"

    #numero da conta debito  210601002
    content += "210601002".zfill(15)

    #tipo entidade a debito
    content += "  "

    #codigo entidade a debito
    content += "00000000"

    #centro responsabilidade a debito
    content += "000000"

    #numero da conta a credito
    content += "110301034".zfill(15)

    #tipo de entidade a credito
    content += "PE"

    #codigo de entidade a credito
    content += seq.zfill(8)

    #centro de responsabilidade a credito
    content += "000000"

    #origem do lancamento
    content += "RML"

    #indicador de inconsistencia
    content += "0"

    #numero da empresa
    content += "001"

    content += "\n"

    return content

def runConverter(file : str) -> str:
    logger.add("log/app.log", rotation="5 MB", level="INFO")
    logger.info(file)

    try:
        dicFile = parserXLSX.parserFile_dict(file)
    except Exception as e:
        logger.exception(f"Ocorreu um erro: {e} ->" + " Matricula em branco")
        sys.exit(1)

    content = ''
    for matriculation in dicFile.keys():
        query_result = utils.sql_query("select distinct seqpessoa from ge_pessoa where matricula = " +  matriculation)
        
        if query_result is None:
            content += "Matricula = " + matriculation + " -> Nao encontrado\n"
            break
        else:
            seq = str(query_result).replace("(","").replace(")","").replace(",","")
            content += makeFile(seq, dicFile.get(matriculation))

    logger.info("Sucesso!")
    return content