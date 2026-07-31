from reportlab.lib.pagesizes import mm
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import datetime
import io

class CupomPDF:
    def __init__(self):
        # Tamanho da etiqueta: 100mm x 150mm (Zebra GC420t)
        self.LARGURA_MM = 100
        self.ALTURA_MM = 150
        self.MARGEM = 5  # mm
        
    def gerar_recibo(self, dados):
        """Gera um recibo em PDF no tamanho da etiqueta Zebra"""
        
        # ===== VERIFICAÇÃO DE SEGURANÇA =====
        if not dados:
            raise ValueError("Dados da cotação não fornecidos")
        
        # Garantir que todos os campos existam com valores padrão
        dados_seguros = {
            'numero_cotacao': dados.get('numero_cotacao', 'COT-2026-0001'),
            'cliente_nome': dados.get('cliente_nome') or 'NÃO INFORMADO',
            'cliente_documento': dados.get('cliente_documento') or '',
            'cidade': dados.get('cidade') or 'NÃO INFORMADO',
            'uf': dados.get('uf') or '',
            'cep_destino': dados.get('cep_destino') or '00000-000',
            'peso': dados.get('peso', 0),
            'frete': dados.get('frete', 0),
            'seguro': dados.get('seguro', 0),
            'total': dados.get('total', 0),
            'modalidade': dados.get('modalidade', 'PACKAGE')
        }
        
        buffer = io.BytesIO()
        c = canvas.Canvas(
            buffer, 
            pagesize=(self.LARGURA_MM * mm, self.ALTURA_MM * mm)
        )
        
        # Configurações
        c.setPageCompression(0)
        
        # Cores
        VERMELHO_JADLOG = colors.HexColor('#E31E24')
        PRETO = colors.black
        CINZA = colors.HexColor('#666666')
        
        # Posições
        margem = self.MARGEM * mm
        largura = self.LARGURA_MM * mm
        altura = self.ALTURA_MM * mm
        
        # ===== CABEÇALHO =====
        y = altura - 8 * mm
        
        # Logo
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(VERMELHO_JADLOG)
        c.drawString(margem, y, "JADLOG BRÁS")
        
        # Linha
        y -= 2 * mm
        c.setStrokeColor(VERMELHO_JADLOG)
        c.setLineWidth(1.5)
        c.line(margem, y, largura - margem, y)
        
        # ===== TÍTULO =====
        y -= 6 * mm
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(PRETO)
        c.drawString(margem, y, "RECIBO DE COTAÇÃO")
        
        # ===== DADOS =====
        y -= 7 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "NÚMERO:")
        
        y -= 4 * mm
        c.setFont("Helvetica-Bold", 10)
        c.setFillColor(PRETO)
        c.drawString(margem, y, dados_seguros['numero_cotacao'])
        
        # Cliente
        y -= 9 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "CLIENTE:")
        
        y -= 4 * mm
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        cliente = dados_seguros['cliente_nome'][:30]
        c.drawString(margem, y, cliente)
        
        # CPF/CNPJ (opcional)
        if dados_seguros['cliente_documento']:
            y -= 8 * mm
            c.setFont("Helvetica-Bold", 8)
            c.setFillColor(CINZA)
            c.drawString(margem, y, "CPF/CNPJ:")
            
            y -= 4 * mm
            c.setFont("Helvetica", 9)
            c.setFillColor(PRETO)
            c.drawString(margem, y, dados_seguros['cliente_documento'])
        
        # Destino
        y -= 9 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "DESTINO:")
        
        y -= 4 * mm
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        destino = f"{dados_seguros['cidade']}/{dados_seguros['uf']}"
        c.drawString(margem, y, destino)
        
        # CEP
        y -= 8 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "CEP:")
        
        y -= 4 * mm
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        c.drawString(margem, y, dados_seguros['cep_destino'])
        
        # Peso
        y -= 8 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "PESO:")
        
        y -= 4 * mm
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        c.drawString(margem, y, f"{dados_seguros['peso']} kg")
        
        # Modalidade
        y -= 8 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "MODALIDADE:")
        
        y -= 4 * mm
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        c.drawString(margem, y, dados_seguros['modalidade'])
        
        # ===== VALORES =====
        y -= 9 * mm
        
        # Valor do Frete
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "FRETE:")
        
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(PRETO)
        c.drawString(margem + 50 * mm, y, f"R$ {dados_seguros['frete']:.2f}")
        
        # Seguro (sempre aparece)
        y -= 8 * mm
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "SEGURO:")
        
        c.setFont("Helvetica", 9)
        c.setFillColor(PRETO)
        c.drawString(margem + 50 * mm, y, f"R$ {dados_seguros['seguro']:.2f}")
        
        # TOTAL
        y -= 12 * mm
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "TOTAL:")
        
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(VERMELHO_JADLOG)
        c.drawString(margem + 50 * mm, y, f"R$ {dados_seguros['total']:.2f}")
        
        # Linha final
        y -= 6 * mm
        c.setStrokeColor(VERMELHO_JADLOG)
        c.setLineWidth(0.5)
        c.line(margem, y, largura - margem, y)
        
        # ===== MENSAGEM PROMOCIONAL =====
        y -= 9 * mm
        c.setFont("Helvetica", 6)
        c.setFillColor(VERMELHO_JADLOG)
        c.drawString(margem, y, "VALORES EXCLUSIVOS DA AV. VAUTIER, 455 (BRÁS)")
        
        y -= 4 * mm
        c.setFont("Helvetica", 5)
        c.setFillColor(CINZA)
        c.drawString(margem, y, "Válidos até Dezembro/2026")
        
        # ===== RODAPÉ =====
        y -= 6 * mm
        c.setFont("Helvetica", 5)
        c.setFillColor(CINZA)
        data = datetime.now().strftime('%d/%m/%Y %H:%M')
        c.drawString(margem, y, f"Emissão: {data}")
        
        # ===== SALVAR PDF =====
        c.save()
        
        pdf_bytes = buffer.getvalue()
        buffer.close()
        
        return pdf_bytes