# TODO: system littlefs?
Summary:	FUSE wrapper that puts the littlefs in user-space
Summary(pl.UTF-8):	Obudowanie FUSE umieszczające littlefs w przestrzeni użytkownika
Name:		littlefs-fuse
Version:	2.7.6
Release:	1
License:	BSD
Group:		Applications/System
#Source0Download: https://github.com/littlefs-project/littlefs-fuse/releases
Source0:	https://github.com/littlefs-project/littlefs-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	af5362106bce17f25e1b849b158a1cf3
URL:		https://github.com/littlefs-project/littlefs-fuse
BuildRequires:	libfuse-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project allows you to mount littlefs directly in a host PC.

%description -l pl.UTF-8
Ten projekt pozwala zamontować bezpośrednio littlefs na maszynie PC.

%prep
%setup -q

%{__sed} -i -e 's/-Os/ /' Makefile

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}" \
	LFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -Dp lfs $RPM_BUILD_ROOT%{_bindir}/lfs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.md README.md
%attr(755,root,root) %{_bindir}/lfs
