# PRACTICA 1 SD

Cluster

## Requisits

Son necesaris Python, Pip i Redis per poder fer la instalació correctament

## Instalació

Utilitza el packet manager [pip](https://pip.pypa.io/en/stable/) per instalar Redis i Flask.

```bash
pip install redis
pip install flask
```

## Ús

Per inicialitzar el serveis, cal utilitzar primerament:

```bash
redis-server
python3 s.py
python3 handler.py
```

Per usar el cluster cal:

```bash
python3 c.py worker --create 2 WORKER
python3 c.py job --wordcount http://localhost:8000/hola1.txt JOB_RUN
```

Primerament creem el nombre de workers que volguem per després trucar al procediment que volem executar sobre el fitxer .txt que volguem executar.

Per últim, per fer multiples execucions, cal:

```bash
python3 c.py worker --create 2 WORKER
python3 c.py job --wordcount http://localhost:8000/hola1.txt --wordcount http://localhost:8000/hola1.txt JOB_RUN
```

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
