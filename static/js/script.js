/* Soundscapes Conservatory of Music - site scripts.
   Vanilla JavaScript; the only dependency is Bootstrap's bundle, loaded before this file. */
(function () {
    'use strict';

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    /* ------------------------------------------------------------------
       1. Navigation drawer: close it after choosing a same-page anchor link
          (a normal page navigation closes it anyway).
       ------------------------------------------------------------------ */
    var siteNav = document.getElementById('site-nav');
    if (siteNav && window.bootstrap) {
        siteNav.addEventListener('click', function (event) {
            var link = event.target.closest('a[href*="#"]');
            if (!link) { return; }
            var target = new URL(link.href, window.location.href);
            if (target.pathname === window.location.pathname) {
                var drawer = bootstrap.Offcanvas.getInstance(siteNav);
                if (drawer) { drawer.hide(); }
            }
        });
    }

    /* ------------------------------------------------------------------
       2. Hero video: the poster image is always shown first; the video is
          added on every device and loops until the visitor pauses it with
          the visible button. Only prefers-reduced-motion keeps the poster.
       ------------------------------------------------------------------ */
    var heroVideo = document.getElementById('hero-video');
    if (heroVideo && heroVideo.dataset.src) {
        var videoToggle = document.querySelector('[data-video-toggle]');

        var setVideoToggle = function (playing) {
            if (!videoToggle) { return; }
            videoToggle.querySelector('[data-label]').textContent = playing ? 'Pause video' : 'Play video';
            videoToggle.querySelector('[data-icon="pause"]').hidden = !playing;
            videoToggle.querySelector('[data-icon="play"]').hidden = playing;
        };

        if (!reduceMotion.matches) {
            var source = document.createElement('source');
            source.src = heroVideo.dataset.src;
            source.type = 'video/mp4';
            heroVideo.appendChild(source);
            heroVideo.load();

            var playPromise = heroVideo.play();
            if (playPromise && playPromise.catch) {
                playPromise.catch(function () { setVideoToggle(false); });
            }

            if (videoToggle) {
                videoToggle.hidden = false;
                setVideoToggle(true);
                videoToggle.addEventListener('click', function () {
                    if (heroVideo.paused) {
                        heroVideo.play();
                        setVideoToggle(true);
                    } else {
                        heroVideo.pause();
                        setVideoToggle(false);
                    }
                });
            }
        }
    }

    /* ------------------------------------------------------------------
       3. Auto-rotating carousels (testimonials, gallery hero).
          Bootstrap handles slides, controls and arrow keys; this code owns
          the timer so that pausing sticks: the user's Pause button, keyboard
          focus inside the carousel, hovering, a hidden tab, and the
          reduced-motion preference all stop the rotation.
       ------------------------------------------------------------------ */
    var carousels = document.querySelectorAll('[data-carousel-autoplay]');
    Array.prototype.forEach.call(carousels, function (element) {
        if (!window.bootstrap) { return; }
        var interval = parseInt(element.getAttribute('data-carousel-autoplay'), 10) || 6000;
        var carousel = bootstrap.Carousel.getOrCreateInstance(element, { interval: false, ride: false, pause: false });
        var toggle = document.querySelector('[data-carousel-toggle="#' + element.id + '"]');
        var timer = null;
        var userPaused = reduceMotion.matches;

        var renderToggle = function () {
            if (!toggle) { return; }
            toggle.querySelector('[data-label]').textContent = userPaused ? 'Play' : 'Pause';
            toggle.setAttribute('aria-label', userPaused ? 'Start automatic slide show' : 'Pause automatic slide show');
            toggle.querySelector('[data-icon="pause"]').hidden = userPaused;
            toggle.querySelector('[data-icon="play"]').hidden = !userPaused;
        };
        var stop = function () {
            if (timer) { window.clearInterval(timer); timer = null; }
        };
        var start = function () {
            stop();
            if (userPaused) { return; }
            timer = window.setInterval(function () {
                if (!document.hidden) { carousel.next(); }
            }, interval);
        };

        if (toggle) {
            toggle.hidden = false;
            toggle.addEventListener('click', function () {
                userPaused = !userPaused;
                renderToggle();
                if (userPaused) { stop(); } else { start(); }
            });
        }
        element.addEventListener('mouseenter', stop);
        element.addEventListener('mouseleave', start);
        element.addEventListener('focusin', stop);
        element.addEventListener('focusout', function (event) {
            if (!element.contains(event.relatedTarget)) { start(); }
        });
        reduceMotion.addEventListener('change', function (event) {
            if (event.matches) { userPaused = true; renderToggle(); stop(); }
        });

        renderToggle();
        start();
    });

    /* ------------------------------------------------------------------
       4. Faculty cards: pointer users see the bio on hover (CSS); the
          "Read bio" button makes the same content reachable by keyboard,
          touch and assistive technology.
       ------------------------------------------------------------------ */
    var bioToggles = document.querySelectorAll('[data-bio-toggle]');
    Array.prototype.forEach.call(bioToggles, function (button) {
        var card = button.closest('.member');
        if (!card) { return; }
        var setOpen = function (open) {
            card.classList.toggle('is-open', open);
            button.setAttribute('aria-expanded', String(open));
            button.querySelector('[data-label]').textContent = open ? 'Hide bio' : 'Read bio';
        };
        button.addEventListener('click', function () {
            setOpen(!card.classList.contains('is-open'));
        });
        card.addEventListener('keydown', function (event) {
            if (event.key === 'Escape' && card.classList.contains('is-open')) {
                setOpen(false);
                button.focus();
            }
        });
    });

    /* ------------------------------------------------------------------
       5. Gallery lightboxes: arrow keys move between photos, a counter
          shows the position, and each album reopens on its first photo.
       ------------------------------------------------------------------ */
    var lightboxes = document.querySelectorAll('.lightbox');
    Array.prototype.forEach.call(lightboxes, function (modal) {
        var carouselElement = modal.querySelector('.carousel');
        if (!carouselElement || !window.bootstrap) { return; }
        var counter = modal.querySelector('[data-lightbox-counter]');
        var total = carouselElement.querySelectorAll('.carousel-item').length;
        var carousel = function () { return bootstrap.Carousel.getOrCreateInstance(carouselElement); };
        var update = function (index) {
            if (counter) { counter.textContent = (index + 1) + ' / ' + total; }
        };
        carouselElement.addEventListener('slid.bs.carousel', function (event) { update(event.to); });
        modal.addEventListener('keydown', function (event) {
            if (event.key === 'ArrowRight') { carousel().next(); }
            if (event.key === 'ArrowLeft') { carousel().prev(); }
        });
        modal.addEventListener('hidden.bs.modal', function () {
            carousel().to(0);
            update(0);
        });
        update(0);
    });
}());
