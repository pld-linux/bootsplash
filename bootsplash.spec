Summary:	Bootsplash
Summary(pl):	Bootsplash
Name:		bootsplash
Version:	3.0.7
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		-
######		Unknown group!
Vendor:		-
Source0:	ftp://ftp.suse.com/pub/people/stepan/%{name}/rpm-sources/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	d7c7cdab692fb2edc5cf5ebb554f20a1
URL:		http://www.bootsplash.org
BuildRequires:	freetype-devel	>= 2
BuildRequires:	libmng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you have a kernel with bootsplash capability you can use the
bootsplash and control it's behaviour with a set of userspace
utilities.

%description -l pl
- -

%prep
%setup -q

%build
cd Utilities
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT%{_docdir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}

install Documentation/* $RPM_BUILD_ROOT%{_docdir}/%{name}
install Scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}
install Utilities/{fbmngplay,fbresolution,fbtruetype,splash} $RPM_BUILD_ROOT%{_bindir}
install Utilities/*.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}
install Utilities/README.* $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Documentation/README.{bootsplash,kernel,config,themes}
%doc Utilities/README.{fbmngplay,fbtruetype}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
