# Scrapper Twitter

Simple scrapper to twitter from a user/word/day

## Crear entorno virtual Windows

```sh
python -m venv <nombre>
```

## Ingresar al entorno virtual Windows

```sh
.\<nombre>\Scripts\activate
```

## Instalar dependencias

```sh
pip install -r requirements.txt
```

## Salir del entorno virtual

```sh
deactivate
```

## Ejecución 

```sh
uvicorn --app-dir=src app:app --reload
```
