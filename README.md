### How to use?

1. git clone <https://github.com/arnoldasr/lab>
2. cd lab/lab3
3. docker compose build
4. docker compose up -d
5. docker exec -it caddy bash
6. caddy hash-password
7. Enter new passwords for your users and replace them in the Caddyfile
8. Rebuild Caddy image and relaunch docker composer


Dont forget to add vhosts to your hosts file