
%bcond_without	themes		# build without themes

Summary:	Bootsplash - graphical boot process for Linux
Summary(pl):	Bootsplash - graficzny proces startu systemu dla Linuksa
Name:		bootsplash
Version:	3.0.7
Release:	0.5
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.suse.com/pub/people/stepan/%{name}/rpm-sources/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d7c7cdab692fb2edc5cf5ebb554f20a1
Source1:	%{name}.script
Source2:	%{name}-bootanim.script
Source3:	%{name}.sysconfig
Source4:	%{name}-theme-darkblue-1.2.tar.gz
# Source4-md5:	a5b64219f284ff772a4f3ebcd4f2bc34
Patch0:		%{name}-freetype-includes.patch
URL:		http://www.bootsplash.org/
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	libmng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	/bin

%description
When you have a kernel with bootsplash capability you can use the
bootsplash and control it's behaviour with this set of userspace
utilities.

%description -l pl
Maj±c j±dro z opcj± bootsplash mo¿na uzyskaæ graficzny ekran podczas
startu systemu i sterowaæ jego zachowaniem przy u¿yciu tego zbioru
narzêdzi przestrzeni u¿ytkownika.

%if %{with themes}
%package theme-darkblue
Summary:	Bootsplash - darkblue theme
Summary(pl):	Bootsplash - motyw darkblue
Group:		Themes
Requires:	bootsplash

%description theme-darkblue
Darkblue theme for bootsplash.

%description theme-darkblue -l pl
Motyw darkblue do bootsplash.

%endif

%prep
%setup -q %{?with_themes:-a4}
%patch0 -p1

%build
%{__make} -C Utilities \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -I/usr/include/freetype2 -DDEFAULT_FONTNAME=\\\"%{_datadir}/%{name}/luxisri.ttf\\\"" \
	STRIP=true

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},/etc/{bootsplash/themes,sysconfig}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/splash
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/bootanim
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/bootsplash
install Scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install Utilities/splash $RPM_BUILD_ROOT%{_bindir}/splash.bin
install Utilities/{fbmngplay,fbresolution,fbtruetype} $RPM_BUILD_ROOT%{_bindir}
install Utilities/*.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}
%if %{with themes}
#darkblue theme
THEME_DIR=$RPM_BUILD_ROOT/etc/bootsplash/themes/darkblue
install -d $THEME_DIR{,/animations,/config,/images}
install darkblue/animations/*.mng $THEME_DIR/animations
install darkblue/config/*.cfg $THEME_DIR/config
install darkblue/images/*.jpeg $THEME_DIR/images
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Documentation,Utilities}/README.*
%attr(755,root,root) %{_bindir}/*
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/bootsplash
%{_datadir}/%{name}

%files theme-darkblue
%defattr(644,root,root,755)
/etc/bootsplash/themes/darkblue/animations/*
%config(noreplace) %verify(not md5 size mtime)/etc/bootsplash/themes/darkblue/config/*
/etc/bootsplash/themes/darkblue/images/*
