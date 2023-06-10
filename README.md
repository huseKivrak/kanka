# kanka

kanka ~~is~~ _will be_ a virtual letter writing and delivery service.

Inspired by traditional correspondence, [kanka](<https://en.wiktionary.org/wiki/kanka#:~:text=kanka%20(definite%20accusative%20kankay%C4%B1%2C%20plural,colloquial)%20bro%2C%20mate%2C%20pal>) (colloquial term for "best buddy" or "dude" in Turkish) combines the charms of epistolary dialogue with the conveniences of digital communication; i.e. no 'waiting in line at the post office'

- delivery time based on distance between users

- letter possession: once you send a letter, it's gone!

- minimal yet highly customizable letter UI

- secure authorization and user privacy protection

## tech

### backend

- **Django**, **Django Rest Framework**
  - Simple JWT, Corsheaders
  - Celery + Celery Beat

### frontend

- **Vite + React + TypeScript**
  - Axios, React Router DOM, Day.js
