# Team SKR Website Source
The source code of http://teamskr.rocks, using Flask framwork, contains CTF tools and website source

## CTF Tools Feautures
1. Some Crypto auto decrypt
2. Some stego tools like strings and zsteg
3. RSA public key auto factorize etc
4. Reversing tools
5. Quick python shell etc

## Deploy using Docker
```
cd tworeal
docker build -t skr .
docker run -d --name skr -p 80:80 skr
```
Access the website in http://localhost

## Stop and remove the container
```
docker stop -t 0 skr
docker rm skr
```