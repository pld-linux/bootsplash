Summary:	Bootsplash - graphical boot process for Linux
Summary(pl):	Bootsplash - graficzny proces startu systemu dla Linuksa
Name:		bootsplash
Version:	3.0.7
Release:	0.2
Epoch:		0
License:	GPL v2
Group:		Applications/System
Source0:	ftp://ftp.suse.com/pub/people/stepan/%{name}/rpm-sources/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d7c7cdab692fb2edc5cf5ebb554f20a1
Source1:	%{name}.script
Patch0:		%{name}-freetype-includes.patch
URL:		http://www.bootsplash.org/
BuildRequires:	freetype-devel >= 2.1
BuildRequires:	libmng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you have a kernel with bootsplash capability you can use the
bootsplash and control it's behaviour with this set of userspace
utilities.

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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},/bin}

install %{SOURCE1} $RPM_BUILD_ROOT/bin/splash
install Scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install Utilities/splash $RPM_BUILD_ROOT%{_bindir}/splash.bin
install Utilities/{fbmngplay,fbresolution,fbtruetype} $RPM_BUILD_ROOT%{_bindir}
install Utilities/*.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Documentation,Utilities}/README.*
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
