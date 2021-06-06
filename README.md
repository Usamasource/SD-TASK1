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

```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)