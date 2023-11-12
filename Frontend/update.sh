npm run build
cp -r dist/* /var/www/junction/
chown caddy:caddy -R /var/www/junction
