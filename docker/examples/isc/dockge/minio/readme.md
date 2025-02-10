# Run dockge
`curl "https://dockge.kuma.pet/compose.yaml?port=5001&stacksPath=/home/simon/Documents/Geek/docker_engine/dockge_minio" --output compose.yaml`

# Lancer un conteneur docker qui lance minio

- https://hub.docker.com/r/minio/minio
- `mkdir test`

```
docker run -d --name minio \
    -p 9000:9000 \
    -p 9001:9001 \
    -e MINIO_ROOT_USER=admin \
    -e MINIO_ROOT_PASSWORD=admin123 \
    -v /home/simon/Documents/Geek/docker_engine/dockge_minio/test:/data \
    minio/minio server /data --console-address ":9001"
```

- port 9000 : api S3 reply here
- port 9001 : web server to manage minio

- Create access keys !


# Env python
- create python venv with vscode
`pip install boto3`