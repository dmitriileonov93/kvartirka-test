FROM python:3.9
COPY ./ /app
RUN python3 -m pip install --upgrade pip && \
    pip install -r /app/requirements.txt
WORKDIR /app/kvartirka_test/
CMD python3 manage.py migrate && \
    python3 manage.py loaddata dampdata.json && \
    python3 manage.py collectstatic --noinput && \
    gunicorn kvartirka_test.wsgi:application --bind 0:8000