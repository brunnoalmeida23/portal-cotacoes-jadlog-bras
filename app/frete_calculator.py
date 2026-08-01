from app.tabela_precos import TabelaPrecos
import re

class FreteCalculator:
    def __init__(self):
        self.tabela = TabelaPrecos()
        
        # Base de CEPs para as capitais (reduzida e otimizada)
        self.base_ceps = {
            # SP Capital
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
            # RJ Capital
            "20000": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20020": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20021": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20030": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20040": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20050": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20060": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20070": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20080": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20090": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            # Outras capitais
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
        """Busca informações de um CEP na base de dados"""
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
                
                # Busca parcial
                for chave, valor in self.base_ceps.items():
                    if chave.startswith(prefixo[:4]):
                        self.cache_ceps[cep_limpo] = valor
                        return valor
            
            resultado = self._classificar_por_primeiro_digito(cep_limpo)
            self.cache_ceps[cep_limpo] = resultado
            return resultado
            
        except Exception as e:
            return {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1}
    
    def _classificar_por_primeiro_digito(self, cep):
        """Classifica o CEP pelo primeiro dígito (fallback)"""
        if not cep:
            return {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1}
        
        regioes = {
            "0": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "1": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "2": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "3": {"cidade": "Belo Horizonte", "uf": "MG", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "4": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "5": {"cidade": "Recife", "uf": "PE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "6": {"cidade": "Fortaleza", "uf": "CE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "7": {"cidade": "Brasília", "uf": "DF", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "8": {"cidade": "Curitiba", "uf": "PR", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "9": {"cidade": "Porto Alegre", "uf": "RS", "tipo_tarifa": "CAPITAL 1", "prazo": 2}
        }
        return regioes.get(cep[0], {"cidade": "Desconhecida", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 5})
    
    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """Calcula o subtotal (GLM + Comissão)"""
        try:
            return self.tabela.calcular_frete(uf, tipo_tarifa, peso, modalidade)
        except Exception as e:
            return None
    
    def calcular_frete_total(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """Retorna apenas o subtotal"""
        try:
            resultado = self.calcular_frete(uf, tipo_tarifa, peso, modalidade)
            if resultado:
                return resultado['subtotal']
            return None
        except Exception as e:
            return None