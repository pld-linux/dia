Summary:	Dia - a gtk+ based diagram creation program
Summary(pl):	Dia - program do tworzenie diagramów
Name:		dia
Version:	0.86
Release:	2
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Vendor:		James Henstridge <james@daa.com.au>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/dia/%{name}-%{version}.tar.gz
Patch0:		%{name}-automake.patch
Patch1:		dia-build-patch.patch
Patch2:		dia-build-with-bonobo.patch
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel >= 1.2.0
BuildRequires:	gnome-print-devel
BuildRequires:	libxml-devel
Requires:	libxml >= 1.8.7
BuildRequires:	popt-devel
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
Dia jest programem zaprojektowanym tak by byæ podobnym do programu
'Visio' znanego z Windows. Dia mo¿e byæ u¿ywany do rysowania ró¿nego
rodzaju diagramów. W tej wersji znajduje siê wsparcie dla diagramów o
statycznej strukturze UML (diagramy klasowe) i dla diagramów
sieciowych. Aktualnie mo¿e on ³adowaæ i zapisywaæ diagramy we w³asnym
formacie oraz eksportowaæ je do postscriptu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
automake
gettextize --copy --force
%configure \
	--enable-gnome \
	--enable-gnome-print \
	--enable-bonobo
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
%{_sysconfdir}/CORBA/servers/*
%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so
%attr(755,root,root) %{_libdir}/dia/lib*.la
%{_datadir}/dia
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/oaf/*
%{_mandir}/man1/*
