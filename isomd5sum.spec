Name:      isomd5sum
Version:   1.2.3
Release:   4
Epoch:     1
Summary:   Utilities for working with md5sum implanted in ISO images
License:   GPLv2+
URL:       https://github.com/rhinstaller/isomd5sum
Source0:   https://github.com/rhinstaller/%{name}/archive/%{version}.tar.gz

%global common_description %{expand:
isomd5sum provides a way of making use of the ISO9660 application data
area to store md5sum data about the iso.  This allows you to check the
iso given nothing more than the iso itself.}

BuildRequires: gcc popt-devel python2-devel python3-devel

%description
%{common_description}

%package devel
Summary: Development headers and library for using isomd5sum
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}-static = %{epoch}:%{version}-%{release}

%description devel
Development headers and libraries for %{name}

%package -n python2-isomd5sum
Summary: Python2 bindings for isomd5sum
%{?python_provide:%python_provide python2-isomd5sum}

%description -n python2-isomd5sum
%{common_description}

%package -n python3-isomd5sum
Summary: Python3 bindings for isomd5sum
%{?python_provide:%python_provide python3-isomd5sum}

%description -n python3-isomd5sum
%{common_description}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"; export CFLAGS
LDFLAGS="$RPM_LD_FLAGS"; export LDFLAGS

PYTHON=%{__python2} make checkisomd5 implantisomd5 pyisomd5sum.so

pushd %{py3dir}
PYTHON=%{__python3} make checkisomd5 implantisomd5 pyisomd5sum.so
popd

%install
PYTHON=%{__python2} make DESTDIR=%{buildroot} install-bin install-devel install-python

pushd %{py3dir}
PYTHON=%{__python3} make DESTDIR=%{buildroot} install-bin install-devel install-python
popd

%pre

%preun

%post

%postun

%files
%license COPYING
%{_bindir}/*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_datadir}/pkgconfig/isomd5sum.pc

%files -n python2-isomd5sum
%{python2_sitearch}/*.so

%files -n python3-isomd5sum
%{python3_sitearch}/*.so

%files help
%{_mandir}/man1/*

%changelog
* Mon Oct 14 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:1.2.3-4
- Package init
