const CACHE_NAME = 'merit-cbt-v1';

// Files to cache for offline use
const STATIC_ASSETS = [
  '/',
  '/dashboard',
  '/static/css/style.css',
  '/static/css/exam.css',
  '/static/js/main.js',
  '/static/manifest.json',
  '/static/icons/icon-192x192.png',
  '/static/icons/icon-512x512.png'
];

// ─── Install: cache static assets ───────────────────────────────────────────
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      console.log('[SW] Caching static assets');
      return cache.addAll(STATIC_ASSETS);
    })
  );
  self.skipWaiting();
});

// ─── Activate: remove old caches ────────────────────────────────────────────
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(
        keys
          .filter(key => key !== CACHE_NAME)
          .map(key => {
            console.log('[SW] Deleting old cache:', key);
            return caches.delete(key);
          })
      )
    )
  );
  self.clients.claim();
});

// ─── Fetch: Network-first for exam routes, Cache-first for static ────────────
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Always go to network for exam taking/submission (must be live)
  const networkOnlyPaths = ['/exam/', '/api/', '/login', '/register', '/logout'];
  const isNetworkOnly = networkOnlyPaths.some(path => url.pathname.startsWith(path));

  if (isNetworkOnly) {
    event.respondWith(
      fetch(event.request).catch(() =>
        caches.match('/') // fallback to homepage if offline
      )
    );
    return;
  }

  // Cache-first for static files (CSS, JS, images)
  if (url.pathname.startsWith('/static/')) {
    event.respondWith(
      caches.match(event.request).then(cached => {
        return cached || fetch(event.request).then(response => {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
          return response;
        });
      })
    );
    return;
  }

  // Network-first for everything else (dashboard, profile, etc.)
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
