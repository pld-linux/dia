Summary:	Dia - a gtk+ based diagram creation program
Summary(pl):	Dia - program do tworzenie diagramów
Name:		dia
Version:	0.85
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Vendor:		James Henstridge <james@daa.com.au>
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/dia/%{name}-%{version}.tar.gz
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	imlib-devel
BuildRequires:	gettext-devel
Requires:	gtk+ >= 1.2.0
Requires: libxml >= 1.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Graphics

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/dia/lib*.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%find_lang %{name}

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%{_applnkdir}/Graphics/dia.desktop
%attr(755,root,root) %{_bindir}/dia
%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so
%attr(755,root,root) %{_libdir}/dia/lib*.la
%{_datadir}/dia
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
