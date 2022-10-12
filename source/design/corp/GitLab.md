# GitLab

## Installation

- [Ubuntu](https://about.gitlab.com/install/#ubuntu)

Quick Start

```shell
sudo apt-get update
sudo apt-get install -y curl openssh-server ca-certificates tzdata perl

sudo apt-get install -y postfix

curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash
sudo EXTERNAL_URL="https://gitlab.example.com" apt-get install gitlab-ee
```