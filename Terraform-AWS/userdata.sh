#! /bin/bash
yum update -y
hostnamectl set-hostname project-portfolio-server
yum install -y docker
systemctl start docker
systemctl enable docker
usermod -a -G docker ec2-user
curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" \
-o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
yum install git -y


# Projenin calistirilmasi
# Running the project

docker run --name 3D-Portolio-Project -d -p 80:8080 --rm herraksoy/projects:3D-Portfolio-Website


# pip icin ekstra ayarlamalar   - image saglikli olup olmadigini denemek icin. SOnrasinda ihtiyac degil.
# Extra settings to install pip - to test if the image is healthy. Afterwards it is not needed.

# sudo yum install python3 python3-pip -y
# sudo pip install Flask
# sudo pip install Flask-Mail