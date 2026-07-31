import json
import re

class FreteCalculator:
    def __init__(self):
        # Carregar dados
        with open("dados_glm.json", "r", encoding="utf-8") as f:
            self.dados_glm = json.load(f)
        
        with open("dados_cidaten.json", "r", encoding="utf-8") as f:
            self.dados_cidaten = json.load(f)
        
        # Mapear pesos para colunas
        self.pesos = [
            0.25, 0.50, 1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00,
            10.00, 11.00, 12.00, 13.00, 14.00, 15.00, 16.00, 17.00, 18.00, 19.00,
            20.00, 21.00, 22.00, 23.00, 24.00, 25.00, 26.00, 27.00, 28.00, 29.00, 30.00
        ]
        
        # Nomes das colunas de peso no JSON (ex: "0.2500", "1.0000")
        self.colunas_peso = [f"{p:.4f}" for p in self.pesos]
        
        # Criar índice por UF e Tipo de Tarifa
        self.glm_index = {}
        for item in self.dados_glm:
            uf = item.get("UF", "").strip().upper()
            tipo = item.get("Tipo de Tarifa", "").strip()
            if uf and tipo:
                key = f"{uf}|{tipo}"
                if key not in self.glm_index:
                    self.glm_index[key] = []
                self.glm_index[key].append(item)
    
    def buscar_cep(self, cep):
        """Busca informações do CEP"""
        # Limpar CEP
        cep_limpo = re.sub(r"\D", "", cep)
        if len(cep_limpo) != 8:
            return None
        
        cep_num = int(cep_limpo)
        
        for item in self.dados_cidaten:
            faixa = item.get("Cep", "")
            if faixa and " a " in faixa:
                try:
                    partes = faixa.split(" a ")
                    cep_ini = int(re.sub(r"\D", "", partes[0]))
                    cep_fim = int(re.sub(r"\D", "", partes[1]))
                    if cep_ini <= cep_num <= cep_fim:
                        return {
                            "uf": item.get("UF", "").strip(),
                            "cidade": item.get("Localidade", "").strip(),
                            "tipo_tarifa": item.get("Tipo Tarifa", "").strip(),
                            "prazo": item.get("Prazo Rodo", ""),
                            "seguro": float(item.get("% Seguro", 0.0066))
                        }
                except:
                    continue
        return None
    
    def calcular_frete(self, uf, tipo_tarifa, peso, modalidade="Package"):
        """Calcula o frete baseado na UF, tipo de tarifa, peso e modalidade"""
        
        # Buscar na tabela GLM
        key = f"{uf}|{tipo_tarifa}"
        if key not in self.glm_index:
            return None
        
        # Encontrar a linha correta
        for item in self.glm_index[key]:
            # Encontrar a coluna de peso correta
            for i, coluna in enumerate(self.colunas_peso):
                if peso <= self.pesos[i]:
                    valor = item.get(coluna, 0)
                    if valor and isinstance(valor, (int, float)):
                        return float(valor)
                    break
        
        # Se peso > 30kg, usar kg adicional
        if peso > 30:
            valor_base = item.get("30.0000", 0)
            kg_adicional = item.get("Kg Adicional", 0)
            if valor_base and kg_adicional:
                extra = (peso - 30) * kg_adicional
                return float(valor_base) + float(extra)
        
        return None