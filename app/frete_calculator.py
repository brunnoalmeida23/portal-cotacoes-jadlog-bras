from app.tabela_precos import TabelaPrecos
import re

class FreteCalculator:
    def __init__(self):
        self.tabela = TabelaPrecos()
        self.base_ceps = {
            "01000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "02000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "03000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "04000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "05000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "06000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "07000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "08000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "08131": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "09000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "20000": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20020": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "30000": {"cidade": "Belo Horizonte", "uf": "MG", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "40000": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "50000": {"cidade": "Recife", "uf": "PE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "60000": {"cidade": "Fortaleza", "uf": "CE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "70000": {"cidade": "Brasília", "uf": "DF", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "80000": {"cidade": "Curitiba", "uf": "PR", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "90000": {"cidade": "Porto Alegre", "uf": "RS", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
        }
        self.cache_ceps = {}

    def buscar_cep(self, cep):
        try:
            cep_limpo = re.sub(r"\D", "", cep)
            if not cep_limpo:
                return None
            if cep_limpo in self.cache_ceps:
                return self.cache_ceps[cep_limpo]
            if len(cep_limpo) >= 5:
                prefixo = cep_limpo[:5]
                if prefixo in self.base_ceps:
                    self.cache_ceps[cep_limpo] = self.base_ceps[prefixo]
                    return self.base_ceps[prefixo]
            resultado = {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1}
            self.cache_ceps[cep_limpo] = resultado
            return resultado
        except:
            return {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1}

    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        try:
            return self.tabela.calcular_frete(uf, tipo_tarifa, peso, modalidade)
        except:
            return None