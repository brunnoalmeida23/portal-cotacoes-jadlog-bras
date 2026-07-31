from reportlab.lib.pagesizes import A4, mm, inch
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io
import os
from datetime import datetime
import re

class CupomPDF:
    def __init__(self):
        # Configuração para impressora térmica 58mm x 297mm
        self.LARGURA_MM = 58  # Largura do papel em mm
        self.ALTURA_MM = 297  # Altura máxima do papel em mm
        
        # Convertendo para pontos (1mm = 2.83465 pontos)
        self.LARGURA_PT = self.LARGURA_MM * 2.83465
        self.ALTURA_PT = self.ALTURA_MM * 2.83465
        
        # Margens em mm
        self.MARGEM_ESQUERDA = 3  # mm
        self.MARGEM_DIREITA = 3   # mm
        self.MARGEM_TOPO = 3      # mm
        self.MARGEM_BASE = 3      # mm
        
        # Largura útil para texto em mm
        self.LARGURA_UTIL_MM = self.LARGURA_MM - self.MARGEM_ESQUERDA - self.MARGEM_DIREITA
        
        # Fonte padrão (usar Helvetica que é suportada nativamente)
        self.FONTE_PADRAO = "Helvetica"
        self.FONTE_NEGRITO = "Helvetica-Bold"
        
        # Tamanhos de fonte em pontos
        self.TAMANHO_TITULO = 10
        self.TAMANHO_SUBTITULO = 8
        self.TAMANHO_NORMAL = 7
        self.TAMANHO_PEQUENO = 6
        self.TAMANHO_DESTAQUE = 12
        
    def _texto_centralizado(self, c, texto, y, tamanho, negrito=False, cor=(0,0,0)):
        """Desenha texto centralizado na largura do cupom"""
        c.setFont(self.FONTE_NEGRITO if negrito else self.FONTE_PADRAO, tamanho)
        c.setFillColorRGB(cor[0], cor[1], cor[2])
        
        # Calcula a largura do texto
        largura_texto = c.stringWidth(texto, self.FONTE_NEGRITO if negrito else self.FONTE_PADRAO, tamanho)
        
        # Centraliza
        x_central = self.MARGEM_ESQUERDA * 2.83465 + (self.LARGURA_UTIL_MM * 2.83465) / 2 - largura_texto / 2
        c.drawString(x_central, y, texto)
        
    def _texto_esquerda(self, c, texto, y, tamanho, negrito=False, cor=(0,0,0)):
        """Desenha texto alinhado à esquerda"""
        c.setFont(self.FONTE_NEGRITO if negrito else self.FONTE_PADRAO, tamanho)
        c.setFillColorRGB(cor[0], cor[1], cor[2])
        x = self.MARGEM_ESQUERDA * 2.83465
        c.drawString(x, y, texto)
        
    def _texto_direita(self, c, texto, y, tamanho, negrito=False, cor=(0,0,0)):
        """Desenha texto alinhado à direita"""
        c.setFont(self.FONTE_NEGRITO if negrito else self.FONTE_PADRAO, tamanho)
        c.setFillColorRGB(cor[0], cor[1], cor[2])
        x_direita = self.MARGEM_ESQUERDA * 2.83465 + self.LARGURA_UTIL_MM * 2.83465
        largura_texto = c.stringWidth(texto, self.FONTE_NEGRITO if negrito else self.FONTE_PADRAO, tamanho)
        c.drawString(x_direita - largura_texto, y, texto)
        
    def _texto_colunas(self, c, texto_esq, texto_dir, y, tamanho, negrito=False):
        """Desenha texto em duas colunas (esquerda e direita)"""
        self._texto_esquerda(c, texto_esq, y, tamanho, negrito)
        self._texto_direita(c, texto_dir, y, tamanho, negrito)
        
    def _linha_horizontal(self, c, y, tipo="simples"):
        """Desenha uma linha horizontal"""
        x1 = self.MARGEM_ESQUERDA * 2.83465
        x2 = (self.MARGEM_ESQUERDA + self.LARGURA_UTIL_MM) * 2.83465
        
        if tipo == "dupla":
            # Linha dupla para separadores importantes
            c.setLineWidth(0.8)
            c.line(x1, y, x2, y)
            c.line(x1, y - 2, x2, y - 2)
        elif tipo == "pontilhada":
            # Linha pontilhada
            c.setDash(2, 2)
            c.setLineWidth(0.3)
            c.line(x1, y, x2, y)
            c.setDash(1, 0)  # Reseta
        else:
            # Linha simples
            c.setLineWidth(0.5)
            c.line(x1, y, x2, y)
            
    def _formatar_moeda(self, valor):
        """Formata valor para moeda brasileira"""
        return f"R$ {valor:.2f}".replace(".", ",")
        
    def _formatar_cep(self, cep):
        """Formata CEP"""
        cep_limpo = re.sub(r"\D", "", str(cep))
        if len(cep_limpo) == 8:
            return f"{cep_limpo[:5]}-{cep_limpo[5:]}"
        return cep_limpo
        
    def _formatar_cpf_cnpj(self, doc):
        """Formata CPF ou CNPJ"""
        doc_limpo = re.sub(r"\D", "", str(doc))
        if len(doc_limpo) == 11:
            return f"{doc_limpo[:3]}.{doc_limpo[3:6]}.{doc_limpo[6:9]}-{doc_limpo[9:]}"
        elif len(doc_limpo) == 14:
            return f"{doc_limpo[:2]}.{doc_limpo[2:5]}.{doc_limpo[5:8]}/{doc_limpo[8:12]}-{doc_limpo[12:]}"
        return doc
        
    def gerar_recibo(self, dados_cotacao):
        """
        Gera um recibo no formato para impressora térmica 58mm x 297mm
        """
        # Cria um buffer para o PDF
        buffer = io.BytesIO()
        
        # Cria o canvas com o tamanho personalizado
        c = canvas.Canvas(buffer, pagesize=(self.LARGURA_PT, self.ALTURA_PT))
        
        # Variável de controle de posição Y (começa do topo)
        y = self.ALTURA_PT - self.MARGEM_TOPO * 2.83465
        
        # ===== CABEÇALHO =====
        # Logo/Identificação
        self._texto_centralizado(c, "JADLOG BRÁS", y, self.TAMANHO_DESTAQUE, negrito=True, cor=(0.8, 0.1, 0.1))
        y -= 6 * 2.83465
        
        self._texto_centralizado(c, "Av. Vautier, 455 - Brás", y, self.TAMANHO_PEQUENO)
        y -= 4 * 2.83465
        
        self._texto_centralizado(c, "São Paulo - SP - CEP: 03032-000", y, self.TAMANHO_PEQUENO)
        y -= 4 * 2.83465
        
        self._texto_centralizado(c, "Tel: (11) 99999-9999", y, self.TAMANHO_PEQUENO)
        y -= 5 * 2.83465
        
        # Linha dupla
        self._linha_horizontal(c, y, "dupla")
        y -= 6 * 2.83465
        
        # ===== TÍTULO =====
        self._texto_centralizado(c, "COTAÇÃO DE FRETE", y, self.TAMANHO_SUBTITULO, negrito=True)
        y -= 5 * 2.83465
        
        # Número da Cotação (destacado)
        self._texto_centralizado(c, f"#{dados_cotacao.get('numero_cotacao', 'N/A')}", y, self.TAMANHO_TITULO, negrito=True)
        y -= 6 * 2.83465
        
        # Data e Hora
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._texto_centralizado(c, f"Gerado em: {data_hora}", y, self.TAMANHO_PEQUENO)
        y -= 5 * 2.83465
        
        self._linha_horizontal(c, y)
        y -= 5 * 2.83465
        
        # ===== DADOS DA COTAÇÃO =====
        self._texto_esquerda(c, "DADOS DA COTAÇÃO", y, self.TAMANHO_NORMAL, negrito=True)
        y -= 5 * 2.83465
        
        # Modalidade
        modalidade = dados_cotacao.get('modalidade', 'PACKAGE')
        self._texto_colunas(c, "Modalidade:", modalidade, y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Origem
        self._texto_colunas(c, "Origem:", "Brás - SP", y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Destino
        destino = dados_cotacao.get('cidade', '')
        uf = dados_cotacao.get('uf', '')
        self._texto_colunas(c, "Destino:", f"{destino}/{uf}" if destino else "N/A", y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # CEP Destino
        cep_destino = self._formatar_cep(dados_cotacao.get('cep_destino', ''))
        self._texto_colunas(c, "CEP Destino:", cep_destino, y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Peso
        peso = dados_cotacao.get('peso', 0)
        self._texto_colunas(c, "Peso:", f"{peso:.3f} kg", y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Tipo de Tarifa
        tipo_tarifa = dados_cotacao.get('tipo_tarifa', '')
        self._texto_colunas(c, "Tipo:", tipo_tarifa, y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Prazo
        prazo = dados_cotacao.get('prazo', '')
        self._texto_colunas(c, "Prazo:", f"{prazo} dias", y, self.TAMANHO_NORMAL)
        y -= 5 * 2.83465
        
        self._linha_horizontal(c, y)
        y -= 5 * 2.83465
        
        # ===== VALORES =====
        self._texto_esquerda(c, "VALORES", y, self.TAMANHO_NORMAL, negrito=True)
        y -= 5 * 2.83465
        
        # Frete Base
        frete = dados_cotacao.get('frete', 0)
        self._texto_colunas(c, "Frete Base:", self._formatar_moeda(frete), y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Seguro
        seguro = dados_cotacao.get('seguro', 0)
        self._texto_colunas(c, "Seguro:", self._formatar_moeda(seguro), y, self.TAMANHO_NORMAL)
        y -= 4.5 * 2.83465
        
        # Valor NF
        valor_nf = dados_cotacao.get('valor_nf', 0)
        if valor_nf:
            self._texto_colunas(c, "Valor NF:", self._formatar_moeda(valor_nf), y, self.TAMANHO_NORMAL)
            y -= 4.5 * 2.83465
        
        # Linha dupla antes do total
        self._linha_horizontal(c, y, "dupla")
        y -= 6 * 2.83465
        
        # TOTAL - Destacado
        total = dados_cotacao.get('total', 0)
        self._texto_colunas(c, "TOTAL:", self._formatar_moeda(total), y, self.TAMANHO_TITULO, negrito=True)
        y -= 6 * 2.83465
        
        self._linha_horizontal(c, y, "dupla")
        y -= 6 * 2.83465
        
        # ===== DADOS DO CLIENTE =====
        if dados_cotacao.get('cliente_nome'):
            self._texto_esquerda(c, "CLIENTE", y, self.TAMANHO_NORMAL, negrito=True)
            y -= 5 * 2.83465
            
            # Nome
            self._texto_esquerda(c, f"Nome: {dados_cotacao['cliente_nome']}", y, self.TAMANHO_NORMAL)
            y -= 4.5 * 2.83465
            
            # Documento
            if dados_cotacao.get('cliente_documento'):
                doc_formatado = self._formatar_cpf_cnpj(dados_cotacao['cliente_documento'])
                self._texto_esquerda(c, f"Documento: {doc_formatado}", y, self.TAMANHO_NORMAL)
                y -= 4.5 * 2.83465
            
            self._linha_horizontal(c, y)
            y -= 5 * 2.83465
        
        # ===== PROMOÇÃO BRÁS =====
        self._texto_centralizado(c, "⭐ VALORES EXCLUSIVOS ⭐", y, self.TAMANHO_NORMAL, negrito=True)
        y -= 4 * 2.83465
        
        self._texto_centralizado(c, "UNIDADE DA AV. VAUTIER, 455", y, self.TAMANHO_PEQUENO)
        y -= 4 * 2.83465
        
        self._texto_centralizado(c, "Válidos até Dezembro/2026", y, self.TAMANHO_PEQUENO)
        y -= 5 * 2.83465
        
        self._linha_horizontal(c, y, "pontilhada")
        y -= 5 * 2.83465
        
        # ===== RODAPÉ =====
        self._texto_centralizado(c, "www.jadlogbras.com.br", y, self.TAMANHO_PEQUENO)
        y -= 4 * 2.83465
        
        self._texto_centralizado(c, "SAC: 0800 123 4567", y, self.TAMANHO_PEQUENO)
        y -= 5 * 2.83465
        
        self._texto_centralizado(c, "Este é um documento de cotação", y, self.TAMANHO_PEQUENO)
        y -= 3.5 * 2.83465
        
        self._texto_centralizado(c, "não possui valor fiscal", y, self.TAMANHO_PEQUENO)
        y -= 4 * 2.83465
        
        # ===== LINHA DE CORTE =====
        self._texto_centralizado(c, "- - - - - - - - - - - - - - - - -", y, self.TAMANHO_PEQUENO)
        
        # Finaliza o PDF
        c.save()
        
        # Pega o valor do buffer
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes