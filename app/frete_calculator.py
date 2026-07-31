from app.tabela_precos import TabelaPrecos

class FreteCalculator:
    def __init__(self):
        self.tabela = TabelaPrecos()
        # Base de dados de CEPs (simplificada para exemplo)
        self.base_ceps = {
            "01000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "02000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "03000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "04000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "05000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "06000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "07000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "08000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "09000": {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1},
            "10000": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "20000": {"cidade": "Rio de Janeiro", "uf": "RJ", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "30000": {"cidade": "Belo Horizonte", "uf": "MG", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "40000": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "50000": {"cidade": "Recife", "uf": "PE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "60000": {"cidade": "Fortaleza", "uf": "CE", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            "70000": {"cidade": "Brasília", "uf": "DF", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "80000": {"cidade": "Curitiba", "uf": "PR", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            "90000": {"cidade": "Porto Alegre", "uf": "RS", "tipo_tarifa": "CAPITAL 1", "prazo": 2},
            # INTERIOR - Exemplos
            "69900": {"cidade": "Rio Branco", "uf": "AC", "tipo_tarifa": "INTERIOR 1", "prazo": 7},
            "69945": {"cidade": "Cruzeiro do Sul", "uf": "AC", "tipo_tarifa": "INTERIOR 1", "prazo": 10},
            "57000": {"cidade": "Maceió", "uf": "AL", "tipo_tarifa": "CAPITAL 1", "prazo": 4},
            "68900": {"cidade": "Macapá", "uf": "AP", "tipo_tarifa": "CAPITAL 1", "prazo": 8},
            "69000": {"cidade": "Manaus", "uf": "AM", "tipo_tarifa": "CAPITAL 1", "prazo": 7},
            "40000": {"cidade": "Salvador", "uf": "BA", "tipo_tarifa": "CAPITAL 1", "prazo": 3},
            # ... mais CEPs podem ser adicionados conforme necessário
        }
        
    def buscar_cep(self, cep):
        """Busca informações de um CEP na base de dados"""
        # Remove formatação
        cep_limpo = re.sub(r"\D", "", cep)
        
        # Se o CEP tem 8 dígitos, pega os 5 primeiros para consulta
        if len(cep_limpo) >= 5:
            prefixo = cep_limpo[:5]
        else:
            prefixo = cep_limpo
            
        # Busca na base de CEPs
        if prefixo in self.base_ceps:
            return self.base_ceps[prefixo]
        
        # Se não encontrou, tenta buscar por faixa de CEP
        # Exemplo: CEPs começando com 01xxx são SP Capital
        if cep_limpo.startswith("01"):
            return {"cidade": "São Paulo", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 1}
        
        # Para CEPs não encontrados, retorna um padrão com base no primeiro dígito
        primeiro_digito = cep_limpo[0] if cep_limpo else "0"
        
        # Mapeamento simples por região
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
        
        return regioes.get(primeiro_digito, {"cidade": "Desconhecida", "uf": "SP", "tipo_tarifa": "CAPITAL 1", "prazo": 5})
    
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