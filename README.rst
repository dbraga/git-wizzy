Git-Wizzy
=========

Overview
========

git-wizzy or wizzy for friends is a simple script that restores files from an internal cache.

Why i need wizzy?

I got bored each time i had commit "fake" configuration files to the git repository such as *.yml configuration files
in a rails project.

I want to be able to restore this files from the fake ones and i want to do it without being forced to merge them.

I want to be able to do it quickly in a snap

That's why I need wizzy, maybe you do it too 

Requirements
============

Git & Python installed on your machine
and magic. a lot of magic.

Installation
============

Copy the wizzy file and the .wizzy-config in the main folder you want to do the magic.
Add this alias to your ``.bashrc`` configuration file: ``echo 'alias wizzy="./wizzy "' >> ~/.bashrc && . ~/.bashrc``


Open your .wizzy-config and type in the files you want to be magic.. check out this .wizzy-config example file::

    ...
	foo_dir/*.yml
	foo_dir/foo.rb

Usage
============

First time you use wizzy you should : ``wizzy install`` and ``wizzy ignore`` so wizzy will automatically generate the cache files and add them on your .gitignore

From now on each time you need to restore the files just type ``wizzy fix`` and you are done. Like magic

If you want to clean the wizzy cache you can type ``wizzy clean``. After that you'll need to ``wizzy install`` again.

If you don't remember a spell just type ``wizzy help``

Support
=======

Please fork it, make it better and make a pull request!
Bug ? Issues ? feel free to use the system tracker!

Authors
=======

This product was mainly developed by *Damiano Braga*

