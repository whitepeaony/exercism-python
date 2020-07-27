# exercism-python
Exercises from Python track on exercism.io

# Setup
### Install required dependencies  
**(Windows)**
First, get latest PowerShell and scoop - a 3-rd party package manager for Windows. Execute the following in PowerShell:
```PowerShell
iex "& { $(irm https://aka.ms/install-powershell.ps1) } -UseMSI"
iwr -useb get.scoop.sh | iex
```
Then set up scoop, installing some basic packages:
```PowerShell
scoop install aria2
scoop install git-with-openssh 7zip
scoop bucket add extras
scoop update
```
Install any of the packages listed below, which you don't have already:
```PowerShell
scoop install vscode
scoop install windows-terminal
scoop install exercism

scoop install vlc
```
### Clone this repository
to a convenient location, with git:
```bash
git clone https://github.com/whitepeaony/exercism-python.git
cd exercism-python
```
or using GitKraken.
### Install python
```PowerShell
scoop bucket add versions
scoop install python37
pip install pipenv
```
### Add dependencies
In PowerShell:
```PowerShell
cd exercism-python
pipenv shell
pipenv install
```
### Manage dependencies
Install a new package:
```PowerShell
pipenv install my-package
```
Update individual packages or all packages:
```PowerShell
pipenv update --outdated
pipevn update my-package
pipenv update
```
Resolve dependencies and write the current setup to Pipfile.lock for reproducibility.
```
pipenv lock
```PowerShell
In case or errors with pre-release packages (like black):
```PowerShell
pipenv lock --pre
```