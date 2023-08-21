# Instalation
## Befor all please install bind server.
### Installation on ubuntu
```bash
sudo apt install bind9 bind9utils 
```
```bash
git clone https://github.com/amirziaee/dns-maker.git
cd dns-maker
chmod +x dns-maker.py
./dns-maker.py option
cp ./outputs/yourfile-name /etc/bind
```
### Add your file to named-config-default-zone
```bash
sudo vim /etc/bind/named.conf.default-zones

zone "your-zone" {
type master;
file "/etc/bind/your-file-name";
};
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