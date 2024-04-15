from openpyxl import load_workbook
from loguru import logger

def parserFile(file):
    wb = load_workbook(filename= file, data_only=True)
    ws = wb['Planilha1']

    matriculationCol = 'A'
    valueCol = 'B'
    logger.debug("Linhas da planilha[" + matriculationCol + "] = " + str(len(ws[matriculationCol])))   
    logger.debug("Linhas da planilha[" + valueCol + "] = " + str(len(ws[matriculationCol])))

    dic = {}
    for i in range(1, len(ws[matriculationCol]) + 1):
        key = ws[matriculationCol + str(i)].value
        if key is None:
            error = str(matriculationCol) + "[" + str(i) +"]" + " = Matricula em branco"
            logger.error(error)
            raise Exception("Ocorreu um erro => Matricula em branco")
        value = str(ws[valueCol + str(i)].value).replace(" ", "").replace(".","").replace(",","")
        
        dic.update({ str(key).replace(" ", "") : value })
    
    return dic