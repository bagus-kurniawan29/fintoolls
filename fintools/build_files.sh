mkdir -p staticfiles_build/static
python3 manage.py collectstatic --noinput
cp -r static/* staticfiles_build/static/