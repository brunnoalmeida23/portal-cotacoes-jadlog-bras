@router.post("/api/calcular-frete")
async def calcular_frete_endpoint(
    cep_destino: str = Form(...),
    peso: float = Form(...),
    valor_nf: float = Form(...),
    modalidade: str = Form("PACKAGE"),
    cliente_nome: str = Form(""),
    cliente_documento: str = Form("")
):
    # Percentual do Advalorem (0,66%)
    SEGURO_PERCENT = float(os.getenv("SEGURO_PERCENT", 0.0066))
    
    # Busca informações do CEP
    info_cep = calculator.buscar_cep(cep_destino)
    if not info_cep:
        return JSONResponse({"success": False, "message": f"CEP {cep_destino} não encontrado na base de dados"})
    
    uf = info_cep["uf"]
    tipo_tarifa = info_cep["tipo_tarifa"]
    
    # Calcula o subtotal (GLM + Comissão)
    resultado = calculator.calcular_frete(uf, tipo_tarifa, peso, modalidade)
    
    if resultado is None or resultado.get('subtotal') is None:
        return JSONResponse({"success": False, "message": f"Tarifa não encontrada para {info_cep['cidade']}/{uf} - {tipo_tarifa}"})
    
    subtotal = resultado['subtotal']
    
    # ===== ADVALOREM (0,66% sobre o valor da NF) =====
    advalorem = round(valor_nf * SEGURO_PERCENT, 2)
    
    # ===== TOTAL = Subtotal + Advalorem =====
    total = round(subtotal + advalorem, 2)
    
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
        "subtotal": subtotal,
        "advalorem": advalorem,
        "frete": subtotal,
        "seguro": advalorem,
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
            "subtotal": subtotal,
            "advalorem": advalorem,
            "valor_base": subtotal,
            "seguro": advalorem,
            "total": total,
            "modalidade": modalidade
        }
    })