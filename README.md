# postgresql_docker

psql -h postgres -U gitpod -d mydatabase

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