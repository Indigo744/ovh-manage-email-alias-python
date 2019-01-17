# ovh-manage-email-redirection-python

Manage your email aliases using the OVH API with Python.

## Prerequesite

Here what you'll need:

* Python 3 (tested with 3.7.1)
* OVH Python module: https://github.com/ovh/python-ovh

  `pip install ovh`

* Slugify Python module: https://github.com/un33k/python-slugify

  `pip install python-slugify`

* tldextract Python module: https://github.com/john-kurkowski/tldextract

  `pip install tldextract`

## Configuration

### OVH conf

Rename `ovh.default.conf` to `ovh.conf` and get your keys from [https://eu.api.ovh.com/createToken/](https://eu.api.ovh.com/createToken/).

Note that this is for EU only. See [others endpoints here](https://github.com/ovh/python-ovh#supported-apis).

### Module conf

Rename `config.default.py` to `config.py` and set your domain and your private email.

## Running the scripts

### Add an alias

The following command line will add an alias `github@mydomain.com` (e.g. for creating an alias for Github)

`python ovh_mail_alias_add.py https://github.com/Indigo744/ovh-manage-email-alias-python`

```
Create email alias:
From : github@mydomain.com
To   : my-private-email@pm.me

Continue (ENTER or CTRL+C to cancel)?

Alias created (ID=123456789)
```

Calling the script without any parameter will ask for your input.

### Remove an alias

The following command line will remove the alias we created just before

`python ovh_mail_alias_rm.py 123456789`

```
Delete the following alias:
ID    : 123456789
From  : github@mydomain.com
To    : my-private-email@pm.me

Continue (ENTER or CTRL+C to cancel)?

Deleting...
Alias deleted!
```

### List all aliases

The following command line will list all the aliases.

`python ovh_mail_alias_ls.py`

```
ID      From    To
123456789     my-private-email@pm.me     github@mydomain.com
123545619     my-private-email@pm.me     youtube@mydomain.com
351493542     my-private-email@pm.me     ovh@mydomain.com
```

It procudes a TSV file (Tab-Separated File).

You can redirect the output to a file in order to open it in Excel or Calc.

`python ovh_mail_alias_ls.py > list.tsv`
