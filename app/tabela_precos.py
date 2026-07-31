# ==================== TABELA DE PREÇOS ====================
class TabelaPrecos:
    def __init__(self):
        # ===== SUBTOTAIS (GLM + COMISSÃO) POR PESO =====
        # Colunas E, G, I, K, M, O, Q, S, U, W, Y, AA da planilha "Preços CLIENTE SIMULADOR"
        # Estes valores já são GLM + Comissão
        self.subtotais_capital = {
            "AC": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 256.02, 50: 303.53, 60: 351.03, 
                70: 398.55, 80: 446.05, 90: 493.56, 100: 541.06
            },
            "AL": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 178.31, 50: 206.16, 60: 234.02, 
                70: 261.87, 80: 289.72, 90: 317.58, 100: 345.43
            },
            "AP": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 255.66, 50: 303.16, 60: 350.67, 
                70: 398.18, 80: 445.69, 90: 493.19, 100: 540.70
            },
            "AM": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 256.02, 50: 303.53, 60: 351.03, 
                70: 398.55, 80: 446.05, 90: 493.56, 100: 541.06
            },
            "BA": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 172.89, 50: 195.69, 60: 218.49, 
                70: 241.29, 80: 264.09, 90: 286.89, 100: 309.69
            },
            "CE": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 282.51, 50: 327.32, 60: 372.13, 
                70: 416.95, 80: 461.75, 90: 506.57, 100: 551.38
            },
            "DF": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 141.62, 50: 160.72, 60: 179.82, 
                70: 198.90, 80: 218.00, 90: 237.09, 100: 256.18
            },
            "ES": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 141.62, 50: 160.72, 60: 179.82, 
                70: 198.90, 80: 218.00, 90: 237.09, 100: 256.18
            },
            "GO": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 141.62, 50: 160.72, 60: 179.82, 
                70: 198.90, 80: 218.00, 90: 237.09, 100: 256.18
            },
            "MA": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 185.57, 50: 215.56, 60: 245.55, 
                70: 275.54, 80: 305.52, 90: 335.51, 100: 365.49
            },
            "MT": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 189.05, 50: 219.83, 60: 250.59, 
                70: 281.37, 80: 312.14, 90: 342.91, 100: 373.69
            },
            "MS": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 156.89, 50: 181.83, 60: 206.76, 
                70: 231.69, 80: 256.62, 90: 281.56, 100: 306.49
            },
            "MG": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 122.57, 50: 135.50, 60: 148.44, 
                70: 161.38, 80: 174.32, 90: 187.25, 100: 200.19
            },
            "PA": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 185.57, 50: 215.56, 60: 245.55, 
                70: 275.54, 80: 305.52, 90: 335.51, 100: 365.49
            },
            "PB": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 236.71, 50: 279.49, 60: 322.29, 
                70: 365.08, 80: 407.87, 90: 450.66, 100: 493.45
            },
            "PR": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 121.05, 50: 133.98, 60: 146.92, 
                70: 159.85, 80: 172.80, 90: 185.73, 100: 198.67
            },
            "PE": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 208.57, 50: 243.72, 60: 278.87, 
                70: 314.02, 80: 349.18, 90: 384.33, 100: 419.48
            },
            "PI": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 185.94, 50: 215.92, 60: 245.91, 
                70: 275.90, 80: 305.88, 90: 335.87, 100: 365.86
            },
            "RJ": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 121.05, 50: 133.98, 60: 146.92, 
                70: 159.85, 80: 172.80, 90: 185.73, 100: 198.67
            },
            "RN": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 255.66, 50: 303.16, 60: 350.67, 
                70: 398.18, 80: 445.69, 90: 493.19, 100: 540.70
            },
            "RS": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 149.67, 50: 169.85, 60: 190.03, 
                70: 210.20, 80: 230.39, 90: 250.56, 100: 270.74
            },
            "RO": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 284.84, 50: 337.28, 60: 389.73, 
                70: 442.18, 80: 494.63, 90: 547.08, 100: 599.53
            },
            "RR": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 255.66, 50: 303.16, 60: 350.67, 
                70: 398.18, 80: 445.69, 90: 493.19, 100: 540.70
            },
            "SC": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 121.05, 50: 133.98, 60: 146.92, 
                70: 159.85, 80: 172.80, 90: 185.73, 100: 198.67
            },
            "SP": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 105.18, 50: 115.98, 60: 126.78, 
                70: 137.58, 80: 148.39, 90: 159.18, 100: 169.99
            },
            "SE": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 177.95, 50: 205.80, 60: 233.66, 
                70: 261.51, 80: 289.35, 90: 317.22, 100: 345.06
            },
            "TO": {
                1: 24.99, 5: 49.99, 10: 79.99, 20: 149.99, 
                30: 229.99, 40: 185.57, 50: 215.56, 60: 245.55, 
                70: 275.54, 80: 305.52, 90: 335.51, 100: 365.49
            }
        }
        
        # ===== KG ADICIONAL (para pesos > 30kg) =====
        self.kg_adicional = {
            "AC": 4.24, "AL": 2.48, "AP": 4.24, "AM": 4.24,
            "BA": 2.02, "CE": 3.99, "DF": 1.68, "ES": 1.68,
            "GO": 1.68, "MA": 2.67, "MT": 2.74, "MS": 2.22,
            "MG": 1.08, "PA": 2.67, "PB": 3.81, "PR": 1.08,
            "PE": 3.14, "PI": 2.67, "RJ": 6.96,
            "RN": 4.24, "RS": 1.68, "RO": 4.24, "RR": 4.24,
            "SC": 1.08, "SP": 5.80, "SE": 2.48, "TO": 2.67
        }
        
        # ===== ADVALOREM =====
        self.ADVALOREM_PERCENT = 0.0066  # 0,66%
        
        # ===== MAPEAMENTO UF -> TIPO =====
        self.tipo_por_uf = {
            "AC": "INTERIOR 1", "AL": "INTERIOR 1", "AP": "INTERIOR 1", 
            "AM": "INTERIOR 1", "BA": "INTERIOR 1", "CE": "INTERIOR 1",
            "DF": "INTERIOR 2", "ES": "INTERIOR 2", "GO": "INTERIOR 2",
            "MA": "INTERIOR 1", "MT": "INTERIOR 1", "MS": "INTERIOR 1",
            "MG": "INTERIOR 2", "PA": "INTERIOR 1", "PB": "INTERIOR 1",
            "PR": "INTERIOR 2", "PE": "INTERIOR 1", "PI": "INTERIOR 1",
            "RJ": "INTERIOR 2", "RN": "INTERIOR 1", "RS": "INTERIOR 2",
            "RO": "INTERIOR 1", "RR": "INTERIOR 1", "SC": "INTERIOR 2",
            "SP": "INTERIOR 2", "SE": "INTERIOR 1", "TO": "INTERIOR 1"
        }
    
    def buscar_tipo_por_uf(self, uf):
        return self.tipo_por_uf.get(uf, "INTERIOR 1")
    
    def _interpolar_subtotal(self, uf, peso):
        """
        Interpola o Subtotal (GLM + Comissão) para um peso específico
        """
        if uf not in self.subtotais_capital:
            return None
        
        tabela = self.subtotais_capital[uf]
        pesos_disponiveis = sorted(tabela.keys())
        
        # Se peso <= 1kg
        if peso <= pesos_disponiveis[0]:
            return tabela[pesos_disponiveis[0]]
        
        # Se peso >= 100kg
        if peso >= pesos_disponiveis[-1]:
            kg_adicional = self.kg_adicional.get(uf, 5.00)
            valor_base = tabela[pesos_disponiveis[-1]]
            return round(valor_base + (peso - pesos_disponiveis[-1]) * kg_adicional, 2)
        
        # Interpolação linear
        for i in range(len(pesos_disponiveis) - 1):
            if pesos_disponiveis[i] <= peso <= pesos_disponiveis[i + 1]:
                peso_baixo = pesos_disponiveis[i]
                peso_alto = pesos_disponiveis[i + 1]
                valor_baixo = tabela[peso_baixo]
                valor_alto = tabela[peso_alto]
                
                proporcao = (peso - peso_baixo) / (peso_alto - peso_baixo)
                valor = valor_baixo + (valor_alto - valor_baixo) * proporcao
                
                return round(valor, 2)
        
        return None
    
    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Calcula o frete: Subtotal + Advalorem
        Fórmula: = Subtotal + (Subtotal * 0.0066)
        """
        # 1. Busca o Subtotal (GLM + Comissão) interpolado
        subtotal = self._interpolar_subtotal(uf, peso)
        if subtotal is None:
            return None
        
        # 2. Advalorem (0,66% sobre o subtotal)
        advalorem = round(subtotal * self.ADVALOREM_PERCENT, 2)
        
        # 3. Total = Subtotal + Advalorem
        total = round(subtotal + advalorem, 2)
        
        return {
            'subtotal': round(subtotal, 2),
            'advalorem': advalorem,
            'total': total
        }
    
    def calcular_frete_total(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Retorna apenas o total (para compatibilidade com o código antigo)
        """
        resultado = self.calcular_frete(uf, tipo_tarifa, peso, modalidade)
        if resultado:
            return resultado['total']
        return None