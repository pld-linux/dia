Summary:	Dia - a gtk+ based diagram creation program
Summary(pl):	Dia - program do tworzenia diagram�w
Name:		dia
Version:	0.88.1
Release:	3
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		James Henstridge <james@daa.com.au>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/dia/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	libxml-devel
BuildRequires:	popt-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
Requires:	libxml >= 1.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11/GNOME

%description
Dia is a program designed to be much like the Windows program 'Visio'.
It can be used to draw different kind of diagrams. In this first
version there is support for UML static structure diagrams (class
diagrams) and Network diagrams. It can currently load and save
diagrams to a custom fileformat and export to postscript.

%description -l pl
Dia jest programem zaprojektowanym tak by by� podobnym do programu
'Visio' znanego z Windows. Dia mo�e by� u�ywany do rysowania r�nego
rodzaju diagram�w. W tej wersji znajduje si� wsparcie dla diagram�w o
statycznej strukturze UML (diagramy klasowe) i dla diagram�w
sieciowych. Aktualnie mo�e on �adowa� i zapisywa� diagramy we w�asnym
formacie oraz eksportowa� je do postscriptu.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
aclocal
autoconf
autoheader
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Graphics

gzip -9nf AUTHORS NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/Graphics/dia.desktop
%attr(755,root,root) %{_bindir}/*
#%{_sysconfdir}/CORBA/servers/*
%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so
%attr(755,root,root) %{_libdir}/dia/lib*.la
%{_datadir}/dia
%{_pixmapsdir}/*
%{_datadir}/mime-info/*
%{_mandir}/man1/*
