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
        
        # 2. TABELA DE LUCROS POR PESO (para INTERIOR)
        # Estes são os lucros que o cliente quer ganhar em cima do GLM
        self.lucros_interior = {
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
        
        # 4. CUSTO GLM POR UF (para CAPITAL)
        self.custo_glm_capital = {
            "AC": 14.76, "AL": 12.97, "AP": 19.65, "AM": 20.01,
            "BA": 12.60, "CE": 14.40, "DF": 11.08, "ES": 11.08,
            "GO": 11.08, "MA": 12.72, "MT": 12.25, "MS": 13.09,
            "MG": 12.77, "PA": 12.72, "PB": 13.58, "PR": 11.25,
            "PE": 14.54, "PI": 13.09, "RJ": 11.25, "RN": 13.58,
            "RS": 11.70, "RO": 16.92, "RR": 19.65, "SC": 11.25,
            "SP": 12.66, "SE": 12.60, "TO": 12.72
        }
        
        # 5. TABELA GLM COMPLETA POR UF E TIPO (para INTERIOR)
        # Valores extraídos da planilha GLM Pack e .Com LIEV.xlsx
        # CORRIGIDO: Agora os valores de 30kg estão corretos para INTERIOR
        self.glm_interior = {
            "AC": {
                "INTERIOR 1": {1: 88.14, 5: 90.78, 10: 98.97, 20: 130.12, 30: 154.99},
                "INTERIOR 2": {1: 109.10, 5: 111.80, 10: 121.91, 20: 160.23, 30: 190.73},
                "INTERIOR 3": {1: 166.55, 5: 170.67, 10: 186.08, 20: 244.52, 30: 290.97}
            },
            "AL": {
                "INTERIOR 1": {1: 73.73, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.56, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.46, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "AP": {
                "INTERIOR 1": {1: 76.35, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 94.02, 5: 94.02, 10: 103.09, 20: 136.95, 30: 161.24},
                "INTERIOR 3": {1: 143.54, 5: 143.54, 10: 157.37, 20: 209.02, 30: 246.01}
            },
            "AM": {
                "INTERIOR 1": {1: 76.35, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 94.02, 5: 94.02, 10: 103.09, 20: 136.95, 30: 161.24},
                "INTERIOR 3": {1: 143.54, 5: 143.54, 10: 157.37, 20: 209.02, 30: 246.01}
            },
            "BA": {
                "INTERIOR 1": {1: 31.18, 5: 33.81, 10: 39.78, 20: 61.78, 30: 74.33},
                "INTERIOR 2": {1: 38.92, 5: 41.62, 10: 48.97, 20: 76.04, 30: 91.46},
                "INTERIOR 3": {1: 59.45, 5: 63.55, 10: 74.78, 20: 116.07, 30: 139.59}
            },
            "CE": {
                "INTERIOR 1": {1: 53.21, 5: 55.84, 10: 62.36, 20: 86.55, 30: 101.85},
                "INTERIOR 2": {1: 66.06, 5: 68.76, 10: 76.79, 20: 106.55, 30: 125.33},
                "INTERIOR 3": {1: 100.86, 5: 104.97, 10: 117.24, 20: 162.61, 30: 191.23}
            },
            "DF": {
                "INTERIOR 1": {1: 23.38, 5: 25.76, 10: 30.87, 20: 49.65, 30: 59.44},
                "INTERIOR 2": {1: 29.27, 5: 31.71, 10: 38.04, 20: 61.21, 30: 73.25},
                "INTERIOR 3": {1: 44.65, 5: 48.40, 10: 58.07, 20: 93.48, 30: 111.86}
            },
            "ES": {
                "INTERIOR 1": {1: 23.38, 5: 25.76, 10: 30.87, 20: 49.65, 30: 59.44},
                "INTERIOR 2": {1: 31.90, 5: 34.35, 10: 41.22, 20: 66.31, 30: 79.35},
                "INTERIOR 3": {1: 38.94, 5: 41.95, 10: 50.33, 20: 81.02, 30: 96.92}
            },
            "GO": {
                "INTERIOR 1": {1: 23.38, 5: 25.76, 10: 30.87, 20: 49.65, 30: 59.44},
                "INTERIOR 2": {1: 29.27, 5: 31.71, 10: 38.04, 20: 61.21, 30: 73.25},
                "INTERIOR 3": {1: 44.65, 5: 48.40, 10: 58.07, 20: 93.48, 30: 111.86}
            },
            "MA": {
                "INTERIOR 1": {1: 73.74, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.57, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.48, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "MT": {
                "INTERIOR 1": {1: 28.63, 5: 31.01, 10: 36.46, 20: 56.58, 30: 68.20},
                "INTERIOR 2": {1: 35.75, 5: 38.22, 10: 44.93, 20: 69.75, 30: 84.05},
                "INTERIOR 3": {1: 54.59, 5: 58.34, 10: 68.61, 20: 106.54, 30: 128.36}
            },
            "MS": {
                "INTERIOR 1": {1: 23.38, 5: 25.76, 10: 30.87, 20: 49.65, 30: 59.44},
                "INTERIOR 2": {1: 29.27, 5: 31.71, 10: 38.04, 20: 61.21, 30: 73.25},
                "INTERIOR 3": {1: 44.65, 5: 48.40, 10: 58.07, 20: 93.48, 30: 111.86}
            },
            "MG": {
                "INTERIOR 1": {1: 21.95, 5: 24.35, 10: 29.21, 20: 47.03, 30: 56.28},
                "INTERIOR 2": {1: 30.01, 5: 32.47, 10: 38.97, 20: 62.80, 30: 75.15},
                "INTERIOR 3": {1: 36.63, 5: 39.64, 10: 47.59, 20: 76.72, 30: 91.77}
            },
            "PA": {
                "INTERIOR 1": {1: 53.23, 5: 55.84, 10: 62.36, 20: 86.55, 30: 101.85},
                "INTERIOR 2": {1: 66.08, 5: 68.76, 10: 76.79, 20: 106.55, 30: 125.33},
                "INTERIOR 3": {1: 100.87, 5: 104.97, 10: 117.24, 20: 162.61, 30: 191.23}
            },
            "PB": {
                "INTERIOR 1": {1: 73.73, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.56, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.46, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "PE": {
                "INTERIOR 1": {1: 53.21, 5: 55.84, 10: 62.36, 20: 86.55, 30: 101.85},
                "INTERIOR 2": {1: 66.06, 5: 68.76, 10: 76.79, 20: 106.55, 30: 125.33},
                "INTERIOR 3": {1: 100.86, 5: 104.97, 10: 117.24, 20: 162.61, 30: 191.23}
            },
            "PI": {
                "INTERIOR 1": {1: 73.74, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.57, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.48, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "PR": {
                "INTERIOR 1": {1: 21.95, 5: 24.35, 10: 29.21, 20: 47.03, 30: 56.28},
                "INTERIOR 2": {1: 30.01, 5: 32.47, 10: 38.97, 20: 62.80, 30: 75.15},
                "INTERIOR 3": {1: 36.63, 5: 39.64, 10: 47.59, 20: 76.72, 30: 91.77}
            },
            "RJ": {
                "INTERIOR 1": {1: 21.95, 5: 24.35, 10: 29.21, 20: 47.03, 30: 56.28},
                "INTERIOR 2": {1: 30.01, 5: 32.47, 10: 38.97, 20: 62.80, 30: 75.15},
                "INTERIOR 3": {1: 36.63, 5: 39.64, 10: 47.59, 20: 76.72, 30: 91.77}
            },
            "RN": {
                "INTERIOR 1": {1: 73.73, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.56, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.46, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "RO": {
                "INTERIOR 1": {1: 73.73, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 91.34, 5: 94.02, 10: 103.09, 20: 136.95, 30: 161.24},
                "INTERIOR 3": {1: 139.43, 5: 143.54, 10: 157.37, 20: 209.02, 30: 246.01}
            },
            "RR": {
                "INTERIOR 1": {1: 90.78, 5: 90.78, 10: 98.97, 20: 130.12, 30: 154.99},
                "INTERIOR 2": {1: 111.80, 5: 111.80, 10: 121.91, 20: 160.23, 30: 190.73},
                "INTERIOR 3": {1: 170.67, 5: 170.67, 10: 186.08, 20: 244.52, 30: 290.97}
            },
            "RS": {
                "INTERIOR 1": {1: 21.96, 5: 24.35, 10: 29.21, 20: 47.03, 30: 56.28},
                "INTERIOR 2": {1: 30.02, 5: 32.47, 10: 38.97, 20: 62.80, 30: 75.15},
                "INTERIOR 3": {1: 36.64, 5: 39.64, 10: 47.59, 20: 76.72, 30: 91.77}
            },
            "SC": {
                "INTERIOR 1": {1: 21.95, 5: 24.35, 10: 29.21, 20: 47.03, 30: 56.28},
                "INTERIOR 2": {1: 30.01, 5: 32.47, 10: 38.97, 20: 62.80, 30: 75.15},
                "INTERIOR 3": {1: 36.63, 5: 39.64, 10: 47.59, 20: 76.72, 30: 91.77}
            },
            "SP": {
                "INTERIOR 1": {1: 16.12, 5: 16.12, 10: 17.19, 20: 24.39, 30: 152.59},
                "INTERIOR 2": {1: 21.45, 5: 21.45, 10: 22.90, 20: 32.52, 30: 152.59},
                "INTERIOR 3": {1: 26.16, 5: 26.16, 10: 27.94, 20: 39.71, 30: 152.59}
            },
            "SE": {
                "INTERIOR 1": {1: 73.73, 5: 76.35, 10: 83.72, 20: 111.22, 30: 131.03},
                "INTERIOR 2": {1: 79.56, 5: 82.26, 10: 90.19, 20: 119.81, 30: 141.05},
                "INTERIOR 3": {1: 121.46, 5: 125.57, 10: 137.67, 20: 182.84, 30: 215.23}
            },
            "TO": {
                "INTERIOR 1": {1: 53.23, 5: 55.84, 10: 62.36, 20: 86.55, 30: 101.85},
                "INTERIOR 2": {1: 66.08, 5: 68.76, 10: 76.79, 20: 106.55, 30: 125.33},
                "INTERIOR 3": {1: 100.87, 5: 104.97, 10: 117.24, 20: 162.61, 30: 191.23}
            }
        }
        
        # 6. TABELA GLM COMPLETA PARA CAPITAL (valores por peso)
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
        
        # 7. KG ADICIONAL PARA INTERIOR (acima de 30kg)
        self.kg_adicional_interior = {
            "AC": {"INTERIOR 1": 29.57, "INTERIOR 2": 39.33, "INTERIOR 3": 59.89},
            "AL": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "AP": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "AM": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "BA": {"INTERIOR 1": 15.82, "INTERIOR 2": 21.04, "INTERIOR 3": 32.03},
            "CE": {"INTERIOR 1": 20.24, "INTERIOR 2": 26.92, "INTERIOR 3": 40.99},
            "DF": {"INTERIOR 1": 12.98, "INTERIOR 2": 17.30, "INTERIOR 3": 26.38},
            "ES": {"INTERIOR 1": 12.98, "INTERIOR 2": 15.97, "INTERIOR 3": 19.47},
            "GO": {"INTERIOR 1": 12.98, "INTERIOR 2": 17.30, "INTERIOR 3": 26.38},
            "MA": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "MT": {"INTERIOR 1": 14.60, "INTERIOR 2": 19.46, "INTERIOR 3": 29.67},
            "MS": {"INTERIOR 1": 12.98, "INTERIOR 2": 17.30, "INTERIOR 3": 26.38},
            "MG": {"INTERIOR 1": 12.38, "INTERIOR 2": 15.22, "INTERIOR 3": 18.57},
            "PA": {"INTERIOR 1": 20.24, "INTERIOR 2": 26.92, "INTERIOR 3": 40.99},
            "PB": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "PE": {"INTERIOR 1": 20.24, "INTERIOR 2": 26.92, "INTERIOR 3": 40.99},
            "PI": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "PR": {"INTERIOR 1": 12.38, "INTERIOR 2": 15.22, "INTERIOR 3": 18.57},
            "RJ": {"INTERIOR 1": 12.38, "INTERIOR 2": 15.22, "INTERIOR 3": 18.57},
            "RN": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "RO": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "RR": {"INTERIOR 1": 29.57, "INTERIOR 2": 39.33, "INTERIOR 3": 59.89},
            "RS": {"INTERIOR 1": 12.38, "INTERIOR 2": 15.22, "INTERIOR 3": 18.57},
            "SC": {"INTERIOR 1": 12.38, "INTERIOR 2": 15.22, "INTERIOR 3": 18.57},
            "SP": {"INTERIOR 1": 6.96, "INTERIOR 2": 7.73, "INTERIOR 3": 8.76},
            "SE": {"INTERIOR 1": 25.24, "INTERIOR 2": 33.58, "INTERIOR 3": 51.13},
            "TO": {"INTERIOR 1": 20.24, "INTERIOR 2": 26.92, "INTERIOR 3": 40.99}
        }
    
    def buscar_tipo_por_uf(self, uf):
        """Retorna o tipo (INTERIOR 1, INTERIOR 2, INTERIOR 3) baseado na UF"""
        return self.tipo_por_uf.get(uf, "INTERIOR 1")
    
    def _interpolar_valor(self, tabela, peso, pesos_disponiveis, kg_adicional=None):
        """
        Interpola linearmente o valor para um peso específico.
        Se o peso for maior que 30kg, usa o kg_adicional para extrapolar.
        """
        # Se o peso é menor que o menor peso da tabela
        if peso <= pesos_disponiveis[0]:
            return tabela[pesos_disponiveis[0]]
        
        # Se o peso é maior que o maior peso da tabela (30kg)
        if peso >= pesos_disponiveis[-1]:
            if kg_adicional is not None:
                # Extrapolação com kg adicional
                valor_base = tabela[pesos_disponiveis[-1]]
                return round(valor_base + (peso - pesos_disponiveis[-1]) * kg_adicional, 2)
            return tabela[pesos_disponiveis[-1]]
        
        # Interpolação linear para pesos entre os disponíveis
        for i in range(len(pesos_disponiveis) - 1):
            if pesos_disponiveis[i] <= peso <= pesos_disponiveis[i + 1]:
                peso_baixo = pesos_disponiveis[i]
                peso_alto = pesos_disponiveis[i + 1]
                valor_baixo = tabela[peso_baixo]
                valor_alto = tabela[peso_alto]
                
                # Interpolação linear
                proporcao = (peso - peso_baixo) / (peso_alto - peso_baixo)
                valor = valor_baixo + (valor_alto - valor_baixo) * proporcao
                
                return round(valor, 2)
        
        return None
    
    def _interpolar_lucro(self, uf, tipo_tarifa, peso):
        """
        Interpola o lucro para um peso específico
        """
        if tipo_tarifa.startswith("CAPITAL"):
            # Lucro = Preço do flyer - GLM
            frete = self.calcular_frete(uf, tipo_tarifa, peso)
            if frete is None:
                return None
            
            if uf in self.custo_glm_capital:
                custo = self.custo_glm_capital[uf]
                lucro = frete - custo
                return round(lucro, 2)
            
            return None
        
        elif tipo_tarifa.startswith("INTERIOR"):
            if tipo_tarifa in self.lucros_interior:
                tabela_lucro = self.lucros_interior[tipo_tarifa]
                pesos_disponiveis = sorted(tabela_lucro.keys())
                return self._interpolar_valor(tabela_lucro, peso, pesos_disponiveis)
            
            return None
        
        return None
    
    def _buscar_glm(self, uf, tipo_tarifa, peso):
        """
        Busca o valor GLM para o UF, tipo de tarifa e peso,
        usando kg_adicional para pesos > 30kg.
        """
        if tipo_tarifa.startswith("CAPITAL"):
            if uf in self.glm_capital:
                tabela = self.glm_capital[uf]
                pesos_disponiveis = sorted(tabela.keys())
                return self._interpolar_valor(tabela, peso, pesos_disponiveis)
            return None
        
        elif tipo_tarifa.startswith("INTERIOR"):
            if uf in self.glm_interior and tipo_tarifa in self.glm_interior[uf]:
                tabela = self.glm_interior[uf][tipo_tarifa]
                pesos_disponiveis = sorted(tabela.keys())
                
                # Busca o kg_adicional para extrapolação acima de 30kg
                kg_adicional = None
                if uf in self.kg_adicional_interior and tipo_tarifa in self.kg_adicional_interior[uf]:
                    kg_adicional = self.kg_adicional_interior[uf][tipo_tarifa]
                
                return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            return None
        
        return None
    
    def calcular_frete(self, uf, tipo_tarifa, peso):
        """
        Calcula o frete usando GLM + Lucro
        
        Args:
            uf: Estado (ex: "SP", "AC")
            tipo_tarifa: "CAPITAL 1", "INTERIOR 1", "INTERIOR 2", "INTERIOR 3"
            peso: Peso em kg
        """
        
        # ===== CAPITAL =====
        if tipo_tarifa.startswith("CAPITAL"):
            # 1. Busca o GLM para o UF
            glm = self._buscar_glm(uf, tipo_tarifa, peso)
            if glm is None:
                return None
            
            # 2. Busca o preço do flyer
            frete_flyer = None
            for peso_limite in sorted(self.precos_capital.keys()):
                if peso <= peso_limite:
                    frete_flyer = self.precos_capital[peso_limite]
                    break
            
            if peso > 30:
                frete_flyer = self.precos_capital[30] + (peso - 30) * 5.00
            
            if frete_flyer is None:
                return None
            
            # 3. Calcula o lucro (preço do flyer - GLM)
            lucro = round(frete_flyer - glm, 2)
            
            # 4. Frete final = GLM + Lucro
            return round(glm + lucro, 2)
        
        # ===== INTERIOR =====
        elif tipo_tarifa.startswith("INTERIOR"):
            # 1. Busca o GLM para o UF e tipo de tarifa
            glm = self._buscar_glm(uf, tipo_tarifa, peso)
            if glm is None:
                return None
            
            # 2. Busca o lucro para o UF e tipo de tarifa
            lucro = self._interpolar_lucro(uf, tipo_tarifa, peso)
            if lucro is None:
                return None
            
            # 3. Frete final = GLM + Lucro
            return round(glm + lucro, 2)
        
        return None
    
    def calcular_lucro(self, uf, tipo_tarifa, peso):
        """Calcula o lucro do cliente (NÃO MOSTRAR NO FRONTEND)"""
        
        frete = self.calcular_frete(uf, tipo_tarifa, peso)
        if frete is None:
            return None
        
        if tipo_tarifa.startswith("CAPITAL"):
            if uf in self.custo_glm_capital:
                custo = self.custo_glm_capital[uf]
                lucro = frete - custo
                return round(lucro, 2)
        
        elif tipo_tarifa.startswith("INTERIOR"):
            if uf in self.glm_interior and tipo_tarifa in self.glm_interior[uf]:
                custo = self._buscar_glm(uf, tipo_tarifa, peso)
                if custo is not None:
                    lucro = frete - custo
                    return round(lucro, 2)
        
        return None