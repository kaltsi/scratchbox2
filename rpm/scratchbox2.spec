Summary: 	Scratchbox2 crosscompiling environment
License: 	LGPL
URL:		https://github.com/mer-packages/scratchbox2
Name: 		scratchbox2
Version:	2.3.90
Release:	14
Source: 	%{name}-%{version}.tar.gz
Prefix: 	/usr
Group: 		Development/Tools
ExclusiveArch:	%{ix86}
BuildRequires:	make
BuildRequires:	autoconf
Requires:	fakeroot
Requires:	libsb2 = %{version}-%{release}

%description
Scratchbox2 crosscompiling environment

%package -n libsb2
Summary: Scratchbox2 preload library
Group:   Development/Tools

%description -n libsb2
Scratchbox2 preload library.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
make

%install
make install prefix=%{buildroot}/usr sysconfdir=%{buildroot}%{_sysconfdir}

%files
%defattr(-,root,root)
%{_bindir}/sb2*
%{_datadir}/scratchbox2/*
%config %{_sysconfdir}/bash_completion.d/sb2.bash
%doc %attr(0444,root,root) /usr/share/man/man1/*
%doc %attr(0444,root,root) /usr/share/man/man7/*

%files -n libsb2
%defattr(-,root,root)
%{_libdir}/libsb2/*
%ifarch x86_64
/usr/lib32/libsb2/*
%endif
