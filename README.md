# Instalation
## Befor all please install bind server.
### installation on ubuntu
```bash
sudo apt install bind9 bind9utils 
```
```bash
git clone https://github.com/amirziaee/dns-maker.git
cd dns-maker
chmod +x dns-maker.py
./dns-maker.py option
```
## Tables

| Option | Description |
| ------ | ----------- |
| zone   | start to create zone file|
| rev-zone | start to create reverse zone file |

## Example

```bash
./dns-maker.py zone
```
or

```bash
./dns-maker.py rev-zone
```