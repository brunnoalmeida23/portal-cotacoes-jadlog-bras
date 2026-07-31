from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JADLOG BRÁS - Simulador</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
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
            .card-shadow { background: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); padding: 24px; }
            .footer { background: #212529; color: white; padding: 15px 0; margin-top: 40px; text-align: center; }
            .nav-link { color: white !important; }
            .navbar-brand { color: white !important; font-weight: 700; }
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
            <div class="text-center py-5">
                <h1 class="display-4 fw-bold mb-4">Simulador de Fretes</h1>
                <p class="lead mb-4">Cotações rápidas para a unidade Brás - SP</p>
                <a href="/simulador" class="btn btn-jadlog btn-lg">
                    <i class="bi bi-calculator me-2"></i>Fazer Cotação
                </a>
            </div>

            <div class="row mt-5 g-4">
                <div class="col-md-4">
                    <div class="card-shadow text-center">
                        <i class="bi bi-truck fs-1 text-danger"></i>
                        <h5 class="mt-3">Simulador Rápido</h5>
                        <p class="text-muted">Calcule fretes em segundos</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card-shadow text-center">
                        <i class="bi bi-clock-history fs-1 text-danger"></i>
                        <h5 class="mt-3">Histórico</h5>
                        <p class="text-muted">Acompanhe suas cotações</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card-shadow text-center">
                        <i class="bi bi-shield-check fs-1 text-danger"></i>
                        <h5 class="mt-3">Preços Transparentes</h5>
                        <p class="text-muted">Valor base, seguro e total</p>
                    </div>
                </div>
            </div>
        </main>

        <footer class="footer">
            <div class="container">&copy; 2026 JADLOG BRÁS</div>
        </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
        <script>
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
                    
                    var modal = bootstrap.Modal.getInstance(document.getElementById('loginModal'));
                    modal.hide();
                    
                    alert('✅ Login realizado com sucesso!');
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
    </body>
    </html>
    """