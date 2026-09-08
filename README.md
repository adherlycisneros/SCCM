# Soundscapes Conservatory of Music (SCCM) Website

A responsive, accessible website for a Brooklyn music conservatory, built with Flask and Jinja on the back end and HTML, CSS, Bootstrap 5, and vanilla JavaScript on the front end.

## Description
This website serves as an online hub for the Soundscapes Conservatory of Music students, faculty, parents, and enthusiasts. It offers users detailed information about SCCM's educational programs, faculty, and events. Designed to attract new students and engage current ones, it features a user-friendly interface with integrated multimedia content.

## Features
- Programs display grouped into individual and group instruction
- Testimonials carousel with a pause control
- Faculty profiles with hover and keyboard-accessible bios
- Interactive gallery with album lightboxes (arrow keys, photo counter, focus management)
- Contact form with server-side validation, a honeypot spam trap, and email integration (Flask-Mail)
- Custom 404 page

### Accessibility
- Semantic landmarks, one `h1` per page and a logical heading outline, skip link
- Keyboard-operable offcanvas navigation with the current page marked
- Visible focus styles and WCAG AA colour contrast (the brand coral is used on surfaces; a deeper coral carries text and buttons)
- Carousels and the hero video stop for `prefers-reduced-motion` and can be paused by anyone
- Labelled form fields with per-field error messages and status announcements

### Performance
- Photos are served as web-sized JPEG derivatives with `srcset` and lazy loading
- The hero video (H.264; a 1280px encode, with a lighter 960px encode for small screens) is added by script only when motion is welcome, so visitors who prefer reduced motion get the poster image
- One Bootstrap bundle, an inline SVG icon sprite, and two self-hosted font families (`static/fonts`) loaded with `font-display: swap`

## Technologies Used
- HTML5, CSS3 (custom properties, grid, flexbox), vanilla JavaScript
- Bootstrap 5.3
- Flask 2 / Jinja2, Flask-Mail
- Gunicorn and Docker on Fly.io

## Project Structure
```
app.py                    routes, page data (faculty, programs, albums, testimonials), contact handling
templates/base.html       shared layout: head, header/navigation, footer, scripts
templates/*.html          one template per page plus 404.html
templates/partials/       icons.html (SVG sprite), closing-cta.html (shared call to action)
static/css/styles.css     design tokens, base styles, shared components, page sections
static/js/script.js       navigation drawer, hero video, carousels, faculty bios, lightboxes
static/images, static/videos   optimized media (originals remain in git history before commit 670752d)
```

## Setup Instructions
```bash
git clone https://github.com/adherlycisneros/SCCM.git
cd SCCM
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export MAIL_SUPPRESS_SEND=1   # develop without SMTP credentials
python app.py                 # http://localhost:8080
```

The contact form sends email through Gmail SMTP with an App Password. Set `MAIL_USERNAME`, `MAIL_PASSWORD` and `MAIL_RECIPIENT` as described in `.env.example`; with `MAIL_SUPPRESS_SEND=1` the form flow works locally without sending anything.

## Deployment
The Dockerfile runs the app with Gunicorn, and the GitHub Actions workflow deploys to Fly.io on every push to `main`.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
