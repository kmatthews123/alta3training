#!/bin/bash

echo -e "Cleaning up Containers..."
sudo docker rm john paul george stuart pete ringo &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null

sudo docker stop indy &> /dev/null
sudo docker rm indy &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null

sudo docker stop bender fry zoidberg farnsworth indy &> /dev/null
sudo docker rm bender fry zoidberg farnsworth indy &> /dev/null
sudo docker network rm ansible-net &> /dev/null
rm /tmp/labrunning &> /dev/null
echo -e "Containers Cleared!\n"

echo -e "Assembling Planet Express team...\n"

### Set ARGS
DOCKERFILE=/workspaces/alta3training/docker_stuff/ubuntu/

### Create networks
sudo docker network create --opt com.docker.network.driver.mtu=1450 --subnet 10.10.2.0/24 ansible-net

### Build docker images
sudo docker build -q --build-arg user=bender      --tag bender:22.04          $DOCKERFILE
sudo docker build -q --build-arg user=fry         --tag fry:22.04             $DOCKERFILE
sudo docker build -q --build-arg user=zoidberg    --tag zoidberg:22.04        $DOCKERFILE
sudo docker build -q --build-arg user=indy        --tag indy:22.04            $DOCKERFILE

### Launch containers and connect networks
sudo docker run -d  --name indy        -h indy       --ip 10.10.2.2 --network ansible-net indy:22.04
sudo docker run -d  --name bender      -h bender     --ip 10.10.2.3 --network ansible-net bender:22.04
sudo docker run -d  --name fry         -h fry        --ip 10.10.2.4 --network ansible-net fry:22.04
sudo docker run -d  --name zoidberg    -h zoidberg   --ip 10.10.2.5 --network ansible-net zoidberg:22.04
sudo docker run -d  --name farnsworth  -h farnsworth --ip 10.10.2.6 --network ansible-net registry.gitlab.com/alta3/planetexpress/centos/farnsworth:8

#these two things are installed via the dev container config
#pip3 install ansible
#sudo apt install sshpass -y
#sshpass -p "alta3" ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub bender@10.10.2.3
#sshpass -p "alta3" ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub fry@10.10.2.4
#sshpass -p "alta3" ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub zoidberg@10.10.2.5

# docker version 20.10.25 patch which dockerfile makes home directories root ownership
names=("bender" "fry" "zoidberg")
for name in "${names[@]}"; do
    sudo docker exec -it $name chown -R $name:$name /home/$name
done


#sshpass -palta3 

#ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub -f bender@10.10.2.3
#ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub -f fry@10.10.2.4
#ssh-copy-id -i /workspaces/alta3training/paramikosshrsa/.ssh/id_rsa.pub -f zoidberg@10.10.2.5

#echo -e ".ansible.cfg Updated (/home/student/.ansible.cfg)"
cp /workspaces/alta3training//ansible/docker_stuff/ansible/ansible.cfg ~/.ansible.cfg

#echo -e "Inventory File Updated (/home/student/mycode/inv/dev/hosts)"
#curl https://static.alta3.com/projects/ansible/deploy/hosts --create-dirs -o ~/mycode/inv/dev/hosts

#echo -e "Nethosts Inventory File Updated (/home/student/mycode/inv/dev/nethosts)"
#curl https://static.alta3.com/projects/ansible/deploy/nethosts --create-dirs -o ~/mycode/inv/dev/nethosts

ansible-playbook /workspaces/alta3training/ansible/docker_stuff/ansible/px-acces.yml -i /workspaces/alta3training//ansible/docker_stuff/inv/hosts
