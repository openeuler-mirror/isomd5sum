Name:      isomd5sum
Version:   1.2.3
Release:   5
Epoch:     1
Summary:   Utilities for working with md5sum implanted in ISO images
License:   GPLv2+
URL:       https://github.com/rhinstaller/isomd5sum
Source0:   https://github.com/rhinstaller/%{name}/archive/%{version}.tar.gz

%global common_description %{expand:
isomd5sum provides a way of making use of the ISO9660 application data
area to store md5sum data about the iso.  This allows you to check the
iso given nothing more than the iso itself.}

BuildRequires: gcc popt-devel  python3-devel

%description
%{common_description}

%package devel
Summary: Development headers and library for using isomd5sum
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}-static = %{epoch}:%{version}-%{release}

%description devel
Development headers and libraries for %{name}

%package -n python3-isomd5sum
Summary: Python3 bindings for isomd5sum
%{?python_provide:%python_provide python3-isomd5sum}

%description -n python3-isomd5sum
%{common_description}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"; export CFLAGS
LDFLAGS="$RPM_LD_FLAGS"; export LDFLAGS

PYTHON=%{__python3} make checkisomd5 implantisomd5 pyisomd5sum.so

%install
PYTHON=%{__python3} make DESTDIR=%{buildroot} install-bin install-devel install-python

%pre

%preun

%post

%postun

%files
%license COPYING
%{_bindir}/*

%files devel
%{_includedir}/*.h
%ifnarch riscv64
%{_libdir}/*.a
%else
%{_prefix}/lib/*.a
%endif
%{_datadir}/pkgconfig/isomd5sum.pc

%files -n python3-isomd5sum
%{python3_sitearch}/*.so

%files help
%{_mandir}/man1/*

%changelog
* Thu Oct 29 2020 wangchen <wangchen137@huawei.com> - 1:1.2.3-5
- Remove python2

* Mon Oct 14 2019 openEuler Buildteam <buildteam@openeuler.org> - 1:1.2.3-4
- Package init
