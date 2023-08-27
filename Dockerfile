FROM python:alpine3.18
#pour remplir le fichier de configuration pour faire fonctionner le fichier python
# il faut recuperer l'id de votre enregistrement dns. Pour cela il faut lister les enregistrement afin de le recuperer 

# pour utiliser l image voici le docker run , n'oubliez pas de changer /mon/chemin/vers/maconfig/config.json
#sudo docker run --name ddns -it -v /mon/chemin/vers/maconfig/config.json:/usr/src/app/config.json cloudflareddns:latest

LABEL version="1.1" 
LABEL maintainer="Alex Wattier <alex@awattier.be>"
LABEL description="nommer l image cloudflareddns pour que le docker run fonctionne"
WORKDIR /usr/src/app
RUN pip install requests
ADD cloudflareddns.py .

CMD [ "python", "./cloudflareddns.py" ]


