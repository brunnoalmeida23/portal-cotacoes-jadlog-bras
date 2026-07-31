from fastapi import APIRouter, Request, Form, Query
from fastapi.responses import JSONResponse, StreamingResponse
import re
import os
import io
from datetime import datetime

# Importações dos seus módulos
from app.supabase_client import (
    salvar_cotacao, buscar_cotacao_por_numero, gerar_numero_cotacao,
    buscar_cliente_por_cpf, salvar_cliente, atualizar_cliente,
    buscar_cotacoes_por_cliente, buscar_cotacoes_por_nome
)
from app.frete_calculator import FreteCalculator
from cupom_pdf import CupomPDF

router = APIRouter()
calculator = FreteCalculator()

# ===== ROTAS PARA CLIENTES =====
@router.post("/api/buscar-cliente")
async def api_buscar_cliente(cpf_cnpj: str = Form(...)):
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    if len(cpf_limpo) not in [11, 14]:
        return JSONResponse({"success": False, "message": "CPF/CNPJ inválido"})
    cliente = buscar_cliente_por_cpf(cpf_limpo)
    if cliente:
        return JSONResponse({"success": True, "dados": cliente})
    return JSONResponse({"success": False, "message": "Cliente não encontrado"})

@router.post("/api/salvar-cliente")
async def api_salvar_cliente(
    cpf_cnpj: str = Form(...),
    nome: str = Form(...),
    razao_social: str = Form(""),
    endereco: str = Form(""),
    cidade: str = Form(""),
    uf: str = Form(""),
    cep: str = Form(""),
    telefone: str = Form(""),
    email: str = Form(""),
    observacoes: str = Form("")
):
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    if len(cpf_limpo) not in [11, 14]:
        return JSONResponse({"success": False, "message": "CPF/CNPJ inválido"})
    
    cliente_existente = buscar_cliente_por_cpf(cpf_limpo)
    if cliente_existente:
        return JSONResponse({"success": False, "message": "Cliente já cadastrado"})
    
    dados_cliente = {
        "cpf_cnpj": cpf_limpo,
        "nome": nome.strip(),
        "razao_social": razao_social.strip() if razao_social else None,
        "endereco": endereco.strip() if endereco else None,
        "cidade": cidade.strip() if cidade else None,
        "uf": uf.strip().upper() if uf else None,
        "cep": cep.strip() if cep else None,
        "telefone": telefone.strip() if telefone else None,
        "email": email.strip() if email else None,
        "observacoes": observacoes.strip() if observacoes else None
    }
    cliente = salvar_cliente(dados_cliente)
    if cliente:
        return JSONResponse({"success": True, "dados": cliente, "message": "Cliente cadastrado com sucesso!"})
    return JSONResponse({"success": False, "message": "Erro ao cadastrar cliente"})

@router.post("/api/atualizar-cliente")
async def api_atualizar_cliente(
    cpf_cnpj: str = Form(...),
    nome: str = Form(...),
    razao_social: str = Form(""),
    endereco: str = Form(""),
    cidade: str = Form(""),
    uf: str = Form(""),
    cep: str = Form(""),
    telefone: str = Form(""),
    email: str = Form(""),
    observacoes: str = Form("")
):
    cpf_limpo = re.sub(r"\D", "", cpf_cnpj)
    if len(cpf_limpo) not in [11, 14]:
        return JSONResponse({"success": False, "message": "CPF/CNPJ inválido"})
    dados_cliente = {
        "nome": nome.strip(),
        "razao_social": razao_social.strip() if razao_social else None,
        "endereco": endereco.strip() if endereco else None,
        "cidade": cidade.strip() if cidade else None,
        "uf": uf.strip().upper() if uf else None,
        "cep": cep.strip() if cep else None,
        "telefone": telefone.strip() if telefone else None,
        "email": email.strip() if email else None,
        "observacoes": observacoes.strip() if observacoes else None
    }
    cliente = atualizar_cliente(cpf_limpo, dados_cliente)
    if cliente:
        return JSONResponse({"success": True, "dados": cliente, "message": "Cliente atualizado com sucesso!"})
    return JSONResponse({"success": False, "message": "Erro ao atualizar cliente"})

# ===== ROTA PARA CALCULAR FRETE =====
@router.post("/api/calcular-frete")
async def calcular_frete_endpoint(
    cep_destino: str = Form(...),
    peso: float = Form(...),
    valor_nf: float = Form(...),
    modalidade: str = Form("PACKAGE"),
    cliente_nome: str = Form(""),
    cliente_documento: str = Form("")
):
    SEGURO_PERCENT = float(os.getenv("SEGURO_PERCENT", 0.0066))
    info_cep = calculator.buscar_cep(cep_destino)
    if not info_cep:
        return JSONResponse({"success": False, "message": f"CEP {cep_destino} não encontrado na base de dados"})
    
    uf = info_cep["uf"]
    tipo_tarifa = info_cep["tipo_tarifa"]
    
    # Calcula o frete com a modalidade selecionada
    valor_base = calculator.calcular_frete(uf, tipo_tarifa, peso, modalidade)
    
    if valor_base is None:
        return JSONResponse({"success": False, "message": f"Tarifa não encontrada para {info_cep['cidade']}/{uf} - {tipo_tarifa}"})
    
    # ===== SEGURO (Advalorem) =====
    # O seguro é calculado sobre o valor da NF, independente da modalidade
    seguro = round(valor_nf * SEGURO_PERCENT, 2)
    
    total = round(valor_base + seguro, 2)
    numero_cotacao = gerar_numero_cotacao()
    
    dados_cotacao = {
        "numero_cotacao": numero_cotacao,
        "cliente_nome": cliente_nome.strip() if cliente_nome else None,
        "cliente_documento": cliente_documento.strip() if cliente_documento else None,
        "cep_destino": cep_destino,
        "cidade": info_cep["cidade"],
        "uf": info_cep["uf"],
        "tipo_tarifa": tipo_tarifa,
        "peso": peso,
        "valor_nf": valor_nf,
        "frete": valor_base,
        "seguro": seguro,
        "total": total,
        "prazo": info_cep["prazo"],
        "origem_cep": "03032-000",
        "modalidade": modalidade
    }
    
    resultado_salvo = salvar_cotacao(dados_cotacao)
    if not resultado_salvo:
        print("⚠️ AVISO: Cotação calculada mas NÃO salva no banco!")
    
    return JSONResponse({
        "success": True,
        "dados": {
            "numero_cotacao": numero_cotacao,
            "destino": f"{info_cep['cidade']}/{info_cep['uf']}",
            "tipo": tipo_tarifa,
            "prazo": f"{info_cep['prazo']} dias",
            "peso": peso,
            "valor_base": valor_base,
            "seguro": seguro,
            "total": total,
            "modalidade": modalidade
        }
    })

# ===== ROTA PARA BUSCAR COTAÇÃO =====
@router.get("/api/buscar-cotacao")
async def api_buscar_cotacao(numero: str = None, documento: str = None, nome: str = None):
    if numero:
        resultado = buscar_cotacao_por_numero(numero)
        if resultado:
            return JSONResponse({"success": True, "dados": resultado})
        return JSONResponse({"success": False, "message": "Cotação não encontrada"})
    elif documento:
        resultado = buscar_cotacoes_por_cliente(documento)
        if resultado:
            return JSONResponse({"success": True, "dados": resultado})
        return JSONResponse({"success": False, "message": "Nenhuma cotação encontrada para este cliente"})
    elif nome:
        resultado = buscar_cotacoes_por_nome(nome)
        if resultado:
            return JSONResponse({"success": True, "dados": resultado})
        return JSONResponse({"success": False, "message": "Nenhuma cotação encontrada para este nome"})
    return JSONResponse({"success": False, "message": "Parâmetro de busca não informado"})

# ===== ROTA PARA RECIBO (PDF) =====
@router.get("/api/imprimir-recibo")
@router.post("/api/imprimir-recibo")
async def imprimir_recibo(request: Request, numero_cotacao: str = Query(None)):
    if not numero_cotacao:
        try:
            form_data = await request.form()
            numero_cotacao = form_data.get('numero_cotacao')
        except:
            pass
    if not numero_cotacao:
        try:
            body = await request.json()
            numero_cotacao = body.get('numero_cotacao')
        except:
            pass
    if not numero_cotacao:
        return JSONResponse({"success": False, "message": "Número da cotação não informado"}, status_code=400)
    
    print(f"🔍 Buscando cotação: {numero_cotacao}")
    resultado = buscar_cotacao_por_numero(numero_cotacao)
    if not resultado:
        print(f"❌ Cotação não encontrada: {numero_cotacao}")
        return JSONResponse({"success": False, "message": f"Cotação {numero_cotacao} não encontrada"}, status_code=404)
    
    try:
        print("📄 Gerando recibo...")
        pdf = CupomPDF()
        pdf_bytes = pdf.gerar_recibo(resultado)
        print(f"✅ Recibo gerado com sucesso! Tamanho: {len(pdf_bytes)} bytes")
        return StreamingResponse(
            io.BytesIO(pdf_bytes),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=recibo_{numero_cotacao}.pdf"}
        )
    except Exception as e:
        print(f"❌ Erro ao gerar recibo: {str(e)}")
        import traceback
        traceback.print_exc()
        return JSONResponse({"success": False, "message": f"Erro ao gerar recibo: {str(e)}"}, status_code=500)