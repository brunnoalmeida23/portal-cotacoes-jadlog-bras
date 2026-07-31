# ==================== TABELA DE PREÇOS ====================
class TabelaPrecos:
    def __init__(self):
        # 1. PREÇOS DO FLYER (CAPITAIS)
        self.precos_capital = {
            1: 24.99,
            5: 49.99,
            10: 79.99,
            20: 149.99,
            30: 229.99
        }
        
        # 2. TABELA INTERIOR (preços de venda)
        self.tabela_interior = {
            "INTERIOR 1": {
                1: 13.00, 5: 26.00, 10: 44.00, 20: 80.00, 30: 126.00,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "INTERIOR 2": {
                1: 13.00, 5: 26.00, 10: 44.00, 20: 80.00, 30: 126.00,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "INTERIOR 3": {
                1: 26.00, 5: 52.00, 10: 88.00, 20: 160.00, 30: 252.00,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            }
        }
        
        # 3. MAPEAMENTO UF -> TIPO (para identificar capital/interior)
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
        
        # 4. CUSTO GLM POR UF (mantido em segredo - não aparece no frontend)
        self.custo_glm = {
            "AC": 14.76, "AL": 12.97, "AP": 19.65, "AM": 20.01,
            "BA": 12.60, "CE": 14.40, "DF": 11.08, "ES": 11.08,
            "GO": 11.08, "MA": 12.72, "MT": 12.25, "MS": 13.09,
            "MG": 12.77, "PA": 12.72, "PB": 13.58, "PR": 11.25,
            "PE": 14.54, "PI": 13.09, "RJ": 11.25, "RN": 13.58,
            "RS": 11.70, "RO": 16.92, "RR": 19.65, "SC": 11.25,
            "SP": 12.66, "SE": 12.60, "TO": 12.72
        }
    
    def buscar_tipo_por_uf(self, uf):
        """Retorna o tipo (INTERIOR 1, INTERIOR 2, INTERIOR 3) baseado na UF"""
        return self.tipo_por_uf.get(uf, "INTERIOR 1")
    
    def calcular_frete(self, uf, tipo_tarifa, peso):
        """
        Calcula o frete com interpolação linear para valores exatos
        
        Args:
            uf: Estado (ex: "SP", "AC")
            tipo_tarifa: "CAPITAL 1", "INTERIOR 1", "INTERIOR 2", "INTERIOR 3"
            peso: Peso em kg
        """
        
        # ===== CAPITAL =====
        if tipo_tarifa.startswith("CAPITAL"):
            # Busca o preço do flyer pela faixa de peso
            for peso_limite in sorted(self.precos_capital.keys()):
                if peso <= peso_limite:
                    return round(self.precos_capital[peso_limite], 2)
            
            # Peso > 30kg - interpolação com base no valor de 30kg
            if peso > 30:
                valor_base = self.precos_capital[30]  # 229.99
                # Usa o mesmo adicional de 5.00 por kg (ajustar conforme necessidade)
                adicional = 5.00
                return round(valor_base + (peso - 30) * adicional, 2)
        
        # ===== INTERIOR =====
        elif tipo_tarifa.startswith("INTERIOR"):
            if tipo_tarifa in self.tabela_interior:
                tabela = self.tabela_interior[tipo_tarifa]
                
                # Pesos disponíveis na tabela (ordenados)
                pesos = sorted(tabela.keys())
                
                # Se o peso é menor que o menor peso da tabela
                if peso <= pesos[0]:
                    return round(tabela[pesos[0]], 2)
                
                # Se o peso é maior que o maior peso da tabela (100kg)
                if peso >= pesos[-1]:
                    return round(tabela[pesos[-1]], 2)
                
                # INTERPOLAÇÃO LINEAR
                for i in range(len(pesos) - 1):
                    if pesos[i] <= peso <= pesos[i + 1]:
                        peso_baixo = pesos[i]
                        peso_alto = pesos[i + 1]
                        valor_baixo = tabela[peso_baixo]
                        valor_alto = tabela[peso_alto]
                        
                        # Interpolação linear
                        proporcao = (peso - peso_baixo) / (peso_alto - peso_baixo)
                        valor = valor_baixo + (valor_alto - valor_baixo) * proporcao
                        
                        # Retorna o valor com 2 casas decimais (sem arredondar para cima)
                        return round(valor, 2)
            
            return None
        
        return None
    
    def calcular_lucro(self, uf, tipo_tarifa, peso):
        """Calcula o lucro do cliente (NÃO MOSTRAR NO FRONTEND)"""
        
        frete = self.calcular_frete(uf, tipo_tarifa, peso)
        if not frete:
            return None
        
        if tipo_tarifa.startswith("CAPITAL"):
            if uf in self.custo_glm:
                custo = self.custo_glm[uf]
                lucro = frete - custo
                return round(lucro, 2)
        
        return None