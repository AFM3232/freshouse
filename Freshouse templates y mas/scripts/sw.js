const CACHE = 'retiro-v1';
const IMGS = [
  'fotos-dron/dji_fly_20260328_131608_0274_1776158539137_photo.JPG',
  'fotos-dron/dji_fly_20260328_131618_0275_1776158538065_photo.JPG',
  'fotos-dron/dji_fly_20260328_131624_0276_1776158537009_photo.JPG',
  'fotos-dron/dji_fly_20260328_132012_0281_1776158480134_photo.JPG',
  'fotos-dron/dji_fly_20260328_132048_0282_1776158478929_photo.JPG',
  'fotos-dron/dji_fly_20260328_132330_0284_1776158433765_photo.JPG',
  'fotos-dron/dji_fly_20260328_132334_0285_1776158432703_photo.JPG',
  'fotos-dron/dji_fly_20260328_132342_0286_1776158431630_photo.JPG',
  'fotos-dron/dji_fly_20260328_132422_0287_1776158430586_photo.JPG',
  'fotos-dron/dji_fly_20260328_132428_0288_1776158429658_photo.JPG',
  'fotos-dron/dji_fly_20260328_132438_0289_1776158428390_photo.JPG',
  'fotos-dron/dji_fly_20260328_132452_0290_1776158427275_photo.JPG',
  'fotos-dron/dji_fly_20260328_132524_0291_1776158426119_photo.JPG',
  'fotos-dron/dji_fly_20260328_132612_0292_1776158425071_photo.JPG',
  'fotos-dron/dji_fly_20260328_132718_0293_1776158423896_photo.JPG',
  'fotos-dron/dji_fly_20260328_132732_0294_1776158422791_photo.JPG',
  'fotos-dron/dji_fly_20260328_132750_0295_1776158421656_photo.JPG',
  'fotos-dron/dji_fly_20260328_132802_0296_1776158420187_photo.JPG',
  'fotos-dron/dji_fly_20260328_132810_0297_1776158419097_photo.JPG',
  'fotos-dron/dji_fly_20260328_132816_0298_1776158417953_photo.JPG',
  'fotos-dron/dji_fly_20260328_132824_0299_1776158414759_photo.JPG',
  'fotos-dron/dji_fly_20260328_132830_0300_1776158403779_photo.JPG',
  'fotos-dron/dji_fly_20260328_132836_0301_1776158392535_photo.JPG',
  'fotos-dron/dji_fly_20260328_132850_0302_1776158386870_photo.JPG',
  'edificio-retiro.jpg',
  'index.html'
];

// Al instalar: pre-cachear todo
self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(c => c.addAll(IMGS)).then(() => self.skipWaiting())
  );
});

// Al activar: borrar caches viejos
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

// Fetch: cache-first para imágenes, network-first para HTML
self.addEventListener('fetch', e => {
  const url = new URL(e.request.url);
  const isImg = /\.(jpe?g|png|webp|gif)$/i.test(url.pathname);
  if (isImg) {
    e.respondWith(
      caches.match(e.request).then(cached => {
        if (cached) return cached;
        return fetch(e.request).then(res => {
          const clone = res.clone();
          caches.open(CACHE).then(c => c.put(e.request, clone));
          return res;
        });
      })
    );
  }
});
