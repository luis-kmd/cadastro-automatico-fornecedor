import sys
from PySide6.QtWidgets import QApplication, QDialog, QPlainTextEdit, QPushButton, QLineEdit, QMessageBox
from PySide6.QtGui import QIcon
from tela import Ui_Dialog
from PySide6.QtCore import Qt

QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

class Cadastro(QDialog):
    def __init__(self):
        super().__init__()

        # Inicializar a interface usando Ui_Dialog
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)  # Configura a UI

        # Definir ícone da janela
        self.setWindowIcon(QIcon('C:\\Users\\Luis Tvc\\Documents\\Cadastro de parceiro comercial\\KMD.ico'))

        # Declarar funções dos botões
        self.Botao_cadastro = self.ui.Lancar
        self.Botao_consulta = self.ui.Consultar
        self.Recebe_CNPJ = self.ui.CNPJreceive
        self.Recebe_detalhes = self.ui.Dadosreceive

        # Declarar sinais
        self.Botao_cadastro.clicked.connect(self.botao_cadastro)
        self.Recebe_CNPJ.textChanged.connect(self.texto_inserido)
        self.Botao_consulta.clicked.connect(self.botao_consulta)

        # Inicialmente, desabilitar os botões
        self.Botao_cadastro.setEnabled(False)
        self.Botao_consulta.setEnabled(False)

        # Armazenando o CNPJ da última consulta
        self.cnpj_consultado = ""

    def texto_inserido(self):
        # Sempre desativa o botão de cadastro quando o texto do CNPJ é alterado
        self.Botao_cadastro.setEnabled(False)

        # Verifica se o texto tem 14 caracteres
        cnpj_atual = self.Recebe_CNPJ.text()
        if len(cnpj_atual) == 14:
            self.Botao_consulta.setEnabled(True)
        else:
            self.Botao_consulta.setEnabled(False)

    def botao_consulta(self):
        # Importar as funções de main.py
        from main import consultar_cnpj, tratar_dados
        cnpj = self.Recebe_CNPJ.text()
        dados_cnpj = consultar_cnpj(cnpj)

        if dados_cnpj:
            # Verifica se houve erro na consulta
            if 'error' in dados_cnpj:
                self.Recebe_detalhes.setPlainText("Erro na consulta ou CNPJ inválido.")
                self.Botao_cadastro.setEnabled(False)
            else:
                # Trata os dados do CNPJ
                dados_empresa = tratar_dados(dados_cnpj)
                if dados_empresa:
                    formatted_data = self.formatar_dados(dados_empresa)
                    self.Recebe_detalhes.setPlainText(formatted_data)
                    self.dados_empresa = dados_empresa  # Armazena os dados formatados
                    self.Botao_cadastro.setEnabled(True)
                    self.cnpj_consultado = cnpj  # Atualiza o CNPJ consultado
        else:
            # Se não houver dados, exibe uma mensagem
            self.Recebe_detalhes.setPlainText("Nenhum dado retornado.")
            self.Botao_cadastro.setEnabled(False)

    def formatar_dados(self, dados_empresa):
        """Formata os dados para exibição no QPlainTextEdit."""
        formatted_data = (
            f"CNPJ: {dados_empresa['codcgc']}\n"
            f"Nome da Empresa: {dados_empresa['razaosocial']}\n"
            f"Inscrição Estadual: {dados_empresa['inscricao']}\n"
            f"Municipio: {dados_empresa['municipio']}\n"
            f"Endereço: {dados_empresa['endereco']}\n"
            f"Bairro: {dados_empresa['bairro']}\n"
            f"Estado: {dados_empresa['estado']}\n"
            f"País: {dados_empresa['pais']}\n"
            f"CEP: {dados_empresa['cep']}\n"
        )
        # Adiciona a data de status se disponível
        return formatted_data

    def botao_cadastro(self):
        from main import cadastrar
        cnpj = self.Recebe_CNPJ.text()
        resultado = cadastrar(cnpj, self.dados_empresa)

        # Exibir mensagem na tela usando QMessageBox
        msg = QMessageBox()
        msg.setWindowTitle("Cadastro")
        msg.setIcon(QMessageBox.Information)
        msg.setText(resultado)
        msg.exec()

        if "sucesso" in resultado:
            # Limpa os dados após cadastro bem-sucedido
            self.Recebe_detalhes.clear()  
            self.Botao_cadastro.setEnabled(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Cadastro()
    # Exibe a janela
    window.show()  
    sys.exit(app.exec())
