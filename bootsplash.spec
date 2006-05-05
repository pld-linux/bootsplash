#
# TODO:
# - place somewhere info that distkernel support only 16bit splashes (thnx Tomasz Grobelny)
#
Summary:	Bootsplash - graphical boot process for Linux
Summary(de):	Bootsplash - graphischer System Start
Summary(pl):	Bootsplash - graficzny proces startu systemu dla Linuksa
Name:		bootsplash
Version:	3.2
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.bootsplash.de/files/splashutils/%{name}-%{version}.tar.bz2
# Source0-md5:	b74c104372fd182d0442b3ed63210e29
Source1:	%{name}.script
Source2:	%{name}-bootanim.script
Source3:	%{name}.sysconfig
Source4:	%{name}.init
Patch0:		%{name}-3.2_makefile_libmng.patch
URL:		http://www.bootsplash.org/
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	libmng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
When you have a kernel with bootsplash capability you can use the
bootsplash and control its behaviour with this set of userspace
utilities.

%description -l de
Wenn du einen Kernel mit der bootsplash Option hast, kannst du diese
mit diesen Programmen steuern.

%description -l pl
Maj�c j�dro z opcj� bootsplash mo�na uzyska� graficzny ekran podczas
startu systemu i sterowa� jego zachowaniem przy u�yciu tego zbioru
narz�dzi przestrzeni u�ytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C Utilities \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/freetype2 -DDEFAULT_FONTNAME=\\\"%{_datadir}/%{name}/luxisri.ttf\\\"" \
	STRIP=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_sysconfdir}/{bootsplash/themes,rc.d/init.d,sysconfig}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/splash
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/bootanim
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/bootsplash
install %{SOURCE4} $RPM_BUILD_ROOT/etc/rc.d/init.d/bootsplash
install Scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install Utilities/splash $RPM_BUILD_ROOT%{_bindir}/splash.bin
install Utilities/{fbmngplay,fbresolution,fbtruetype} $RPM_BUILD_ROOT%{_bindir}
install Utilities/*.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Documentation,Utilities}/README.*
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bootsplash
%attr(754,root,root) /etc/rc.d/init.d/bootsplash
%{_datadir}/%{name}
%dir %{_sysconfdir}/bootsplash
%dir %{_sysconfdir}/bootsplash/themes
