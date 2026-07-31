# ==================== TABELA DE PREÇOS ====================
class TabelaPrecos:
    def __init__(self):
        # ===== PREÇOS FINAIS POR PESO (LUCROS) =====
        # Estes são os valores FINAIS (GLM + Lucro) da planilha "Preços CLIENTE SIMULADOR"
        self.precos_finais_capital = {
            1: 24.99,
            5: 49.99,
            10: 79.99,
            20: 149.99,
            30: 229.99,
            40: 130.00,
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
        
        # ===== GLM PACK (para modalidade .PACKAGE) =====
        # Valores extraídos da planilha GLM PACK.xlsx
        self.glm_pack_capital = {
            "AC": {1: 14.6932, 5: 32.038, 10: 48.6916, 20: 90.0664, 30: 122.693},
            "AL": {1: 13.0948, 5: 24.7804, 10: 33.7876, 20: 58.5952, 30: 77.8948},
            "AM": {1: 19.3588, 5: 32.038, 10: 48.6916, 20: 90.0664, 30: 122.693},
            "AP": {1: 19.3588, 5: 32.038, 10: 48.6916, 20: 90.0664, 30: 122.693},
            "BA": {1: 13.0948, 5: 18.6676, 10: 33.7876, 20: 58.5952, 30: 77.8948},
            "CE": {1: 14.6932, 5: 29.1652, 10: 56.2732, 20: 106.094, 30: 145.503},
            "DF": {1: 11.734, 5: 15.1792, 10: 21.6052, 20: 44.7496, 30: 56.4892},
            "ES": {1: 11.734, 5: 15.1792, 10: 21.6052, 20: 44.7496, 30: 56.4892},
            "GO": {1: 11.734, 5: 15.1792, 10: 23.8624, 20: 44.7496, 30: 56.4892},
            "MA": {1: 13.192, 5: 25.4608, 10: 35.2132, 20: 64.0492, 30: 82.1176},
            "MT": {1: 12.4468, 5: 18.7324, 10: 30.094, 20: 63.0772, 30: 83.8024},
            "MS": {1: 12.2416, 5: 17.7172, 10: 25.3528, 20: 44.9656, 30: 61.4788},
            "MG": {1: 11.356, 5: 13.1488, 10: 18.592, 20: 33.2692, 30: 40.8832},
            "PA": {1: 13.192, 5: 25.4608, 10: 35.2132, 20: 64.0492, 30: 82.1176},
            "PB": {1: 13.9588, 5: 25.4932, 10: 45.0412, 20: 85.93, 30: 111.688},
            "PR": {1: 11.356, 5: 13.1488, 10: 18.592, 20: 33.2692, 30: 40.8832},
            "PE": {1: 13.5268, 5: 27.502, 10: 39.4144, 20: 73.4236, 30: 94.7968},
            "PI": {1: 13.192, 5: 25.4608, 10: 35.2132, 20: 64.0492, 30: 82.1176},
            "RJ": {1: 11.356, 5: 13.1488, 10: 18.592, 20: 33.2692, 30: 40.8832},
            "RN": {1: 13.9588, 5: 25.0936, 10: 48.6916, 20: 94.0516, 30: 122.693},
            "RS": {1: 11.734, 5: 15.1792, 10: 21.6052, 20: 44.7496, 30: 56.4892},
            "RO": {1: 14.6932, 5: 32.038, 10: 48.6916, 20: 94.0516, 30: 122.693},
            "RR": {1: 19.3588, 5: 32.038, 10: 48.6916, 20: 90.0664, 30: 122.693},
            "SC": {1: 11.356, 5: 13.1488, 10: 18.592, 20: 33.2692, 30: 40.8832},
            "SP": {1: 11.248, 5: 12.6412, 10: 16.4644, 20: 28.2796, 30: 31.8544},
            "SE": {1: 13.0948, 5: 24.7804, 10: 33.7876, 20: 60.9388, 30: 80.3356},
            "TO": {1: 13.192, 5: 25.4608, 10: 35.2132, 20: 64.0492, 30: 82.1176}
        }
        
        # ===== GLM COM (para modalidade .COM) =====
        # Valores extraídos da planilha GLM .com.xlsx
        self.glm_com_capital = {
            "AC": {1: 16.6156, 5: 44.3392, 10: 81.3508, 20: 173.032, 30: 231.32},
            "AL": {1: 12.4144, 5: 25.3096, 10: 43.0432, 20: 85.1848, 30: 111.99},
            "AM": {1: 16.6156, 5: 44.3392, 10: 81.3508, 20: 173.032, 30: 231.32},
            "AP": {1: 16.6156, 5: 44.3392, 10: 81.3508, 20: 173.032, 30: 231.32},
            "BA": {1: 12.2848, 5: 24.6724, 10: 41.7472, 20: 82.2472, 30: 111.612},
            "CE": {1: 14.1424, 5: 34.4788, 10: 61.846, 20: 128.18, 30: 176.628},
            "DF": {1: 10.5676, 5: 19.9096, 10: 32.9776, 20: 63.412, 30: 85.822},
            "ES": {1: 10.4704, 5: 19.3696, 10: 31.8544, 20: 60.8848, 30: 82.2148},
            "GO": {1: 10.5676, 5: 19.9096, 10: 32.9776, 20: 63.412, 30: 85.822},
            "MA": {1: 12.5872, 5: 26.1736, 10: 44.728, 20: 85.8544, 30: 118.049},
            "MT": {1: 11.896, 5: 25.2556, 10: 43.5076, 20: 84.418, 30: 116.699},
            "MS": {1: 11.6908, 5: 24.1, 10: 41.1208, 20: 82.7116, 30: 112.887},
            "MG": {1: 9.9952, 5: 17.7712, 10: 28.7656, 20: 54.1564, 30: 72.754},
            "PA": {1: 13.6024, 5: 28.42, 10: 48.7132, 20: 97.7884, 30: 133.148},
            "PB": {1: 13.3648, 5: 30.3208, 10: 53.3572, 20: 108.761, 30: 149.132},
            "PR": {1: 9.9736, 5: 17.6956, 10: 28.6252, 20: 53.6704, 30: 72.0952},
            "PE": {1: 12.868, 5: 27.8152, 10: 48.184, 20: 96.9784, 30: 132.456},
            "PI": {1: 12.5872, 5: 26.1736, 10: 44.728, 20: 89.6884, 30: 122.078},
            "RJ": {1: 9.9952, 5: 17.7712, 10: 28.7656, 20: 54.1564, 30: 72.754},
            "RN": {1: 13.3648, 5: 30.3208, 10: 53.3572, 20: 108.761, 30: 149.132},
            "RS": {1: 10.1572, 5: 18.7324, 10: 30.7744, 20: 58.5304, 30: 79.0072},
            "RO": {1: 15.568, 5: 38.8096, 10: 70.0108, 20: 146.842, 30: 202.592},
            "RR": {1: 16.6156, 5: 44.3392, 10: 81.3508, 20: 173.032, 30: 231.32},
            "SC": {1: 10.0708, 5: 18.214, 10: 29.7052, 20: 56.1112, 30: 75.5404},
            "SP": {1: 8.4076, 5: 14.1316, 10: 22.3072, 20: 40.8724, 30: 54.5128},
            "SE": {1: 12.4144, 5: 25.3096, 10: 43.0432, 20: 85.1848, 30: 111.99},
            "TO": {1: 13.9912, 5: 30.5044, 10: 52.9684, 20: 107.606, 30: 147.026}
        }
        
        # ===== KG ADICIONAL (PACK) =====
        self.kg_adicional_pack_capital = {
            "AC": 4.2444, "AL": 2.484, "AM": 4.2444, "AP": 4.2444,
            "BA": 2.0196, "CE": 3.9852, "DF": 1.6848, "ES": 1.6848,
            "GO": 1.6848, "MA": 2.6676, "MT": 2.7432, "MS": 2.2248,
            "MG": 1.08, "PA": 2.6676, "PB": 3.8124, "PR": 1.08,
            "PE": 3.1428, "PI": 2.6676, "RJ": 1.08,
            "RN": 4.2444, "RS": 1.6848, "RO": 4.2444, "RR": 4.2444,
            "SC": 1.08, "SP": 0.9072, "SE": 2.484, "TO": 2.6676
        }
        
        # ===== KG ADICIONAL (COM) =====
        self.kg_adicional_com_capital = {
            "AC": 14.9904, "AL": 12.204, "AM": 15.8652, "AP": 12.7224,
            "BA": 11.016, "CE": 13.824, "DF": 8.0676, "ES": 7.7652,
            "GO": 7.8624, "MA": 13.4568, "MT": 9.396, "MS": 8.0676,
            "MG": 6.7608, "PA": 13.3596, "PB": 12.96, "PR": 6.7068,
            "PE": 12.7116, "PI": 13.0248, "RJ": 6.7608,
            "RN": 13.392, "RS": 8.2728, "RO": 13.6944, "RR": 15.9408,
            "SC": 7.3656, "SP": 5.7996, "SE": 11.5668, "TO": 10.5624
        }
        
        # ===== GLM PACK INTERIOR =====
        self.glm_pack_interior = {
            "AC": {"INTERIOR 1": {1: 90.7792, 5: 130.124, 10: 201.058, 20: 475.875, 30: 722.223}},
            "AL": {"INTERIOR 1": {1: 76.3504, 5: 111.224, 10: 171.585, 20: 406.118, 30: 616.35}},
            # ... (manter todos os estados da planilha GLM PACK)
        }
        
        # ===== GLM COM INTERIOR =====
        self.glm_com_interior = {
            "AC": {"INTERIOR 1": {1: 93.8032, 5: 138.494, 10: 213.078, 20: 575.872, 30: 827.382}},
            "AL": {"INTERIOR 1": {1: 78.7156, 5: 117.542, 10: 180.43, 20: 483.197, 30: 726.37}},
            # ... (manter todos os estados da planilha GLM .COM)
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
    
    def _buscar_glm(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Busca o valor GLM para o UF, tipo de tarifa e peso
        """
        if tipo_tarifa.startswith("CAPITAL"):
            if modalidade.upper() == "PACKAGE":
                if uf in self.glm_pack_capital:
                    tabela = self.glm_pack_capital[uf]
                    kg_adicional = self.kg_adicional_pack_capital.get(uf, 1.08)
                    pesos_disponiveis = sorted(tabela.keys())
                    return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            else:  # COM
                if uf in self.glm_com_capital:
                    tabela = self.glm_com_capital[uf]
                    kg_adicional = self.kg_adicional_com_capital.get(uf, 6.76)
                    pesos_disponiveis = sorted(tabela.keys())
                    return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            return None
        
        elif tipo_tarifa.startswith("INTERIOR"):
            if modalidade.upper() == "PACKAGE":
                if uf in self.glm_pack_interior and tipo_tarifa in self.glm_pack_interior[uf]:
                    tabela = self.glm_pack_interior[uf][tipo_tarifa]
                    pesos_disponiveis = sorted(tabela.keys())
                    # kg_adicional para interior (usar da planilha GLM PACK)
                    kg_adicional = None  # Buscar da planilha
                    return self._interpolar_valor(tabela, peso, pesos_disponiveis, kg_adicional)
            else:  # COM
                if uf in self.glm_com_interior and tipo_tarifa in self.glm_com_interior[uf]:
                    tabela = self.glm_com_interior[uf][tipo_tarifa]
                    pesos_disponiveis = sorted(tabela.keys())
                    kg_adicional = None  # Buscar da planilha
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
        # 1. Busca o GLM (com a modalidade)
        glm = self._buscar_glm(uf, tipo_tarifa, peso, modalidade)
        if glm is None:
            return None
        
        # 2. Busca o Lucro
        lucro = self._buscar_lucro(tipo_tarifa, peso)
        if lucro is None:
            return None
        
        # 3. Frete = GLM + Lucro
        return round(glm + lucro, 2)