# Intégration Continue (CI/CD) avec GitHub Actions

---

## 🐳 Objectif

Automatiser le **build** et le **push** de l'image Docker d'un projet vers **Docker Hub**, à chaque `push` sur la branche `main`.

---

## 📁 1. Structure du projet local

```bash
my-app/
├── Dockerfile
├── app.py
└── requirements.txt
```

### `app.py`

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Docker!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

### `requirements.txt`

```
flask
```

### `Dockerfile`

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

---

## 🚀 2. Créer le repo sur GitHub

1. Crée un repo vide sur GitHub, par exemple `username/my-app`.
2. Initialise ton projet local :

```bash
git init
git remote add origin https://github.com/username/my-app.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

## 🔐 3. Créer les secrets GitHub

Va dans ton dépôt GitHub > **Settings** > **Secrets and variables** > **Actions** > **New repository secret**.

Ajoute ces secrets :

* `DOCKER_USERNAME` → ton nom d’utilisateur Docker Hub
* `DOCKER_PASSWORD` → ton mot de passe Docker Hub (ou token d'accès)

---

## ⚙️ 4. Ajouter GitHub Actions

Crée un fichier dans ton projet :

```bash
mkdir -p .github/workflows
touch .github/workflows/docker-image.yml
```

### `.github/workflows/docker-image.yml`

```yaml
name: Build and Push Docker image

on:
  push:
    branches:
      - main

jobs:
  build-and-push:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Log in to Docker Hub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKER_USERNAME }}
        password: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build Docker image
      run: docker build -t ${{ secrets.DOCKER_USERNAME }}/my-app:latest .

    - name: Push Docker image
      run: docker push ${{ secrets.DOCKER_USERNAME }}/my-app:latest
```

---

## ✅ 5. Test final

1. Fais un changement (ex : modifie `hello()`).
2. Fais un commit et pousse :

```bash
git add .
git commit -m "Update message"
git push origin main
```

3. Va dans **Actions** sur GitHub pour suivre le workflow.
4. Va sur ton **Docker Hub** pour vérifier que l’image est bien poussée.

---

## 📦 Résultat

* Image Doker `username/my-app:latest` sera automatiquement construite et poussée à chaque push sur `main`.

