docker build -t kubeapp .
docker run -it -p 9000:9000 --rm --name kubeapp_running kubeapp