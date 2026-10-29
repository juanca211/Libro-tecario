
# Libro-tecario

Proyecto web desarrollado en equipo, con backend en Python y Flask y frontend en HTML, CSS y JavaScript.

## Requisitos

- Git
- Python 3.14 o una versión compatible con las dependencias del proyecto
- Visual Studio Code (recomendado)

## Instalación en Windows

### 1. Clonar el repositorio

```powershell
git clone URL_DEL_REPOSITORIO
cd Libro-tecario
```

Reemplaza `URL_DEL_REPOSITORIO` por la URL HTTPS real de GitHub.

### 2. Crear y activar el entorno virtual

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```powershell
python -m pip install -r backend/requirements.txt
```

### 4. Ejecutar el backend

```powershell
python backend/app.py
```

Abre http://127.0.0.1:5000 para acceder al backend.

La ruta http://127.0.0.1:5000/api/health permite comprobar su estado.

## Estructura del proyecto

```text
Libro-tecario/
├── backend/
│   ├── app.py
│   ├── schema.sql
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── .gitignore
└── README.md
```

## Convenciones de Git

- `main`: versiones estables del proyecto.
- `develop`: integración de funcionalidades.
- `feature/nombre-tarea`: desarrollo de nuevas funcionalidades.

Crear una rama para cada tarea a partir de `develop`:

```powershell
git switch develop
git switch -c feature/nombre-tarea
```

Guardar cambios:

```powershell
git add .
git commit -m "feat: descripcion del cambio"
git push -u origin feature/nombre-tarea
```

Las funcionalidades se integran en `develop` mediante Pull Requests. Los cambios de `develop` se pasan a `main` cuando estén revisados y listos para una versión estable.

## Reglas del equipo

- No subir el entorno virtual `.venv`.
- No subir contraseñas, claves privadas ni archivos `.env`.
- Mantener actualizado `requirements.txt` cuando cambien las dependencias.
- Usar nombres de ramas descriptivos.
- Revisar los cambios antes de integrarlos.
- Cada integrante debe crear su propio entorno virtual local.
