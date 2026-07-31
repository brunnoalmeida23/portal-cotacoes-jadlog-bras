from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/simulador", response_class=HTMLResponse)
async def simulador():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JADLOG BRÁS - Simulador</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
        <link rel="manifest" href="/manifest.json">
        <meta name="theme-color" content="#E31E24">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="Jadlog Brás">
        <link rel="apple-touch-icon" href="/icons/launchericon-192x192.png">
        <style>
            .bg-jadlog { background: #E31E24; }
            .btn-jadlog { background: #E31E24; color: white; border: none; padding: 10px 30px; border-radius: 8px; }
            .btn-jadlog:hover { background: #B81217; color: white; }
            .btn-jadlog:disabled { opacity: 0.6; cursor: not-allowed; }
            .card-shadow { background: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); padding: 24px; }
            .footer { background: #212529; color: white; padding: 15px 0; margin-top: 40px; text-align: center; }
            .nav-link { color: white !important; }
            .navbar-brand { color: white !important; font-weight: 700; }
            .resultado-box { background: #f8f9fa; padding: 16px; border-radius: 8px; border-left: 4px solid #E31E24; }
            .badge-origem { background: #E31E24; color: white; padding: 8px 16px; border-radius: 20px; font-weight: 600; display: inline-block; }
            .badge-cotacao { background: #28a745; color: white; padding: 8px 16px; border-radius: 20px; font-weight: 600; display: inline-block; }
            .badge-cliente { background: #17a2b8; color: white; padding: 4px 12px; border-radius: 20px; font-size: 0.8rem; }
            .tabela-precos { background: #f8f9fa; border-radius: 8px; padding: 12px; }
            .tabela-precos td { padding: 4px 8px; }
            .install-banner {
                position: fixed;
                bottom: 0;
                left: 0;
                right: 0;
                background: white;
                padding: 16px 20px;
                box-shadow: 0 -4px 20px rgba(0,0,0,0.15);
                display: none;
                align-items: center;
                justify-content: space-between;
                z-index: 9999;
                border-top: 3px solid #E31E24;
            }
            .install-banner .btn-install {
                background: #E31E24;
                color: white;
                border: none;
                padding: 10px 24px;
                border-radius: 10px;
                font-weight: 600;
                cursor: pointer;
            }
            .install-banner .btn-install:hover {
                background: #B81217;
            }
            .install-banner .btn-close-banner {
                background: transparent;
                border: none;
                font-size: 1.5rem;
                color: #999;
                cursor: pointer;
            }
            .promocao-bras {
                background: #f8f9fa;
                border: 2px dashed #E31E24;
                border-radius: 8px;
                padding: 10px;
                margin-top: 15px;
                text-align: center;
            }
            .promocao-bras .titulo {
                color: #E31E24;
                font-weight: 600;
                font-size: 0.9rem;
            }
            .promocao-bras .validade {
                color: #6c757d;
                font-size: 0.8rem;
            }
            .cliente-encontrado {
                background: #d4edda;
                border: 1px solid #c3e6cb;
                border-radius: 8px;
                padding: 12px;
                margin-bottom: 15px;
            }
            .modal-content {
                border-radius: 12px;
            }
            .modal-header {
                background: #E31E24;
                color: white;
                border-radius: 12px 12px 0 0;
            }
            .modal-header .btn-close {
                filter: brightness(0) invert(1);
            }
        </style>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg bg-jadlog">
            <div class="container">
                <a class="navbar-brand" href="/">
                    <img src="/logo" alt="Jadlog" height="70" style="max-height:70px; width:auto; background:white; padding:10px 16px; border-radius:12px; box-shadow: 0 2px 8px rgba(0,0,0,0.15);">
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMenu">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navMenu">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="/">Início</a></li>
                        <li class="nav-item"><a class="nav-link active" href="/simulador">Simulador</a></li>
                        <li class="nav-item"><a class="nav-link" href="/consulta">Consulta</a></li>
                        <li class="nav-item" id="loginButton">
                            <button class="btn btn-outline-light btn-sm ms-2" onclick="abrirLogin()">
                                <i class="bi bi-box-arrow-in-right me-1"></i> Funcionário
                            </button>
                        </li>
                        <li class="nav-item" id="logoutButton" style="display:none;">
                            <button class="btn btn-outline-light btn-sm ms-2" onclick="logout()">
                                <i class="bi bi-box-arrow-right me-1"></i> Sair
                            </button>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Modal de Login -->
        <div class="modal fade" id="loginModal" tabindex="-1">
            <div class="modal-dialog modal-sm">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="bi bi-person-badge me-2"></i>Acesso Funcionário</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <p class="text-muted">Digite a senha para acessar as funções restritas:</p>
                        <input type="password" class="form-control form-control-lg" id="senhaLogin" placeholder="Senha">
                        <small class="text-muted d-block mt-2">Senha padrão: <strong>jadlog2026</strong></small>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button class="btn btn-jadlog" onclick="validarLogin()">
                            <i class="bi bi-box-arrow-in-right me-1"></i> Entrar
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal de Senha para Impressão -->
        <div class="modal fade" id="senhaModal" tabindex="-1">
            <div class="modal-dialog modal-sm">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title"><i class="bi bi-lock me-2"></i>Confirmação de Senha</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                    </div>
                    <div class="modal-body">
                        <p class="text-muted">Digite a senha para imprimir o recibo:</p>
                        <input type="password" class="form-control form-control-lg" id="senhaImpressao" placeholder="Senha">
                        <small class="text-muted d-block mt-2">Senha padrão: <strong>jadlog2026</strong></small>
                    </div>
                    <div class="modal-footer">
                        <button class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                        <button class="btn btn-jadlog" onclick="validarSenhaImpressao()">
                            <i class="bi bi-printer me-1"></i> Imprimir
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="install-banner" id="installBanner">
            <div style="display:flex;align-items:center;gap:12px;">
                <div style="width:48px;height:48px;border-radius:12px;background:#E31E24;display:flex;align-items:center;justify-content:center;color:white;font-weight:800;font-size:24px;">J</div>
                <div>
                    <p style="font-weight:600;margin:0;">JADLOG BRÁS</p>
                    <p style="font-size:0.85rem;color:#6c757d;margin:0;">Instale o app para cotações rápidas</p>
                </div>
            </div>
            <div style="display:flex;gap:8px;align-items:center;">
                <button class="btn-install" id="installBtn">📲 Instalar App</button>
                <button class="btn-close-banner" id="closeBannerBtn">✕</button>
            </div>
        </div>

        <main class="container py-4">
            <h2 class="fw-bold mb-4"><i class="bi bi-calculator text-danger me-2"></i>Simular Frete</h2>

            <div class="row g-4">
                <div class="col-lg-7">
                    <div class="card-shadow">
                        <div class="mb-3">
                            <h6 class="fw-bold">
                                <i class="bi bi-person-badge text-danger me-2"></i>
                                Dados do Cliente
                            </h6>
                            <div class="input-group mb-2">
                                <span class="input-group-text"><i class="bi bi-search"></i></span>
                                <input type="text" class="form-control" id="buscarCliente" 
                                       placeholder="Digite o CPF ou CNPJ do cliente" maxlength="18">
                                <button class="btn btn-jadlog" type="button" onclick="buscarCliente()">
                                    <i class="bi bi-search"></i> Buscar
                                </button>
                                <button class="btn btn-outline-secondary" type="button" onclick="limparCliente()">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div id="statusCliente" style="display:none;" class="mb-2">
                                <span id="statusMensagem"></span>
                            </div>
                            <div id="clienteCarregado" style="display:none;" class="cliente-encontrado">
                                <div class="d-flex justify-content-between align-items-center">
                                    <div>
                                        <strong id="clienteNomeCarregado"></strong>
                                        <small class="d-block text-muted" id="clienteInfoCarregado"></small>
                                    </div>
                                    <span class="badge-cliente">✅ Cliente encontrado</span>
                                </div>
                            </div>
                            <div id="formCliente" style="display:none;">
                                <div class="row g-2">
                                    <div class="col-md-6">
                                        <label class="fw-bold small">CPF/CNPJ *</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteCpf" 
                                               placeholder="000.000.000-00" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="fw-bold small">Nome *</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteNome" 
                                               placeholder="Nome completo" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="fw-bold small">Razão Social</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteRazao" 
                                               placeholder="Razão social (opcional)">
                                    </div>
                                    <div class="col-md-6">
                                        <label class="fw-bold small">Telefone</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteTelefone" 
                                               placeholder="(11) 99999-9999">
                                    </div>
                                    <div class="col-md-12">
                                        <label class="fw-bold small">Endereço</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteEndereco" 
                                               placeholder="Rua, número, complemento">
                                    </div>
                                    <div class="col-md-4">
                                        <label class="fw-bold small">Cidade</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteCidade" 
                                               placeholder="Cidade">
                                    </div>
                                    <div class="col-md-4">
                                        <label class="fw-bold small">UF</label>
                                        <select class="form-control form-control-sm" id="clienteUf">
                                            <option value="">Selecione</option>
                                            <option value="AC">AC</option><option value="AL">AL</option>
                                            <option value="AP">AP</option><option value="AM">AM</option>
                                            <option value="BA">BA</option><option value="CE">CE</option>
                                            <option value="DF">DF</option><option value="ES">ES</option>
                                            <option value="GO">GO</option><option value="MA">MA</option>
                                            <option value="MT">MT</option><option value="MS">MS</option>
                                            <option value="MG">MG</option><option value="PA">PA</option>
                                            <option value="PB">PB</option><option value="PR">PR</option>
                                            <option value="PE">PE</option><option value="PI">PI</option>
                                            <option value="RJ">RJ</option><option value="RN">RN</option>
                                            <option value="RS">RS</option><option value="RO">RO</option>
                                            <option value="RR">RR</option><option value="SC">SC</option>
                                            <option value="SP">SP</option><option value="SE">SE</option>
                                            <option value="TO">TO</option>
                                        </select>
                                    </div>
                                    <div class="col-md-4">
                                        <label class="fw-bold small">CEP</label>
                                        <input type="text" class="form-control form-control-sm" id="clienteCep" 
                                               placeholder="00000-000">
                                    </div>
                                </div>
                                <button type="button" class="btn btn-success btn-sm w-100 mt-2" onclick="salvarCliente()">
                                    <i class="bi bi-save me-1"></i> Salvar Cliente
                                </button>
                            </div>
                        </div>
                        
                        <hr>
                        
                        <div class="mb-3">
                            <label class="fw-bold">Origem</label>
                            <div class="badge-origem">
                                <i class="bi bi-geo-alt-fill me-2"></i>
                                Brás - SP (03000-000)
                            </div>
                        </div>
                        
                        <form id="formSimulador">
                            <input type="hidden" id="clienteDocumento" value="">
                            <div class="mb-3">
                                <label class="fw-bold">
                                    <i class="bi bi-geo-alt me-1"></i>
                                    CEP de Destino
                                </label>
                                <input type="text" class="form-control form-control-lg" id="cepDestino" 
                                       placeholder="Digite o CEP do destinatário" maxlength="9" required>
                                <small class="text-muted">Ex: 01000-000 (SP Capital) ou 69945-000 (Interior)</small>
                            </div>
                            <div class="row g-3">
                                <div class="col-md-6">
                                    <label class="fw-bold">
                                        <i class="bi bi-weight-scale me-1"></i>
                                        Peso (kg)
                                    </label>
                                    <input type="number" class="form-control form-control-lg" id="peso" 
                                           step="0.001" placeholder="Ex: 2.350" required>
                                </div>
                                <div class="col-md-6">
                                    <label class="fw-bold">
                                        <i class="bi bi-receipt me-1"></i>
                                        Valor da NF (R$)
                                    </label>
                                    <input type="number" class="form-control form-control-lg" id="valorNF" 
                                           step="0.01" placeholder="Ex: 5000.00" required>
                                    <small class="text-muted">Seguro: 0,66% do valor da NF</small>
                                </div>
                            </div>
                            <button type="submit" class="btn btn-jadlog w-100 mt-4" id="btnCalcular">
                                <i class="bi bi-calculator me-2"></i>
                                Calcular Frete
                            </button>
                        </form>
                    </div>
                </div>

                <div class="col-lg-5">
                    <div class="card-shadow" id="resultadoArea">
                        <h5 class="fw-bold">
                            <i class="bi bi-file-text text-danger me-2"></i>
                            Resultado da Cotação
                        </h5>
                        <div class="text-center text-muted py-5">
                            <i class="bi bi-search fs-1 d-block mb-3"></i>
                            <p>Preencha os dados ao lado<br>e clique em <strong>Calcular Frete</strong></p>
                        </div>
                    </div>
                    
                    <div class="card-shadow" id="resultadoDados" style="display:none;">
                        <h5 class="fw-bold">
                            <i class="bi bi-file-text text-danger me-2"></i>
                            Resultado da Cotação
                        </h5>
                        <div class="mb-3">
                            <span class="badge-cotacao" id="numeroCotacao" style="cursor:pointer;" title="Clique duas vezes para funções restritas">
                                <i class="bi bi-hash me-1"></i>COT-2026-0001
                            </span>
                        </div>
                        <div class="resultado-box">
                            <div class="row">
                                <div class="col-6">
                                    <small class="text-muted">Origem</small>
                                    <p class="fw-bold mb-0">Brás - SP</p>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Destino</small>
                                    <p class="fw-bold mb-0" id="resDestino">-</p>
                                </div>
                            </div>
                            <div class="row mt-2">
                                <div class="col-6">
                                    <small class="text-muted">Tipo</small>
                                    <p class="fw-bold mb-0" id="resTipo">-</p>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Prazo</small>
                                    <p class="fw-bold mb-0" id="resPrazo">-</p>
                                </div>
                            </div>
                            <div class="row mt-2">
                                <div class="col-6">
                                    <small class="text-muted">Peso</small>
                                    <p class="fw-bold mb-0" id="resPeso">-</p>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Modalidade</small>
                                    <p class="fw-bold mb-0" id="resModalidade">PACKAGE</p>
                                </div>
                            </div>
                            <hr>
                            <div class="row">
                                <div class="col-6">
                                    <small class="text-muted">Valor do Frete</small>
                                    <p class="fw-bold text-success fs-5" id="resFrete">R$ -</p>
                                </div>
                                <div class="col-6">
                                    <small class="text-muted">Seguro</small>
                                    <p class="fw-bold" id="resSeguro">R$ -</p>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-12">
                                    <small class="text-muted">Frete Total</small>
                                    <p class="fw-bold fs-3 text-danger" id="resTotal">R$ -</p>
                                </div>
                            </div>
                            <div class="promocao-bras">
                                <div class="titulo">
                                    <i class="bi bi-star-fill text-warning me-1"></i>
                                    VALORES EXCLUSIVOS DA UNIDADE DA AV. VALTIER (BRÁS)
                                </div>
                                <div class="validade">
                                    <i class="bi bi-calendar me-1"></i>
                                    Válidos até Dezembro de 2026
                                </div>
                            </div>
                        </div>
                        
                        <!-- BOTÕES -->
                        <div class="d-flex gap-2 mt-2">
                            <!-- Botão para cliente final - Baixar Cotação (sempre visível) -->
                            <button onclick="baixarRecibo(document.getElementById('numeroCotacao').textContent)" 
                                    class="btn btn-outline-success flex-fill">
                                <i class="bi bi-file-pdf me-1"></i> 📄 Baixar Cotação
                            </button>
                            
                            <!-- Botão para funcionários - Imprimir Recibo (só aparece se logado) -->
                            <button id="btnImprimirRecibo" 
                                    onclick="solicitarSenhaImpressao(document.getElementById('numeroCotacao').textContent)" 
                                    class="btn btn-outline-primary flex-fill" 
                                    style="display:none;">
                                <i class="bi bi-printer me-1"></i> 🖨️ Imprimir Recibo
                            </button>
                        </div>
                        
                        <button class="btn btn-outline-danger w-100 mt-2" onclick="limparResultado()">
                            <i class="bi bi-arrow-counterclockwise me-2"></i>
                            Nova Cotação
                        </button>
                    </div>
                </div>
            </div>

            <div class="row mt-4">
                <div class="col-12">
                    <div class="card-shadow">
                        <h6 class="fw-bold mb-2"><i class="bi bi-table text-danger me-2"></i>Tabela de Preços - CAPITAIS</h6>
                        <table class="tabela-precos w-100">
                            <tr><td><strong>Até 1 kg</strong></td><td class="text-end fw-bold text-danger">R$ 24,99</td></tr>
                            <tr><td><strong>Até 5 kg</strong></td><td class="text-end fw-bold text-danger">R$ 49,99</td></tr>
                            <tr><td><strong>Até 10 kg</strong></td><td class="text-end fw-bold text-danger">R$ 79,99</td></tr>
                            <tr><td><strong>Até 20 kg</strong></td><td class="text-end fw-bold text-danger">R$ 149,99</td></tr>
                            <tr><td><strong>Até 30 kg</strong></td><td class="text-end fw-bold text-danger">R$ 229,99</td></tr>
                            <tr><td><strong>Acima de 30 kg</strong></td><td class="text-end fw-bold">Consultar atendente</td></tr>
                        </table>
                        <small class="text-muted">* Para INTERIOR, consulte valores específicos</small>
                    </div>
                </div>
            </div>
        </main>

        <footer class="footer">
            <div class="container">&copy; 2026 JADLOG BRÁS</div>
        </footer>

        <script>
        const ts = Date.now();
        
        // ===== MÁSCARAS =====
        document.getElementById('clienteCpf').addEventListener('input', function(e) {
            let value = this.value.replace(/\\D/g, '');
            if (value.length <= 11) {
                value = value.replace(/(\\d{3})(\\d)/, '$1.$2');
                value = value.replace(/(\\d{3})(\\d)/, '$1.$2');
                value = value.replace(/(\\d{3})(\\d{2})$/, '$1-$2');
            } else {
                value = value.replace(/^(\\d{2})(\\d)/, '$1.$2');
                value = value.replace(/^(\\d{2})\\.(\\d{3})(\\d)/, '$1.$2.$3');
                value = value.replace(/\\.(\\d{3})(\\d)/, '.$1/$2');
                value = value.replace(/(\\d{4})(\\d)/, '$1-$2');
            }
            this.value = value;
        });

        document.getElementById('buscarCliente').addEventListener('input', function(e) {
            let value = this.value.replace(/\\D/g, '');
            if (value.length <= 11) {
                value = value.replace(/(\\d{3})(\\d)/, '$1.$2');
                value = value.replace(/(\\d{3})(\\d)/, '$1.$2');
                value = value.replace(/(\\d{3})(\\d{2})$/, '$1-$2');
            } else {
                value = value.replace(/^(\\d{2})(\\d)/, '$1.$2');
                value = value.replace(/^(\\d{2})\\.(\\d{3})(\\d)/, '$1.$2.$3');
                value = value.replace(/\\.(\\d{3})(\\d)/, '.$1/$2');
                value = value.replace(/(\\d{4})(\\d)/, '$1-$2');
            }
            this.value = value;
        });

        document.getElementById('cepDestino').addEventListener('input', function(e) {
            let value = this.value.replace(/\\D/g, '');
            if (value.length > 5) {
                value = value.substring(0, 5) + '-' + value.substring(5, 8);
            }
            this.value = value;
        });

        // ===== CLIENTES =====
        async function buscarCliente() {
            const cpf = document.getElementById('buscarCliente').value.replace(/\\D/g, '');
            if (!cpf) {
                alert('Digite o CPF ou CNPJ do cliente');
                return;
            }
            if (cpf.length !== 11 && cpf.length !== 14) {
                alert('CPF/CNPJ inválido');
                return;
            }
            const statusDiv = document.getElementById('statusCliente');
            const statusMsg = document.getElementById('statusMensagem');
            statusDiv.style.display = 'block';
            statusMsg.innerHTML = '🔍 Buscando cliente...';
            statusMsg.className = 'text-info';
            try {
                const formData = new URLSearchParams({ cpf_cnpj: cpf });
                const response = await fetch('/api/buscar-cliente', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: formData
                });
                const result = await response.json();
                if (result.success) {
                    const cliente = result.dados;
                    document.getElementById('clienteNomeCarregado').textContent = cliente.nome;
                    document.getElementById('clienteInfoCarregado').textContent = 
                        `${cliente.cidade || ''}${cliente.uf ? '/' + cliente.uf : ''} • ${cliente.telefone || 'Sem telefone'}`;
                    document.getElementById('clienteCarregado').style.display = 'block';
                    document.getElementById('clienteNome').value = cliente.nome;
                    document.getElementById('clienteRazao').value = cliente.razao_social || '';
                    document.getElementById('clienteCpf').value = cliente.cpf_cnpj;
                    document.getElementById('clienteEndereco').value = cliente.endereco || '';
                    document.getElementById('clienteCidade').value = cliente.cidade || '';
                    document.getElementById('clienteUf').value = cliente.uf || '';
                    document.getElementById('clienteCep').value = cliente.cep || '';
                    document.getElementById('clienteTelefone').value = cliente.telefone || '';
                    document.getElementById('formCliente').style.display = 'none';
                    statusMsg.innerHTML = '✅ Cliente encontrado! Dados carregados automaticamente.';
                    statusMsg.className = 'text-success';
                    document.getElementById('clienteDocumento').value = cliente.cpf_cnpj;
                } else {
                    document.getElementById('clienteCarregado').style.display = 'none';
                    document.getElementById('formCliente').style.display = 'block';
                    document.getElementById('clienteCpf').value = cpf;
                    statusMsg.innerHTML = '⚠️ Cliente não encontrado. Faça o cadastro abaixo.';
                    statusMsg.className = 'text-warning';
                }
            } catch (error) {
                statusMsg.innerHTML = '❌ Erro ao buscar cliente. Tente novamente.';
                statusMsg.className = 'text-danger';
            }
        }

        function limparCliente() {
            document.getElementById('buscarCliente').value = '';
            document.getElementById('clienteCarregado').style.display = 'none';
            document.getElementById('formCliente').style.display = 'none';
            document.getElementById('statusCliente').style.display = 'none';
            document.getElementById('clienteNome').value = '';
            document.getElementById('clienteRazao').value = '';
            document.getElementById('clienteCpf').value = '';
            document.getElementById('clienteEndereco').value = '';
            document.getElementById('clienteCidade').value = '';
            document.getElementById('clienteUf').value = '';
            document.getElementById('clienteCep').value = '';
            document.getElementById('clienteTelefone').value = '';
            document.getElementById('clienteDocumento').value = '';
        }

        async function salvarCliente() {
            const cpf = document.getElementById('clienteCpf').value.replace(/\\D/g, '');
            const nome = document.getElementById('clienteNome').value.trim();
            if (!cpf || !nome) {
                alert('CPF/CNPJ e Nome são obrigatórios');
                return;
            }
            const dados = new URLSearchParams({
                cpf_cnpj: cpf,
                nome: nome,
                razao_social: document.getElementById('clienteRazao').value,
                endereco: document.getElementById('clienteEndereco').value,
                cidade: document.getElementById('clienteCidade').value,
                uf: document.getElementById('clienteUf').value,
                cep: document.getElementById('clienteCep').value,
                telefone: document.getElementById('clienteTelefone').value
            });
            try {
                const response = await fetch('/api/salvar-cliente', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: dados
                });
                const result = await response.json();
                if (result.success) {
                    alert('✅ Cliente cadastrado com sucesso!');
                    document.getElementById('buscarCliente').value = cpf;
                    await buscarCliente();
                    document.getElementById('formCliente').style.display = 'none';
                    document.getElementById('clienteNome').value = nome;
                    document.getElementById('clienteDocumento').value = cpf;
                } else {
                    alert('❌ ' + result.message);
                }
            } catch (error) {
                alert('❌ Erro ao salvar cliente');
            }
        }

        // ===== COTAÇÃO =====
        document.getElementById('formSimulador').addEventListener('submit', async function(e) {
            e.preventDefault();
            const btn = document.getElementById('btnCalcular');
            btn.disabled = true;
            btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span> Calculando...';
            const dados = new URLSearchParams({
                cep_destino: document.getElementById('cepDestino').value,
                peso: document.getElementById('peso').value,
                valor_nf: document.getElementById('valorNF').value,
                cliente_nome: document.getElementById('clienteNome').value || 'Cliente não informado',
                cliente_documento: document.getElementById('clienteDocumento').value || ''
            });
            try {
                const response = await fetch('/api/calcular-frete?' + ts, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                    body: dados
                });
                const result = await response.json();
                if (result.success) {
                    document.getElementById('resultadoArea').style.display = 'none';
                    document.getElementById('resultadoDados').style.display = 'block';
                    const d = result.dados;
                    document.getElementById('numeroCotacao').textContent = d.numero_cotacao;
                    document.getElementById('resDestino').textContent = d.destino;
                    document.getElementById('resTipo').textContent = d.tipo;
                    document.getElementById('resPrazo').textContent = d.prazo;
                    document.getElementById('resPeso').textContent = d.peso + ' kg';
                    document.getElementById('resModalidade').textContent = d.modalidade || 'PACKAGE';
                    document.getElementById('resFrete').textContent = 'R$ ' + d.valor_base.toFixed(2);
                    document.getElementById('resSeguro').textContent = 'R$ ' + d.seguro.toFixed(2);
                    document.getElementById('resTotal').textContent = 'R$ ' + d.total.toFixed(2);
                } else {
                    alert('❌ ' + result.message);
                }
            } catch (error) {
                alert('❌ Erro ao calcular frete. Tente novamente.');
            } finally {
                btn.disabled = false;
                btn.innerHTML = '<i class="bi bi-calculator me-2"></i> Calcular Frete';
            }
        });

        function limparResultado() {
            document.getElementById('resultadoArea').style.display = 'block';
            document.getElementById('resultadoDados').style.display = 'none';
            document.getElementById('formSimulador').reset();
        }

        // ===== RECIBO =====
        async function baixarRecibo(numeroCotacao) {
            if (!numeroCotacao || numeroCotacao === 'COT-2026-0001') {
                alert('❌ Faça uma cotação primeiro!');
                return;
            }
            if (!confirm('Deseja baixar a cotação ' + numeroCotacao + '?')) return;
            try {
                const timestamp = Date.now();
                const url = `/api/imprimir-recibo?numero_cotacao=${encodeURIComponent(numeroCotacao)}&_=${timestamp}`;
                const response = await fetch(url, { method: 'GET' });
                const contentType = response.headers.get('content-type');
                if (response.ok && contentType && contentType.includes('application/pdf')) {
                    const blob = await response.blob();
                    const urlBlob = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = urlBlob;
                    a.download = `cotacao_${numeroCotacao}.pdf`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    window.URL.revokeObjectURL(urlBlob);
                    alert('✅ Cotação baixada com sucesso!');
                } else {
                    const text = await response.text();
                    try {
                        const error = JSON.parse(text);
                        alert('❌ ' + (error.message || 'Erro ao baixar cotação'));
                    } catch (e) {
                        alert('❌ Erro ao baixar cotação. Tente novamente.');
                    }
                }
            } catch (error) {
                alert('❌ Erro ao baixar cotação. Verifique sua conexão.');
            }
        }

        async function imprimirRecibo(numeroCotacao) {
            if (!numeroCotacao || numeroCotacao === 'COT-2026-0001') {
                alert('❌ Faça uma cotação primeiro!');
                return;
            }
            try {
                const timestamp = Date.now();
                const url = `/api/imprimir-recibo?numero_cotacao=${encodeURIComponent(numeroCotacao)}&_=${timestamp}`;
                const response = await fetch(url, { method: 'GET' });
                if (response.ok) {
                    const blob = await response.blob();
                    const urlBlob = window.URL.createObjectURL(blob);
                    const printWindow = window.open(urlBlob, '_blank');
                    if (printWindow) {
                        printWindow.onload = function() {
                            setTimeout(function() {
                                printWindow.print();
                            }, 1500);
                        };
                    } else {
                        const a = document.createElement('a');
                        a.href = urlBlob;
                        a.download = `recibo_${numeroCotacao}.pdf`;
                        document.body.appendChild(a);
                        a.click();
                        document.body.removeChild(a);
                        alert('⚠️ Popup bloqueado. O recibo foi baixado.');
                    }
                    setTimeout(() => {
                        window.URL.revokeObjectURL(urlBlob);
                    }, 5000);
                } else {
                    const error = await response.json();
                    alert('❌ ' + (error.message || 'Erro ao imprimir recibo'));
                }
            } catch (error) {
                alert('❌ Erro ao imprimir recibo. Verifique sua conexão.');
            }
        }

        // ===== SISTEMA DE LOGIN =====
        let funcionarioLogado = false;
        const SENHA_FUNCIONARIO = 'jadlog2026';

        function abrirLogin() {
            var modal = new bootstrap.Modal(document.getElementById('loginModal'));
            modal.show();
            document.getElementById('senhaLogin').value = '';
            document.getElementById('senhaLogin').focus();
        }

        function validarLogin() {
            const senha = document.getElementById('senhaLogin').value;
            
            if (senha === SENHA_FUNCIONARIO) {
                funcionarioLogado = true;
                
                document.getElementById('loginButton').style.display = 'none';
                document.getElementById('logoutButton').style.display = 'block';
                
                // Mostra o botão de impressão
                document.getElementById('btnImprimirRecibo').style.display = 'block';
                
                var modal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
                modal.hide();
                
                alert('✅ Login realizado com sucesso! Você pode imprimir recibos agora.');
            } else {
                alert('❌ Senha incorreta! Tente novamente.');
                document.getElementById('senhaLogin').value = '';
                document.getElementById('senhaLogin').focus();
            }
        }

        function logout() {
            funcionarioLogado = false;
            
            document.getElementById('loginButton').style.display = 'block';
            document.getElementById('logoutButton').style.display = 'none';
            
            document.getElementById('btnImprimirRecibo').style.display = 'none';
            
            alert('🔒 Você saiu do modo funcionário.');
        }

        document.getElementById('senhaLogin').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                validarLogin();
            }
        });

        document.getElementById('loginModal').addEventListener('hidden.bs.modal', function() {
            document.getElementById('senhaLogin').value = '';
        });

        // ===== SISTEMA DE SENHA HÍBRIDO (para impressão) =====
        let senhaValidada = false;
        let validadeSenha = null;
        let numeroCotacaoAtual = '';
        const SENHA_IMPRESSAO = 'jadlog2026';
        const VALIDADE_HORAS = 8;

        function validarSenhaImpressao() {
            const senha = document.getElementById('senhaImpressao').value;
            
            if (senha === SENHA_IMPRESSAO) {
                senhaValidada = true;
                validadeSenha = new Date();
                validadeSenha.setHours(validadeSenha.getHours() + VALIDADE_HORAS);
                
                var modal = bootstrap.Modal.getInstance(document.getElementById('senhaModal'));
                modal.hide();
                
                imprimirRecibo(numeroCotacaoAtual);
                
                alert(`✅ Senha validada! Você pode imprimir recibos até as ${validadeSenha.getHours()}:${String(validadeSenha.getMinutes()).padStart(2, '0')}`);
            } else {
                alert('❌ Senha incorreta! Tente novamente.');
                document.getElementById('senhaImpressao').value = '';
                document.getElementById('senhaImpressao').focus();
            }
        }

        function solicitarSenhaImpressao(numeroCotacao) {
            if (!numeroCotacao || numeroCotacao === 'COT-2026-0001') {
                alert('❌ Faça uma cotação primeiro!');
                return;
            }
            
            if (!funcionarioLogado) {
                alert('🔒 Apenas funcionários logados podem imprimir recibos. Faça login no botão "Funcionário".');
                return;
            }
            
            numeroCotacaoAtual = numeroCotacao;
            
            if (senhaValidada && validadeSenha && new Date() < validadeSenha) {
                imprimirRecibo(numeroCotacao);
                return;
            }
            
            var modal = new bootstrap.Modal(document.getElementById('senhaModal'));
            modal.show();
            document.getElementById('senhaImpressao').value = '';
            document.getElementById('senhaImpressao').focus();
        }

        document.getElementById('senhaImpressao').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                validarSenhaImpressao();
            }
        });

        document.getElementById('senhaModal').addEventListener('hidden.bs.modal', function() {
            document.getElementById('senhaImpressao').value = '';
        });

        // ===== DUPLO CLIQUE NO NÚMERO DA COTAÇÃO =====
        document.getElementById('numeroCotacao').addEventListener('dblclick', function() {
            if (funcionarioLogado) {
                alert('🔓 Você já está logado como funcionário. O botão "Imprimir Recibo" já está visível.');
            } else {
                alert('🔒 Área restrita. Faça login no botão "Funcionário" no canto superior direito.');
            }
        });

        // ===== PWA =====
        let deferredPrompt;
        const installBanner = document.getElementById('installBanner');
        const installBtn = document.getElementById('installBtn');
        const closeBannerBtn = document.getElementById('closeBannerBtn');

        window.addEventListener('beforeinstallprompt', (e) => {
            e.preventDefault();
            deferredPrompt = e;
            installBanner.style.display = 'flex';
            console.log('📱 PWA pronto para instalação!');
        });

        installBtn.addEventListener('click', async () => {
            if (deferredPrompt) {
                deferredPrompt.prompt();
                const result = await deferredPrompt.userChoice;
                if (result.outcome === 'accepted') {
                    console.log('✅ App instalado com sucesso!');
                    installBanner.style.display = 'none';
                } else {
                    console.log('❌ Usuário recusou a instalação');
                }
                deferredPrompt = null;
            }
        });

        closeBannerBtn.addEventListener('click', () => {
            installBanner.style.display = 'none';
        });

        window.addEventListener('appinstalled', () => {
            installBanner.style.display = 'none';
            console.log('🎉 App instalado!');
        });

        if (window.matchMedia('(display-mode: standalone)').matches) {
            installBanner.style.display = 'none';
        }

        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/sw.js')
                    .then(function(registration) {
                        console.log('ServiceWorker registrado com sucesso:', registration.scope);
                    })
                    .catch(function(error) {
                        console.log('Falha ao registrar ServiceWorker:', error);
                    });
            });
        }
        </script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """