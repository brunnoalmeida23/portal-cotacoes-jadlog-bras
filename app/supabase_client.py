from supabase import create_client, Client
import os
import re
from datetime import datetime

# Configuração do Supabase
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("⚠️ AVISO: Variáveis SUPABASE_URL e SUPABASE_KEY não configuradas!")
    supabase = None
else:
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ==================== CLIENTES ====================

def buscar_cliente_por_cpf(cpf_cnpj):
    """Busca um cliente pelo CPF/CNPJ"""
    if not supabase:
        return None
    
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    
    try:
        response = supabase.table("clientes")\
            .select("*")\
            .eq("cpf_cnpj", cpf_limpo)\
            .execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        return None
    except Exception as e:
        print(f"❌ Erro ao buscar cliente: {e}")
        return None

def salvar_cliente(dados_cliente):
    """Salva um novo cliente no banco"""
    if not supabase:
        return None
    
    try:
        # Limpa o CPF/CNPJ
        dados_cliente['cpf_cnpj'] = re.sub(r"\D", "", dados_cliente['cpf_cnpj'])
        
        # Adiciona timestamps
        dados_cliente['created_at'] = datetime.now().isoformat()
        dados_cliente['updated_at'] = datetime.now().isoformat()
        
        response = supabase.table("clientes")\
            .insert(dados_cliente)\
            .execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        return None
    except Exception as e:
        print(f"❌ Erro ao salvar cliente: {e}")
        return None

def atualizar_cliente(cpf_cnpj, dados_cliente):
    """Atualiza um cliente existente"""
    if not supabase:
        return None
    
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    dados_cliente['updated_at'] = datetime.now().isoformat()
    
    try:
        response = supabase.table("clientes")\
            .update(dados_cliente)\
            .eq("cpf_cnpj", cpf_limpo)\
            .execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        return None
    except Exception as e:
        print(f"❌ Erro ao atualizar cliente: {e}")
        return None

# ==================== COTAÇÕES ====================

def salvar_cotacao(dados_cotacao):
    """Salva uma cotação no banco"""
    if not supabase:
        print("⚠️ Supabase não configurado, cotação não salva")
        return None
    
    try:
        # Adiciona timestamps
        dados_cotacao['data_criacao'] = datetime.now().isoformat()
        
        response = supabase.table("cotacoes")\
            .insert(dados_cotacao)\
            .execute()
        
        if response.data and len(response.data) > 0:
            print(f"✅ Cotação {dados_cotacao['numero_cotacao']} salva com sucesso!")
            return response.data[0]
        return None
    except Exception as e:
        print(f"❌ Erro ao salvar cotação: {e}")
        return None

def buscar_cotacao_por_numero(numero_cotacao):
    """Busca uma cotação pelo número"""
    if not supabase:
        return None
    
    try:
        response = supabase.table("cotacoes")\
            .select("*")\
            .eq("numero_cotacao", numero_cotacao)\
            .execute()
        
        if response.data and len(response.data) > 0:
            return response.data[0]
        return None
    except Exception as e:
        print(f"❌ Erro ao buscar cotação: {e}")
        return None

def buscar_cotacoes_por_cliente(cpf_cnpj):
    """Busca todas as cotações de um cliente"""
    if not supabase:
        return None
    
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    
    try:
        response = supabase.table("cotacoes")\
            .select("*")\
            .eq("cliente_documento", cpf_limpo)\
            .order("data_criacao", desc=True)\
            .execute()
        
        if response.data and len(response.data) > 0:
            return response.data
        return []
    except Exception as e:
        print(f"❌ Erro ao buscar cotações do cliente: {e}")
        return []

# ==================== GERAR NÚMERO DE COTAÇÃO ====================

def gerar_numero_cotacao():
    """Gera um número de cotação no formato COT-YYYY-NNNN"""
    ano = datetime.now().year
    
    # Busca o último número do ano
    if supabase:
        try:
            response = supabase.table("cotacoes")\
                .select("numero_cotacao")\
                .like("numero_cotacao", f"COT-{ano}-%")\
                .order("numero_cotacao", desc=True)\
                .limit(1)\
                .execute()
            
            if response.data and len(response.data) > 0:
                ultimo = response.data[0]['numero_cotacao']
                numero = int(ultimo.split('-')[2]) + 1
            else:
                numero = 1
        except:
            numero = 1
    else:
        numero = 1
    
    return f"COT-{ano}-{numero:04d}"