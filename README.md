RPM Spec for Docker
======================

Tries to follow the [packaging guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines) from Fedora.

* Binary: `/usr/bin/docker`
* Sysconfig: `/etc/sysconfig/dcoker`

To Build
---------

To build the RPM (non-root user):

1. Check out this repo
2. Install rpmdevtools and mock 

    ```
    sudo yum install rpmdevtools mock
    ```
3. Set up your rpmbuild directory tree

    ```
    rpmdev-setuptree
    ```
4. Link the spec file and sources from the repository into your rpmbuild/SOURCES directory

    ```
    ln -s ${repo}/SPECS/docker.spec rpmbuild/SPECS/
    ln -s ${repo}/SOURCES/* rpmbuild/SOURCES/
    ```
5. Download remote source files

    ```
    spectool -g -R rpmbuild/SPECS/docker.spec
    ```
6. Build the RPM

    ```
    rpmbuild -ba rpmbuild/SPECS/docker.spec
    ```

7. (Optional) Build for another Fedora release

    ```
    sudo mock -r fedora-19-x86_64 --resultdir rpmbuild/RPMS/x86_64/ rpmbuild/SRPMS/docker-1.2.0-1.fc20.src.rpm 
    ```

To run
---------------

1. Install the rpm
2. systemctl start docker

More info
---------
See the [docker.com](http://www.docker.com) website.
