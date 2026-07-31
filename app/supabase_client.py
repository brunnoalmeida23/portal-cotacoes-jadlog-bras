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

def buscar_cotacoes_por_nome(nome):
    """
    Busca cotações pelo nome do cliente (busca parcial com tratamento de caracteres)
    """
    if not supabase:
        print("⚠️ Supabase não configurado")
        return []
    
    if not nome or len(nome.strip()) < 2:
        print("⚠️ Nome muito curto para busca (mínimo 2 caracteres)")
        return []
    
    try:
        # Limpa o nome para busca (remove espaços extras)
        nome_limpo = nome.strip()
        print(f"🔍 Buscando cotações por nome: '{nome_limpo}'")
        
        # Busca usando ilike (case insensitive)
        response = supabase.table("cotacoes")\
            .select("*")\
            .ilike("cliente_nome", f"%{nome_limpo}%")\
            .order("data_criacao", desc=True)\
            .execute()
        
        if response.data and len(response.data) > 0:
            print(f"✅ Encontradas {len(response.data)} cotações para o nome: '{nome_limpo}'")
            return response.data
        
        # Se não encontrou, tenta buscar com o nome normalizado (sem acentos)
        try:
            import unicodedata
            nome_normalizado = ''.join(
                c for c in unicodedata.normalize('NFD', nome_limpo)
                if unicodedata.category(c) != 'Mn'
            )
            
            if nome_normalizado != nome_limpo:
                print(f"🔍 Tentando busca com nome normalizado: '{nome_normalizado}'")
                response = supabase.table("cotacoes")\
                    .select("*")\
                    .ilike("cliente_nome", f"%{nome_normalizado}%")\
                    .order("data_criacao", desc=True)\
                    .execute()
                
                if response.data and len(response.data) > 0:
                    print(f"✅ Encontradas {len(response.data)} cotações para o nome normalizado: '{nome_normalizado}'")
                    return response.data
        except ImportError:
            pass
        
        print(f"ℹ️ Nenhuma cotação encontrada para o nome: '{nome_limpo}'")
        return []
    except Exception as e:
        print(f"❌ Erro ao buscar cotações por nome: {str(e)}")
        import traceback
        traceback.print_exc()
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