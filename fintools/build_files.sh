mkdir -p staticfiles_build/static
python3 manage.py collectstatic --noinput
<<<<<<< HEAD
cp -r static/* staticfiles_build/static/
=======
cp -r static/* staticfiles_build/static/
>>>>>>> 418236a92d054306c454cead7bad69677b7eb3f6
