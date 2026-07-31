# ==================== TABELA DE PREÇOS ====================
class TabelaPrecos:
    def __init__(self):
        # ===== PREÇOS FINAIS POR PESO (CAPITAIS) =====
        # Estes são os valores FINAIS (GLM + Lucro) da planilha
        self.precos_finais_capital = {
            1: 24.99,
            5: 49.99,
            10: 79.99,
            20: 149.99,
            30: 229.99,
            40: 130.00,   # Atenção: valores > 30kg são diferentes
            50: 140.00,
            60: 150.00,
            70: 160.00,
            80: 180.00,
            90: 190.00,
            100: 200.00
        }
        
        # ===== LUCROS POR TIPO DE TARIFA =====
        self.lucros = {
            "CAPITAL 1": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "CAPITAL 2": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "CAPITAL 3": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "INTERIOR 1": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "INTERIOR 2": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            },
            "INTERIOR 3": {
                1: 10.23, 5: 15.74, 10: 27.04, 20: 46.10, 30: 75.24,
                40: 130.00, 50: 140.00, 60: 150.00, 70: 160.00,
                80: 180.00, 90: 190.00, 100: 200.00
            }
        }
        
        # ===== GLM POR UF (CAPITAL) =====
        self.glm_capital = {
            "AC": {1: 14.76, 5: 34.25, 10: 52.95, 20: 103.89, 30: 154.75},
            "AL": {1: 12.97, 5: 26.10, 10: 36.22, 20: 66.71, 30: 96.70},
            "AP": {1: 19.65, 5: 33.88, 10: 52.58, 20: 103.53, 30: 154.39},
            "AM": {1: 20.01, 5: 34.25, 10: 52.95, 20: 103.89, 30: 154.75},
            "BA": {1: 12.60, 5: 18.87, 10: 35.85, 20: 66.34, 30: 96.33},
            "CE": {1: 14.40, 5: 30.67, 10: 61.11, 20: 122.47, 30: 183.94},
            "DF": {1: 11.08, 5: 14.95, 10: 22.17, 20: 48.15, 30: 68.77},
            "ES": {1: 11.08, 5: 14.95, 10: 22.17, 20: 48.15, 30: 68.77},
            "GO": {1: 11.08, 5: 14.95, 10: 24.70, 20: 48.15, 30: 68.77},
            "MA": {1: 12.72, 5: 26.48, 10: 37.43, 20: 69.84, 30: 101.83},
            "MT": {1: 12.25, 5: 19.30, 10: 32.08, 20: 69.10, 30: 104.52},
            "MS": {1: 13.09, 5: 19.25, 10: 27.83, 20: 49.86, 30: 78.19},
            "MG": {1: 12.77, 5: 14.91, 10: 21.38, 20: 38.80, 30: 52.81},
            "PA": {1: 12.72, 5: 26.48, 10: 37.43, 20: 69.84, 30: 101.83},
            "PB": {1: 13.58, 5: 26.54, 10: 48.48, 20: 94.41, 30: 140.15},
            "PR": {1: 11.25, 5: 13.39, 10: 19.85, 20: 37.27, 30: 51.28},
            "PE": {1: 14.54, 5: 30.23, 10: 43.62, 20: 81.81, 30: 119.65},
            "PI": {1: 13.09, 5: 26.85, 10: 37.80, 20: 70.20, 30: 102.19},
            "RJ": {1: 11.25, 5: 13.39, 10: 19.85, 20: 37.27, 30: 51.28},
            "RN": {1: 13.58, 5: 26.06, 10: 52.58, 20: 103.53, 30: 154.39},
            "RS": {1: 11.70, 5: 15.80, 10: 23.43, 20: 50.89, 30: 72.68},
            "RO": {1: 16.92, 5: 39.45, 10: 61.05, 20: 119.91, 30: 178.62},
            "RR": {1: 19.65, 5: 33.88, 10: 52.58, 20: 103.53, 30: 154.39},
            "SC": {1: 11.25, 5: 13.39, 10: 19.85, 20: 37.27, 30: 51.28},
            "SP": {1: 12.66, 5: 14.31, 10: 18.84, 20: 32.88, 30: 37.56},
            "SE": {1: 12.60, 5: 25.73, 10: 35.85, 20: 66.34, 30: 96.33},
            "TO": {1: 12.72, 5: 26.48, 10: 37.43, 20: 69.84, 30: 101.83}
        }
        
        # ===== KG ADICIONAL PARA PESOS > 30KG (CAPITAL) =====
        self.kg_adicional_capital = {
            "AC": 4.24, "AL": 2.48, "AP": 4.24, "AM": 4.24,
            "BA": 2.02, "CE": 3.99, "DF": 1.68, "ES": 1.68,
            "GO": 1.68, "MA": 2.67, "MT": 2.74, "MS": 2.22,
            "MG": 1.08, "PA": 2.67, "PB": 3.81, "PR": 1.08,
            "PE": 3.14, "PI": 2.67, "RJ": 6.96,
            "RN": 4.24, "RS": 1.68, "RO": 4.24, "RR": 4.24,
            "SC": 1.08, "SP": 5.80, "SE": 2.48, "TO": 2.67
        }
        
        # ===== TABELA GLM PARA INTERIOR =====
        # (mantida da planilha anterior)
        self.glm_interior = {
            "AC": {
                "INTERIOR 1": {1: 88.14, 5: 90.78, 10: 98.97, 20: 130.12, 30: 154.99},
                "INTERIOR 2": {1: 109.10, 5: 111.80, 10: 121.91, 20: 160.23, 30: 190.73},
                "INTERIOR 3": {1: 166.55, 5: 170.67, 10: 186.08, 20: 244.52, 30: 290.97}
            },
            # ... (manter todos os outros estados da planilha anterior)
        }
        
        # ===== KG ADICIONAL PARA INTERIOR =====
        self.kg_adicional_interior = {
            "AC": {"INTERIOR 1": 29.57, "INTERIOR 2": 39.33, "INTERIOR 3": 59.89},
            # ... (manter todos os outros estados da planilha anterior)
        }
        
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
    
    def _interpolar_valor(self, tabela, peso, pesos_disponiveis, kg_adicional=None):
        """
        Interpola linearmente o valor para um peso específico.
        """
        if peso <= pesos_disponiveis[0]:
            return tabela[pesos_disponiveis[0]]
        
        if peso >= pesos_disponiveis[-1]:
            if kg_adicional is not None:
                valor_base = tabela[pesos_disponiveis[-1]]
                return round(valor_base + (peso - pesos_disponiveis[-1]) * kg_adicional, 2)
            return tabela[pesos_disponiveis[-1]]
        
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
    
    def _buscar_glm(self, uf, tipo_tarifa, peso):
        """
        Busca o valor GLM para o UF e peso
        """
        if tipo_tarifa.startswith("CAPITAL"):
            if uf in self.glm_capital:
                tabela = self.glm_capital[uf]
                pesos_disponiveis = sorted(tabela.keys())
                kg_adicional = self.kg_adicional_capital.get(uf, 5.00)
                return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            return None
        
        elif tipo_tarifa.startswith("INTERIOR"):
            if uf in self.glm_interior and tipo_tarifa in self.glm_interior[uf]:
                tabela = self.glm_interior[uf][tipo_tarifa]
                pesos_disponiveis = sorted(tabela.keys())
                
                kg_adicional = None
                if uf in self.kg_adicional_interior and tipo_tarifa in self.kg_adicional_interior[uf]:
                    kg_adicional = self.kg_adicional_interior[uf][tipo_tarifa]
                
                return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            return None
        
        return None
    
    def _buscar_lucro(self, tipo_tarifa, peso):
        """
        Busca o lucro para o tipo de tarifa e peso
        """
        if tipo_tarifa in self.lucros:
            tabela = self.lucros[tipo_tarifa]
            pesos_disponiveis = sorted(tabela.keys())
            return self._interpolar_valor(tabela, peso, pesos_disponiveis)
        return None
    
    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Calcula o frete: GLM + Lucro
        """
        # 1. Busca o GLM
        glm = self._buscar_glm(uf, tipo_tarifa, peso)
        if glm is None:
            return None
        
        # 2. Busca o Lucro
        lucro = self._buscar_lucro(tipo_tarifa, peso)
        if lucro is None:
            return None
        
        # 3. Frete = GLM + Lucro
        return round(glm + lucro, 2)