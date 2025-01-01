# Utiliser une image de base avec Python et les dépendances nécessaires
FROM python:3.8-slim

# Installer les dépendances nécessaires pour pgAdmin
RUN apt-get update && apt-get install -y \
    git \   
    wget \
    libpq-dev \
    python3-dev \
    && apt-get clean

# Installer pgAdmin
RUN pip install --upgrade pip
RUN pip install flask && pip install pgadmin4

# Configurer pgAdmin pour qu'il puisse être exécuté
RUN mkdir -p /usr/local/lib/python3.8/dist-packages/pgadmin4
WORKDIR /usr/local/lib/python3.8/dist-packages/pgadmin4
RUN wget https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v6.21/pip/pgadmin4-6.21-py3-none-any.whl \
    && pip install pgadmin4-6.21-py3-none-any.whl

# Configurer les variables d'environnement pour pgAdmin
ENV PGADMIN_CONFIG_SERVER_MODE=True
ENV PGADMIN_CONFIG_FILE_PATH=/root/.pgadmin

# Exposer le port 5050
EXPOSE 5050

# Commande par défaut pour démarrer pgAdmin
CMD ["python3", "/usr/local/lib/python3.8/dist-packages/pgadmin4/pgAdmin4.py"]
