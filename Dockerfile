FROM python:3.7
RUN apt-get update
RUN apt-get install -y rubygems build-essential libmpc-dev sagemath
RUN gem install zsteg --no-ri --no-rdoc 
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN wget https://packages.microsoft.com/config/debian/10/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN apt-get install -y apt-transport-https
RUN apt-get update
RUN apt-get install -y dotnet-sdk-2.1 nano
RUN mkdir /2real
COPY ./ /2real
WORKDIR /2real
RUN chmod +x setup.sh
ENTRYPOINT ./setup.sh
