from app.tabela_precos import TabelaPrecos
import re
import os

# Tenta importar a base de CEPs
try:
    from app.ceps_data import CEPS_DATABASE
    print(f"✅ Base de CEPs carregada: {len(CEPS_DATABASE)} registros")
except ImportError:
    print("⚠️ Arquivo ceps_data.py não encontrado. Usando base de fallback.")
    # Base de fallback (mínima)
    CEPS_DATABASE = {
        "01000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
        "02000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
        "03000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
        "04000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
        "05000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
        "20000": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
        "30000": {"cidade": "Belo Horizonte", "uf": "MG", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
        "40000": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
        "50000": {"cidade": "Recife", "uf": "PE", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
        "60000": {"cidade": "Fortaleza", "uf": "CE", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
        "70000": {"cidade": "Brasília", "uf": "DF", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
        "80000": {"cidade": "Curitiba", "uf": "PR", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
        "90000": {"cidade": "Porto Alegre", "uf": "RS", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
    }

class FreteCalculator:
    def __init__(self):
        self.tabela = TabelaPrecos()
        self.base_ceps = CEPS_DATABASE
        self.cache_ceps = {}
        print(f"📊 FreteCalculator inicializado com {len(self.base_ceps)} CEPs")

    def buscar_cep(self, cep):
        """
        Busca informações de um CEP na base de dados
        """
        # Remove formatação
        cep_limpo = re.sub(r"\D", "", cep)
        
        if not cep_limpo:
            return None
        
        # Verifica cache
        if cep_limpo in self.cache_ceps:
            return self.cache_ceps[cep_limpo]
        
        # Tenta com 5 dígitos (prefixo)
        if len(cep_limpo) >= 5:
            prefixo = cep_limpo[:5]
            
            # Busca exata pelo prefixo
            if prefixo in self.base_ceps:
                self.cache_ceps[cep_limpo] = self.base_ceps[prefixo]
                print(f"✅ CEP {cep_limpo} encontrado: {self.base_ceps[prefixo]}")
                return self.base_ceps[prefixo]
            
            # Tenta com 4 dígitos
            if len(prefixo) >= 4:
                prefixo_4 = prefixo[:4]
                for chave, valor in self.base_ceps.items():
                    if chave.startswith(prefixo_4):
                        self.cache_ceps[cep_limpo] = valor
                        print(f"✅ CEP {cep_limpo} encontrado por prefixo 4: {valor}")
                        return valor
            
            # Tenta com 3 dígitos
            if len(prefixo) >= 3:
                prefixo_3 = prefixo[:3] + "000"
                if prefixo_3 in self.base_ceps:
                    self.cache_ceps[cep_limpo] = self.base_ceps[prefixo_3]
                    print(f"✅ CEP {cep_limpo} encontrado por prefixo 3: {self.base_ceps[prefixo_3]}")
                    return self.base_ceps[prefixo_3]
            
            # Tenta com 2 dígitos
            if len(prefixo) >= 2:
                prefixo_2 = prefixo[:2] + "0000"
                if prefixo_2 in self.base_ceps:
                    self.cache_ceps[cep_limpo] = self.base_ceps[prefixo_2]
                    print(f"✅ CEP {cep_limpo} encontrado por prefixo 2: {self.base_ceps[prefixo_2]}")
                    return self.base_ceps[prefixo_2]
        
        # Se não encontrou, classifica por primeiro dígito
        resultado = self._classificar_por_primeiro_digito(cep_limpo)
        self.cache_ceps[cep_limpo] = resultado
        print(f"⚠️ CEP {cep_limpo} não encontrado. Usando fallback: {resultado}")
        return resultado
    
    def _classificar_por_primeiro_digito(self, cep):
        """
        Classifica o CEP pelo primeiro dígito (fallback)
        """
        if not cep:
            return {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066}
        
        primeiro_digito = cep[0]
        
        # Mapeamento por região (baseado no padrão dos Correios)
        regioes = {
            "0": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
            "1": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1, "seguro": 0.0066},
            "2": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
            "3": {"cidade": "Belo Horizonte", "uf": "MG", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
            "4": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
            "5": {"cidade": "Recife", "uf": "PE", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
            "6": {"cidade": "Fortaleza", "uf": "CE", "tipo_tarifa": "CAPITAL 1", "prazo": 3, "seguro": 0.0066},
            "7": {"cidade": "Brasília", "uf": "DF", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
            "8": {"cidade": "Curitiba", "uf": "PR", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066},
            "9": {"cidade": "Porto Alegre", "uf": "RS", "tipo_tarifa": "CAPITAL 1", "prazo": 2, "seguro": 0.0066}
        }
        
        return regioes.get(primeiro_digito, {"cidade": "Desconhecida", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 5, "seguro": 0.0066})
    
    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Calcula o frete usando a tabela de preços
        """
        return self.tabela.calcular_frete(uf, tipo_tarifa, peso, modalidade)
    
    def calcular_lucro(self, uf, tipo_tarifa, peso, modalidade="PACKAGE"):
        """
        Calcula o lucro (uso interno)
        """
        return self.tabela.calcular_lucro(uf, tipo_tarifa, peso, modalidade)