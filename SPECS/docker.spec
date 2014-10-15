Name:           docker
Version:        1.2.0
Release:        1.vp%{?dist}
Summary:        Automates deployment of containerized applications
License:        ASL 2.0
Group:          System Environment/Daemons
URL:            http://www.docker.com
ExclusiveArch:  x86_64
Source0:        https://get.docker.io/builds/Linux/x86_64/docker-latest.tgz
Source1:        %{name}.service
Source2:        %{name}.socket
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  systemd-units
Requires:       systemd

%description
Docker is an open-source engine that automates the deployment of any
application as a lightweight, portable, self-sufficient container that will
run virtually anywhere.

Docker containers can encapsulate any payload, and will run consistently on
and between virtually any server. The same container that a developer builds
and tests on a laptop will run at scale, in production*, on VMs, bare-metal
servers, OpenStack clusters, public instances, or combinations of the above.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_bindir}
cp usr/local/bin/docker %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/sysconfig
cp %{_sourcedir}/%{name}.sysconfig %{buildroot}/%{_sysconfdir}/sysconfig/%{name}
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}
mkdir -p %{buildroot}/%{_unitdir}
cp %{_sourcedir}/%{name}.service %{buildroot}/%{_unitdir}/
cp %{_sourcedir}/%{name}.socket %{buildroot}/%{_unitdir}/

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sysconfdir}/sysconfig/%{name}
%{_sharedstatedir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%attr(755, root, root) %{_bindir}/docker

%doc



%changelog
