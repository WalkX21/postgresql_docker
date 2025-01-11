FROM gitpod/workspace-full

# Install PostgreSQL client
RUN sudo apt-get update && \
    sudo apt-get install -y postgresql-client && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/* /tmp/* \
    
    
