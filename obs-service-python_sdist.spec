#
# spec file for package obs-service-ython_sdist
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define service python_sdist

Name:           obs-service-%{service}
Version:        0.0.2+git.1456307570.6d1c8ca
Release:        0
Summary:        An OBS source service: Generate Python sdists
%if 0%{?mageia}
License:        GPLv2+
Group:          Development/Tools
%else
License:        GPL-2.0+
Group:          Development/Tools/Building
%endif
Url:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
#Requires:       python >= 2.6
Requires:       python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It generates Python source distribution (sdist) tarballs

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 python_sdist %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 python_sdist.service %{buildroot}%{_prefix}/lib/obs/service

%if 0%{?fedora} > 29 || 0%{?centos_ver} >= 7 || 0%{?mageia} >= 8
perl -p -i -e 's{#!.*python}{#!%{_bindir}/python2}' %{buildroot}%{_prefix}/lib/obs/service/python_sdist
%endif

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
