# postgresql_docker

sudo nano /etc/hosts
127.0.0.1 postgres

psql -h postgres -U gitpod -d mydatabase

docker cp /workspace/postgresql_docker/persons.csv postgres:/tmp/persons.csv
docker cp /workspace/postgresql_docker/employes.csv postgres:/tmp/employes.csv


sudo mkdir -p /etc/cni/net.d
sudo bash -c 'cat > /etc/cni/net.d/10-mynet.conf <<EOF
{
  "cniVersion": "0.3.1",
  "name": "mynet",
  "type": "bridge",
  "bridge": "cni0",
  "isGateway": true,
  "ipMasq": true,
  "ipam": {
    "type": "host-local",
    "subnet": "10.22.0.0/16",
    "routes": [
      { "dst": "0.0.0.0/0" }
    ]
  }
}
EOF'