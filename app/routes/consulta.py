from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/consulta", response_class=HTMLResponse)
async def consulta():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JADLOG BRÁS - Consulta</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            .btn-outline-jadlog { background: transparent; color: #E31E24; border: 2px solid #E31E24; padding: 10px 30px; border-radius: 8px; }
            .btn-outline-jadlog:hover { background: #E31E24; color: white; }
            .card-shadow { background: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); padding: 24px; }
            .footer { background: #212529; color: white; padding: 15px 0; margin-top: 40px; text-align: center; }
            .nav-link { color: white !important; }
            .navbar-brand { color: white !important; font-weight: 700; }
            .resultado-item {
                background: #f8f9fa;
                border-radius: 8px;
                padding: 12px 16px;
                border-left: 4px solid #E31E24;
                margin-bottom: 10px;
                cursor: pointer;
                transition: all 0.2s;
            }
            .resultado-item:hover {
                background: #e9ecef;
                transform: translateX(4px);
                box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            }
            .resultado-item .numero {
                font-weight: 700;
                color: #E31E24;
            }
            .resultado-item .info {
                font-size: 0.9rem;
                color: #6c757d;
            }
            .resultado-item .valor {
                font-weight: 700;
                color: #28a745;
            }
            .badge-status-ok { background: #28a745; color: white; padding: 2px 10px; border-radius: 20px; font-size: 0.7rem; }
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
            .cliente-info {
                background: #d4edda;
                border: 1px solid #c3e6cb;
                border-radius: 8px;
                padding: 12px 16px;
                margin-bottom: 16px;
            }
            .cliente-info .nome {
                font-weight: 700;
                font-size: 1.1rem;
            }
            .cliente-info .doc {
                color: #6c757d;
                font-size: 0.9rem;
            }
            .total-cotacoes {
                font-size: 0.9rem;
                color: #6c757d;
                margin-top: 8px;
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
                        <li class="nav-item"><a class="nav-link" href="/simulador">Simulador</a></li>
                        <li class="nav-item"><a class="nav-link active" href="/consulta">Consulta</a></li>
                        <li class="nav-item" id="loginButton">
                            <button class="btn btn-outline-light btn-sm ms-2" onclick="abrirLogin()">
                                <i class="bi bi-box-arrow-in-right me-1"></i> Login
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
                        <small class="text-muted d-block mt-2">Digite a senha de acesso</small>
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
            <div class="row">
                <div class="col-lg-8 mx-auto">
                    <div class="card-shadow">
                        <h4 class="fw-bold mb-4">
                            <i class="bi bi-search text-danger me-2"></i>
                            Consultar Cotações
                        </h4>
                        
                        <div class="mb-3">
                            <label class="fw-bold">CPF/CNPJ do Cliente</label>
                            <div class="input-group">
                                <span class="input-group-text"><i class="bi bi-credit-card"></i></span>
                                <input type="text" class="form-control" id="buscarDocumento" placeholder="Digite o CPF ou CNPJ" maxlength="18">
                                <button class="btn btn-jadlog" onclick="buscarCotacoes()">
                                    <i class="bi bi-search me-2"></i>Buscar
                                </button>
                                <button class="btn btn-outline-secondary" onclick="limparBusca()">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <small class="text-muted">Digite o CPF ou CNPJ para ver todas as cotações do cliente</small>
                        </div>

                        <div id="resultadoArea" style="display:none;">
                            <div id="clienteInfo" class="cliente-info" style="display:none;">
                                <div class="d-flex justify-content-between align-items-center">
                                    <div>
                                        <span class="nome" id="clienteNome">-</span>
                                        <span class="doc" id="clienteDoc">-</span>
                                    </div>
                                    <span class="badge-status-ok">✅ Cliente encontrado</span>
                                </div>
                                <div class="total-cotacoes" id="totalCotacoes">Total de cotações: 0</div>
                            </div>
                            <div id="listaCotacoes"></div>
                            <div id="nenhumaCotacao" style="display:none;">
                                <div class="text-center text-muted py-4">
                                    <i class="bi bi-inbox fs-1 d-block mb-3"></i>
                                    <p>Nenhuma cotação encontrada para este cliente</p>
                                </div>
                            </div>
                        </div>

                        <div id="loading" style="display:none;" class="text-center py-4">
                            <div class="spinner-border text-danger" role="status">
                                <span class="visually-hidden">Carregando...</span>
                            </div>
                            <p class="mt-2 text-muted">Buscando cotações...</p>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <footer class="footer">
            <div class="container">&copy; 2026 JADLOG BRÁS</div>
        </footer>

        <script>
        // ===== SISTEMA DE LOGIN COM localStorage =====
        const SENHA_FUNCIONARIO = 'jadlog2026';
        const VALIDADE_LOGIN_HORAS = 8;

        function verificarSessao() {
            const loginData = localStorage.getItem('loginData');
            if (loginData) {
                try {
                    const data = JSON.parse(loginData);
                    const agora = new Date().getTime();
                    if (agora < data.expiracao) {
                        // Sessão ainda válida
                        document.getElementById('loginButton').style.display = 'none';
                        document.getElementById('logoutButton').style.display = 'block';
                        return true;
                    } else {
                        localStorage.removeItem('loginData');
                    }
                } catch (e) {
                    localStorage.removeItem('loginData');
                }
            }
            return false;
        }

        function abrirLogin() {
            var modal = new bootstrap.Modal(document.getElementById('loginModal'));
            modal.show();
            document.getElementById('senhaLogin').value = '';
            document.getElementById('senhaLogin').focus();
        }

        function validarLogin() {
            const senha = document.getElementById('senhaLogin').value;
            
            if (senha === SENHA_FUNCIONARIO) {
                // Salvar sessão no localStorage com expiração
                const agora = new Date().getTime();
                const expiracao = agora + (VALIDADE_LOGIN_HORAS * 60 * 60 * 1000);
                localStorage.setItem('loginData', JSON.stringify({
                    expiracao: expiracao
                }));
                
                document.getElementById('loginButton').style.display = 'none';
                document.getElementById('logoutButton').style.display = 'block';
                
                var modal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
                modal.hide();
                
                alert('✅ Login realizado com sucesso! Você permanecerá logado por 8 horas.');
            } else {
                alert('❌ Senha incorreta! Tente novamente.');
                document.getElementById('senhaLogin').value = '';
                document.getElementById('senhaLogin').focus();
            }
        }

        function logout() {
            localStorage.removeItem('loginData');
            
            document.getElementById('loginButton').style.display = 'block';
            document.getElementById('logoutButton').style.display = 'none';
            
            alert('🔒 Você saiu do modo restrito.');
        }

        document.getElementById('senhaLogin').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                validarLogin();
            }
        });

        document.getElementById('loginModal').addEventListener('hidden.bs.modal', function() {
            document.getElementById('senhaLogin').value = '';
        });

        // Verificar sessão ao carregar a página
        window.addEventListener('load', function() {
            verificarSessao();
        });

        // ===== MÁSCARA CPF/CNPJ =====
        document.getElementById('buscarDocumento').addEventListener('input', function(e) {
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

        document.getElementById('buscarDocumento').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') buscarCotacoes();
        });

        // ===== BUSCAR COTAÇÕES =====
        async function buscarCotacoes() {
            const documento = document.getElementById('buscarDocumento').value.trim();
            if (!documento) {
                alert('Digite o CPF ou CNPJ do cliente');
                return;
            }
            document.getElementById('resultadoArea').style.display = 'none';
            document.getElementById('listaCotacoes').innerHTML = '';
            document.getElementById('nenhumaCotacao').style.display = 'none';
            document.getElementById('loading').style.display = 'block';
            const cpfLimpo = documento.replace(/\\D/g, '');
            const url = `/api/buscar-cotacao?documento=${encodeURIComponent(cpfLimpo)}`;
            try {
                const response = await fetch(url);
                const result = await response.json();
                document.getElementById('loading').style.display = 'none';
                if (result.success && result.dados) {
                    const dados = Array.isArray(result.dados) ? result.dados : [result.dados];
                    if (dados.length === 0 || (dados.length === 1 && !dados[0].numero_cotacao)) {
                        document.getElementById('resultadoArea').style.display = 'block';
                        document.getElementById('nenhumaCotacao').style.display = 'block';
                        document.getElementById('clienteInfo').style.display = 'none';
                        return;
                    }
                    const primeiro = dados[0];
                    document.getElementById('clienteNome').textContent = primeiro.cliente_nome || 'NÃO INFORMADO';
                    document.getElementById('clienteDoc').textContent = primeiro.cliente_documento || '';
                    document.getElementById('totalCotacoes').textContent = `Total de cotações: ${dados.length}`;
                    document.getElementById('clienteInfo').style.display = 'block';
                    
                    let html = '';
                    dados.forEach((d) => {
                        const data = d.data_criacao ? new Date(d.data_criacao).toLocaleString('pt-BR') : 'Data não informada';
                        const destino = (d.cidade || '') + '/' + (d.uf || '');
                        const valor = d.total || d.frete || 0;
                        html += `
                            <div class="resultado-item" onclick="verDetalhe('${d.numero_cotacao}')">
                                <div class="d-flex justify-content-between align-items-center">
                                    <div>
                                        <span class="numero">${d.numero_cotacao || 'N/A'}</span>
                                        <span class="info ms-3">
                                            <i class="bi bi-calendar3 me-1"></i>${data}
                                        </span>
                                    </div>
                                    <span class="valor">R$ ${valor.toFixed(2)}</span>
                                </div>
                                <div class="info mt-1">
                                    <i class="bi bi-geo-alt me-1"></i>${destino || 'Destino não informado'}
                                    <span class="ms-3">
                                        <i class="bi bi-weight-scale me-1"></i>${d.peso || 0} kg
                                    </span>
                                </div>
                            </div>
                        `;
                    });
                    document.getElementById('listaCotacoes').innerHTML = html;
                    document.getElementById('resultadoArea').style.display = 'block';
                    document.getElementById('nenhumaCotacao').style.display = 'none';
                } else {
                    document.getElementById('resultadoArea').style.display = 'block';
                    document.getElementById('nenhumaCotacao').style.display = 'block';
                    document.getElementById('clienteInfo').style.display = 'none';
                }
            } catch (error) {
                document.getElementById('loading').style.display = 'none';
                alert('❌ Erro ao buscar cotações. Verifique sua conexão.');
                console.error('Erro:', error);
            }
        }

        function limparBusca() {
            document.getElementById('buscarDocumento').value = '';
            document.getElementById('resultadoArea').style.display = 'none';
            document.getElementById('listaCotacoes').innerHTML = '';
            document.getElementById('nenhumaCotacao').style.display = 'none';
            document.getElementById('clienteInfo').style.display = 'none';
            document.getElementById('loading').style.display = 'none';
        }

        function verDetalhe(numeroCotacao) {
            if (!numeroCotacao) return;
            window.location.href = `/consulta?numero=${numeroCotacao}`;
        }

        window.addEventListener('load', function() {
            const urlParams = new URLSearchParams(window.location.search);
            const numero = urlParams.get('numero');
            if (numero) {
                const campoNumero = document.getElementById('buscarNumero');
                if (campoNumero) {
                    campoNumero.value = numero;
                    buscarCotacao();
                }
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