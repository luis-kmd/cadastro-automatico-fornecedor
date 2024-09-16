import requests
from api import api
from PySide6.QtWidgets import QMessageBox

# FUNÇÃO PARA CONSULTAR O CNPJ
def consultar_cnpj(cnpj):
    url = f"https://open.cnpja.com/office/{cnpj}?registrations=BR"
    try:
        # FAZER A REQUISIÇÃO GET
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    # TRATAR ERROS DE REQUISIÇÃO
    except requests.exceptions.HTTPError as err:
        print(f"Erro ao consultar o CNPJ: {err}")
        return {"error": str(err)}
    # TRATAR ERROS DE CONEXÃO
    except requests.exceptions.RequestException as e:
        print(f"Erro ao consultar o CNPJ: {e}")
        return {"error": str(e)}

# FUNÇÃO PARA TRATAR OS DADOS DO CNPJ
def tratar_dados(dados_cnpj):
    # VERIFICAR SE HOUVE ERRO NA CONSULTA
    if 'error' in dados_cnpj:
        print(dados_cnpj['error'])
        return
    
    # ACESSANDO O DICIONÁRIO 'COMPANY' DENTRO DO DICIONÁRIO 'DADOS_CNPJ'
    company_info = dados_cnpj.get('company', {})
    
    # ACESSANDO O CNPJ
    codcgc = dados_cnpj.get('taxId', 'Não disponível')
    
    # FORMATANDO O CNPJ NO FORMATO xx.xxx.xxx/xxxx-xx
    codcgc = codcgc.replace('.', '').replace('/', '').replace('-', '')
    
    # VERIFICANDO SE A CHAVE 'REGISTRATIONS' EXISTE
    registrations = dados_cnpj.get('registrations', [])
    if registrations:
        primeira_inscricao = registrations[0].get('number', 'Não disponível')
    else:
        primeira_inscricao = 'Não disponível'
    
    # ACESSANDO A RAZÃO SOCIAL E NOME ABREVIADO
    razsoc = company_info.get('name', 'Não disponível')
    nomeab = dados_cnpj.get('alias', 'Não disponível')
    
    # VERIFICANDO SE A CHAVE 'ADDRESS' EXISTE
    address = dados_cnpj.get('address', {})
    endereco = address.get('street', '') + ', ' + address.get('number', '')
    bairro = address.get('district', 'Não disponível')
    codmun = address.get('municipality', 'Não disponível')
    estado = address.get('state', 'Não disponível')
    paislo = address.get('country', {}).get('name', 'Não disponível')
    codcep = address.get('zip', 'Não disponível')
    
    # FORMATANDO O CEP NO FORMATO xx.xxx-xxx
    codcep_formatado = formatar_cep(codcep)
    
    # ACESSANDO A DATA DE STATUS
    datsuf = dados_cnpj.get('statusDate', 'Não disponível')

    # RETORNA OS DADOS TRATADOS
    return {
        "codcgc": codcgc,
        "inscricao": primeira_inscricao,
        "razaosocial": razsoc,
        "nomeab": nomeab,
        "endereco": endereco,
        "bairro": bairro,
        "municipio": codmun,
        "estado": estado,
        "pais": paislo,
        "cep": codcep_formatado,  # CEP FORMATADO
        "data_status": datsuf
    }

# FUNÇÃO PARA FORMATAR O CEP
def formatar_cep(cep):
    """FORMAR O CEP NO FORMATO xx.xxx-xxx"""
    cep = cep.replace('.', '').replace('-', '')  
    # REMOVENDO PONTOS E TRAÇOS DO CEP
    if len(cep) == 8:  
        # CERTIFICANDO-SE DE QUE O CEP TEM 8 DÍGITOS
        return f"{cep[:2]}.{cep[2:5]}-{cep[5:]}"
    # RETORNA O CEP FORMATADO
    return cep  

# FUNÇÃO PARA FORMATAR O CNPJ
def formatar_cnpj(cnpj):
    """FORMAR O CNPJ NO FORMATO xx.xxx.xxx/xxxx-xx"""
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')
    # CERTIFICA-SE DE QUE O CNPJ TEM 14 DÍGITOS
    if len(cnpj) == 14:  
        # RETORNA O CNPJ FORMATADO
        return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj  

# FUNÇÃO PARA CADASTRAR O FORNECEDOR
def cadastrar(codcgc, dados_empresa):
    # FORMATANDO O CNPJ
    codcgc_formatado = formatar_cnpj(codcgc)
    codmun = dados_empresa.get('municipio')

    # VERIFICA SE O CNPJ JÁ EXISTE NO BANCO DE DADOS
    verificar = f"SELECT CODCGC FROM RODCLI WHERE CODCGC = '{codcgc_formatado}'"
    resultado = api("GET", verificar)
    
    # SELECIONA O CÓDIGO DO MUNICÍPIO DO BANCO DE DADOS
    verificar_codmun = f"SELECT CODMUN FROM RODMUN WHERE CODIBG = '{codmun}'"
    resultado_codmun = api("GET", verificar_codmun)

    # SELECIONANDO O CÓDIGO NA DICT
    if len(resultado_codmun) > 0:
        resultado_codmun = resultado_codmun[0]['CODMUN']
    else:
        raise("Nenhum município encontrado")

    if resultado:
        # POPUP DE AVISO DE CNPJ JÁ CADASTRADO
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("ESSE CNPJ JÁ ESTÁ CADASTRADO")
        msg.setWindowTitle("Aviso")
        msg.exec()
        return "CNPJ já cadastrado"
    else:
        try:
            # SE O CNPJ NÃO EXISTIR, INSERE NO BANCO DE DADOS
            query_insertforn = (
                f"EXEC SP_InsertForn "
                f"@CODCGC = '{codcgc_formatado}', "
                f"@INSCRI = '{dados_empresa['inscricao']}', "
                f"@RAZSOC = '{dados_empresa['razaosocial']}', "
                f"@NOMEAB = '{dados_empresa['razaosocial']}', "
                f"@ENDERE = '{dados_empresa['endereco']}', "
                f"@BAIRRO = '{dados_empresa['bairro']}', "
                f"@CODMUN = {resultado_codmun}, "
                f"@ESTADO = '{dados_empresa['estado']}', "
                f"@PAISLO = '{dados_empresa['pais']}', "
                f"@CODCEP = '{dados_empresa['cep']}', "
                f"@CODCON = ' ', "
                f"@DATSUF = '{dados_empresa['data_status']}'"
            ).upper()
            # EXECUÇÃO DA PROCEDURE
            api("POST", query_insertforn)

            # SELECIONA O CÓDIGO DO FORNECEDOR CADASTRADO PARA INFORMAR AO USUÁRIO
            codigo = f"SELECT CODCLIFOR FROM RODCLI WHERE CODCGC = '{codcgc_formatado}'"
            resultado_codigo = api("GET", codigo)
            resultado_codigo = resultado_codigo[0]['CODCLIFOR']

            # INSERE NO BANCO DE DADOS A PARTE CONTÁBIL
            query_insertcont = (
                f"EXEC SP_InsertCont "
                f"@DESCRI = '{dados_empresa['razaosocial']}', "
                f"@CODAUX = '{resultado_codigo}', "
                f"@CODCLIFOR = {resultado_codigo}"
            )
            # EXECUÇÃO DA PROCEDURE
            api("POST", query_insertcont)

            # POPUP DE SUCESSO
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"Cadastro realizado com sucesso, código do forncedor é: {resultado_codigo}")
            msg.exec()
            return "sucesso"
        except Exception as e:
            # POPUP DE ERRO
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(f"Houve um erro no cadastro: {str(e)}")
            msg.setWindowTitle("Erro")
            msg.exec()
            return "erro"
