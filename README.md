# django-kubernetes-azure
Django project Deployment on Azure Container Machine using Kubernetes as orchestration Tool.

### Preliminary steps

- Clone this repo source code :

 ```
 https://github.com/inforian/django-kubernetes-azure.git
 ```
 
- Run python manage.py runserver , and visit Browser you will see pink theme Template.

### Publish Docker Containers

- Install [Docker](https://docs.docker.com/engine/installation/)


- Build docker image for pink theme :
 
  ```docker
  docker build -t dj:pink . ## (assuming you are inside django project)
  ```
  
- Now , Build Image for Orange theme BUt before that edit template index.html
  and copy paste below code inside `<head>` tag.
  
  ```html
    <style>
        #banner {
            background-color: #ffa500;
        }
    </style>
  ```
  
- Refresh Django dev server url you will see ornage theme.
- Build image for Orange theme
```docker
docker build -t dj:orange .
```
  
- Check your iamges : 
  ```docker
    docker images | grep dj 
  ```
  
 - Now Login to you docker hub Account and push this image to docker-hub: 
 ```docker
    docker login
    
    # for orange
     docker tag {image_id} {docker_hub_username}/dj:orange
    
    # for pink
     docker tag {image_id} {docker_hub_username}/dj:pink
```
 
### Azure
 - Create a Resource on Azure, You have to choose Azure Container service from Azure portal from their
  you can choose any `kubernetes` as orchestration type.
  
![containers microsoft azure](https://cloud.githubusercontent.com/assets/15274390/26521350/41e9c5d4-4304-11e7-8a3d-96eb88e20a47.png)
  
 - After your Machine is up and Running connect with you `Master VM` via `SSh` 
 
![master_k8s](https://i.stack.imgur.com/QtWnG.png)

- Copy files from `kubernetes_config` to `Master VM` 

- You must have 3 files on `Master VM`
    - rc-orange.yaml
    - rc-pink.yaml
    - service.yaml

### Kubernetes

- Create replication controller for pink theme (I have created only one rc so only one pod will be created): 
```
kubectl create -f rc-pink.yaml
```
-  

- Create service with :
```
 kubectl create -f service.yaml 
```

- List your service to check status (Wait for some time till external ip assigned to your service) : 

```
kubectl get service | grep my-dj-app
```

- If external ip is assigned to your service then visit app url which will be like:
```
http://{external-ip}:8000  # you will see pink theme
```

### Play with Kubernetes and see its Magic :

- Now create replication controller for orange theme, I have created 3 `Rc's` here :
```
kubectl create -f rc-orange.yaml
```

- Check newly created `RC` and wait for it un-till it is ready with : 
 ```
 kubectl get rc | grep dj-orange
```

- Note : No new service will be craeted here but we have bind orange-theme `RC`
with already existing Service (which craeted above).

- Refresh web url(refresh it every other second by pressing f5) , you will see web theme is switching 
from pink to orange and vice-versa on every refresh or some time remain as it was before.

- Now we will Scale down pink theme replica to `0` , visit web url now only orange theme will work 
```
kubectl scale rc/dj-pink --replicas=0
```

- Scale up Pink theme `RC` again to `1` and - orange to `0` 
```
kubectl scale rc/dj-pink --replicas=1

kubectl scale rc/dj-orange --replicas=0
```
- Now only pink theme will work, this way you can easily roll out 
your new version of site, or we you want to scale you `RC's` according to traffic 
on your sites's , you can scale them using above commands.

