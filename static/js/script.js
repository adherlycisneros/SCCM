/* Soundscapes Conservatory of Music - site scripts.
   Vanilla JavaScript; the only dependency is Bootstrap's bundle, loaded before this file. */
(function () {
    'use strict';

    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

    /* ------------------------------------------------------------------
       1. Navigation drawer: a same-page anchor link (the Programs submenu
          while on the Programs page) closes the drawer first and jumps to
          the section only once it has closed. Bootstrap returns focus to the
          menu button when the drawer closes, and the browser scrolls that
          button into view, so jumping earlier would end at the top of the
          page. A normal page navigation closes the drawer by itself.
       ------------------------------------------------------------------ */
    var siteNav = document.getElementById('site-nav');
    if (siteNav && window.bootstrap) {
        siteNav.addEventListener('click', function (event) {
            var link = event.target.closest('a[href*="#"]');
            if (!link) { return; }
            var target = new URL(link.href, window.location.href);
            var drawer = bootstrap.Offcanvas.getInstance(siteNav);
            if (target.pathname !== window.location.pathname || !target.hash || !drawer || !siteNav.classList.contains('show')) { return; }
            event.preventDefault();
            siteNav.addEventListener('hidden.bs.offcanvas', function () {
                var section = document.getElementById(target.hash.slice(1));
                if (window.location.hash === target.hash && section) {
                    section.scrollIntoView();
                } else {
                    window.location.hash = target.hash;
                }
            }, { once: true });
            drawer.hide();
        });
    }

    /* ------------------------------------------------------------------
       2. Hero video: the poster image is always shown first; the video is
          added on every device (a lighter 960px encode below 768px) and
          loops until the visitor pauses it with the visible button. Only
          prefers-reduced-motion keeps the poster.
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
            var smallScreen = window.matchMedia('(max-width: 767.98px), (max-height: 500px)').matches;
            var source = document.createElement('source');
            source.src = (smallScreen && heroVideo.dataset.srcSmall) || heroVideo.dataset.src;
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
       4. Faculty cards: pointer users see the bio by hovering the portrait
          (CSS); the "Read bio" / "Close bio" button reveals the same overlay
          for keyboard, touch and assistive technology. Escape closes an
          opened bio, and also dismisses a hover-revealed one without the
          pointer having to move away (WCAG 1.4.13); the hover works again
          once the pointer has left the portrait.
       ------------------------------------------------------------------ */
    var bioToggles = document.querySelectorAll('[data-bio-toggle]');
    Array.prototype.forEach.call(bioToggles, function (button) {
        var card = button.closest('.member');
        var media = card && card.querySelector('.member__media');
        if (!card) { return; }
        var setOpen = function (open) {
            card.classList.toggle('is-open', open);
            button.setAttribute('aria-expanded', String(open));
            button.querySelector('[data-label]').textContent = open ? 'Close bio' : 'Read bio';
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
        if (media) {
            media.addEventListener('mouseleave', function () {
                card.classList.remove('is-dismissed');
            });
        }
    });
    if (bioToggles.length) {
        document.addEventListener('keydown', function (event) {
            if (event.key !== 'Escape') { return; }
            Array.prototype.forEach.call(document.querySelectorAll('.member__media:hover'), function (media) {
                media.closest('.member').classList.add('is-dismissed');
            });
        });
    }

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

    /* ------------------------------------------------------------------
       6. Programs: mark the section navigator's current entry as the
          reader scrolls between Individual and Group Instruction. The
          observer fires whenever a section crosses a band near the top of
          the viewport; the current entry is then the last section whose
          top has passed that band, and none while the reader is still
          above the first section.
       ------------------------------------------------------------------ */
    var sectionNav = document.querySelector('.section-nav');
    if (sectionNav && 'IntersectionObserver' in window) {
        var navLinks = Array.prototype.slice.call(sectionNav.querySelectorAll('.section-nav__link'));
        var sections = navLinks.map(function (link) {
            return document.getElementById(link.getAttribute('href').slice(1));
        });
        var setCurrent = function (target) {
            navLinks.forEach(function (link, index) {
                if (sections[index] === target) {
                    link.setAttribute('aria-current', 'true');
                } else {
                    link.removeAttribute('aria-current');
                }
            });
        };
        var update = function () {
            var line = window.innerHeight * 0.25;
            var current = null;
            sections.forEach(function (section) {
                if (section && section.getBoundingClientRect().top <= line) { current = section; }
            });
            setCurrent(current);
        };
        var sectionObserver = new IntersectionObserver(update, { rootMargin: '-15% 0px -75% 0px' });
        sections.forEach(function (section) {
            if (section) { sectionObserver.observe(section); }
        });
    }
}());
