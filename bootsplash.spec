# TODO:
# - place somewhere info that distkernel support only 16bit splashes (thnx Tomasz Grobelny)
#
Summary:	Bootsplash - graphical boot process for Linux
Summary(de.UTF-8):	Bootsplash - graphischer System Start
Summary(pl.UTF-8):	Bootsplash - graficzny proces startu systemu dla Linuksa
Name:		bootsplash
Version:	3.2
Release:	5
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
BuildRequires:	rpmbuild(macros) >= 1.268
Requires(post,preun):	/sbin/chkconfig
Suggests:	bootsplash-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
When you have a kernel with bootsplash capability you can use the
bootsplash and control its behaviour with this set of userspace
utilities.

%description -l de.UTF-8
Wenn du einen Kernel mit der bootsplash Option hast, kannst du diese
mit diesen Programmen steuern.

%description -l pl.UTF-8
Mając jądro z opcją bootsplash można uzyskać graficzny ekran podczas
startu systemu i sterować jego zachowaniem przy użyciu tego zbioru
narzędzi przestrzeni użytkownika.

%prep
%setup -q
%patch0 -p1
rm -f Utilities/splash.o

%build
%{__make} -C Utilities \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/freetype2 -DDEFAULT_FONTNAME=\\\"%{_datadir}/%{name}/luxisri.ttf\\\"" \
	STRIP=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_sysconfdir}/bootsplash/themes} \
	 $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig}

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

%post
/sbin/chkconfig --add bootsplash

%preun
if [ "$1" = "0" ]; then
	%service bootsplash stop
	/sbin/chkconfig --del bootsplash
fi

%files
%defattr(644,root,root,755)
%doc {Documentation,Utilities}/README.*
%attr(755,root,root) %{_bindir}/*
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/bootsplash
%attr(754,root,root) /etc/rc.d/init.d/bootsplash
%{_datadir}/%{name}
%dir %{_sysconfdir}/bootsplash
%dir %{_sysconfdir}/bootsplash/themes
