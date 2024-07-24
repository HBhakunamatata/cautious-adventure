# Integration Test

# Deployment

## 2.1 SSH

```shell
ssh root@[server ip address]

exit
```

### 2.1.1 SSH Keys

```shell
ssh-keygen

ssh -i /tmp/id_rsa root@[server_ip_address]

ssh-keygen -p -f /tmp/id_rsa
```



## 2.2 Software Installation

```shell
apt update && apt -y upgrade

apt-cache search apache

apt show apache2

apt install nginx
```

## 2.3 Setting up the system locale

1. Open the file /etc/locale.gen in an editor and make sure the line that begins with “en_US.UTF-8” is uncommented.
2. Enter the command locale-gen; this will (re)generate the locales.
3. Open the file /etc/default/locale in an editor, and make sure it contains the line LANG=en_US.UTF-8. Changes in this file require logout and login to take effect.

To check that everything is right, do this:
1. Enter the command locale; everything (except, possibly, LANGUAGE and LC_ALL) should have the value “en_US.UTF-8”.
2. Enter the command perl -e ''; it should do nothing and give no message.

## 2.4 Quickly starting Django on a server




### 2.1 Learning Nginx and Deploy in Ubuntu

### 2.2 Learning Deploy Django Project in Ubuntu

### 2.3 Deploy MySQL in Ubuntu