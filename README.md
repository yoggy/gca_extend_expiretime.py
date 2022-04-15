# gca_extend_expiretime.py
 
see also...

  - [ARCore Cloud Anchor Management API | Google Developers](https://developers.google.com/ar/develop/cloud-anchors/management-api?hl=en)

```
$ cd ~
$ mkdir work
$ cd work
$ git clone https://github.com/yoggy/gca_extend_expiretime.py.git

$ crontab -e

0 */4 * * * $HOME/work/gca_extend_expiretime/gca_extend_expiretime.py your_credentials.json 2>/dev/null >/dev/null

```

## Copyright and license
Copyright (c) 2022 yoggy

Released under the [MIT license](LICENSE)
