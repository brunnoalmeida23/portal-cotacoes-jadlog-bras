// ==========================================
// SERVICE WORKER - JADLOG BRÁS
// ==========================================

// ===== VERSÃO (MUDE QUANDO ATUALIZAR) =====
const CACHE_VERSION = 'v1.0.2';  // ← AUMENTE SEMPRE QUE ATUALIZAR
const CACHE_NAME = `jadlog-bras-${CACHE_VERSION}`;

// ===== ARQUIVOS PARA CACHEAR =====
const urlsToCache = [
  '/',
  '/simulador',
  '/consulta',
  '/manifest.json',
  '/icons/launchericon-192x192.png',
  '/static/img/logo-jadlog.png',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css',
  'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js'
];

// ==========================================
// INSTALAÇÃO
// ==========================================
self.addEventListener('install', event => {
  console.log(`🔧 Service Worker instalando: ${CACHE_NAME}`);
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('📦 Cache aberto, adicionando arquivos...');
        return cache.addAll(urlsToCache);
      })
      .then(() => {
        console.log('✅ Arquivos cacheados com sucesso!');
        // Força o Service Worker a ativar imediatamente
        return self.skipWaiting();
      })
      .catch(err => {
        console.error('❌ Erro ao adicionar ao cache:', err);
      })
  );
});

// ==========================================
// ATIVAÇÃO
// ==========================================
self.addEventListener('activate', event => {
  console.log(`🔧 Service Worker ativando: ${CACHE_NAME}`);
  
  const cacheWhitelist = [CACHE_NAME];
  
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheWhitelist.indexOf(cacheName) === -1) {
            console.log(`🗑️ Removendo cache antigo: ${cacheName}`);
            return caches.delete(cacheName);
          }
        })
      );
    })
    .then(() => {
      console.log('✅ Cache antigo removido!');
      // Toma controle das páginas abertas
      return self.clients.claim();
    })
  );
});

// ==========================================
// INTERCEPTAÇÃO DE REQUISIÇÕES
// ==========================================
self.addEventListener('fetch', event => {
  // Ignora requisições para APIs (não cachear)
  if (event.request.url.includes('/api/')) {
    event.respondWith(fetch(event.request));
    return;
  }
  
  // Ignora requisições para arquivos estáticos com ? (para não cachear versões)
  if (event.request.url.includes('?_=') || event.request.url.includes('&_=')) {
    event.respondWith(fetch(event.request));
    return;
  }
  
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        if (response) {
          // Retorna do cache
          return response;
        }
        
        // Se não estiver no cache, busca da rede
        return fetch(event.request)
          .then(response => {
            // Verifica se é uma resposta válida
            if (!response || response.status !== 200 || response.type !== 'basic') {
              return response;
            }
            
            // Clona a resposta para cachear
            const responseToCache = response.clone();
            
            caches.open(CACHE_NAME)
              .then(cache => {
                cache.put(event.request, responseToCache);
              });
            
            return response;
          });
      })
      .catch(() => {
        // Fallback para quando offline
        return new Response('Offline - Tente novamente mais tarde', {
          status: 503,
          statusText: 'Service Unavailable'
        });
      })
  );
});

// ==========================================
// MENSAGENS DO CLIENTE (para forçar atualização)
// ==========================================
self.addEventListener('message', event => {
  if (event.data === 'skipWaiting') {
    console.log('⏭️ Pulando espera e ativando novo Service Worker');
    self.skipWaiting();
  }
  
  if (event.data === 'forceUpdate') {
    console.log('🔄 Forçando atualização do cache...');
    caches.delete(CACHE_NAME).then(() => {
      console.log('✅ Cache removido, recarregando...');
      // Notifica o cliente para recarregar
      event.ports[0].postMessage('reload');
    });
  }
});