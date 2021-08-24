# Pan-Net exercise v 2
## Exercise 0 - environment preparedness (macOS)
### Multipass for running Ubuntu instances
1. Download and install Multipass from [Ubuntu webpage][b4b91157] to run Ubuntu Server VM.
2. Spin-up Ubuntu VM by running following command in terminal `multipass launch --name panet`
3. List running VMs and verify "panet" VM is running by `multipass list`
4. Open a shell on a running instance with: `multipass shell panet` or `multipass exec panet -- lsb_release -a`

### Xcode command line developer tools for running Git
After recent macOS upgrade my Git installation stopped working. I've got following error when trying to run a _Git command_:

`% git status
xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools), missing xcrun at: /Library/Developer/Comman
dLineTools/usr/bin/xcrun`

1. Open terminal and run `xcode-select --install`.
2. Confirm Xcode CLI developer tools installation in the popup window.
3. Wait for the installation to finish (ETA 30 mins).
4. Try running `git status`.
5. Add files into the commit.
6. Add files to be ignored into the .gitignore file.

## Exercise 1
### 1.1 Install and configure Docker

Ansible playbook site.yml is created to:
1. Install Docker service
2. Enable container logging to Docker host's syslog file




  [b4b91157]: https://multipass.run "Multipass - Ubuntu VMs on demand for any workstation"
