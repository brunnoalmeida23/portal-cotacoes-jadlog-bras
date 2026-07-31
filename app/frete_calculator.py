import re
import json
import os
from app.tabela_precos import TabelaPrecos

class FreteCalculator:
    def __init__(self):
        self.dados_cidaten = []
        possible_paths = [
            "dados_cidaten.json",
            os.path.join(os.path.dirname(__file__), "..", "dados_cidaten.json"),
            os.path.join(os.path.dirname(__file__), "dados_cidaten.json")
        ]
        for path in possible_paths:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.dados_cidaten = json.load(f)
                    print(f"✅ dados_cidaten.json carregado de: {path} ({len(self.dados_cidaten)} linhas)")
                    break
            except Exception as e:
                continue
        if not self.dados_cidaten:
            print("⚠️ dados_cidaten.json NÃO encontrado!")
        
        # Carregar dados_glm.json
        self.dados_glm = []
        possible_paths_glm = [
            "dados_glm.json",
            os.path.join(os.path.dirname(__file__), "..", "dados_glm.json"),
            os.path.join(os.path.dirname(__file__), "dados_glm.json")
        ]
        for path in possible_paths_glm:
            try:
                with open(path, "r", encoding="utf-8") as f:
                    self.dados_glm = json.load(f)
                    print(f"✅ dados_glm.json carregado de: {path} ({len(self.dados_glm)} linhas)")
                    break
            except Exception as e:
                continue
        if not self.dados_glm:
            print("⚠️ dados_glm.json NÃO encontrado!")
        
        self.tabela = TabelaPrecos()
    
    def buscar_cep(self, cep):
        """Busca informações do CEP na base de dados"""
        cep_limpo = re.sub(r"\D", "", cep)
        
        if len(cep_limpo) != 8:
            return None
        
        cep_num = int(cep_limpo)
        
        # FALLBACK PARA SP CAPITAL (01000-000 a 05999-999)
        if cep_limpo.startswith(("01", "02", "03")):
            return {
                "uf": "SP",
                "cidade": "SAO PAULO",
                "tipo_tarifa": "CAPITAL 1",
                "prazo": "1",
                "seguro": 0.0066,
                "modalidade": "PACKAGE"
            }
        
        # Busca nos dados do JSON
        for item in self.dados_cidaten:
            faixa = item.get("Cep", "")
            if faixa and " a " in faixa:
                try:
                    partes = faixa.split(" a ")
                    cep_ini = int(re.sub(r"\D", "", partes[0]))
                    cep_fim = int(re.sub(r"\D", "", partes[1]))
                    if cep_ini <= cep_num <= cep_fim:
                        uf = item.get("UF", "").strip().upper()
                        tipo = item.get("Tipo Tarifa", "").strip().upper()
                        frap = item.get("Frap (Fob)", "").strip().upper()
                        
                        if tipo.startswith("INTERIOR"):
                            if "1" in tipo:
                                tipo_tarifa = "INTERIOR 1"
                            elif "2" in tipo:
                                tipo_tarifa = "INTERIOR 2"
                            elif "3" in tipo:
                                tipo_tarifa = "INTERIOR 3"
                            else:
                                tipo_tarifa = "INTERIOR 1"
                        else:
                            tipo_tarifa = "CAPITAL 1"
                        
                        return {
                            "uf": uf,
                            "cidade": item.get("Localidade", "").strip().upper(),
                            "tipo_tarifa": tipo_tarifa,
                            "prazo": item.get("Prazo Rodo", "1"),
                            "seguro": float(item.get("% Seguro", 0.0066)),
                            "modalidade": "PACKAGE"
                        }
                except:
                    continue
        
        # Se não encontrou, retorna None
        return None
    
    def calcular_frete(self, uf, tipo_tarifa, peso):
        """Calcula o frete usando a tabela de preços"""
        return self.tabela.calcular_frete(uf, tipo_tarifa, peso)