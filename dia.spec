Summary:	Dia - a gtk+ based diagram creation program
Summary(pl):	Dia - program do tworzenie diagramów
Name:		dia
Version:	0.41
Release:	3
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Vendor:		Alexander Larsson <alla@lysator.liu.se>
Source0:	http://www.lysator.liu.se/~alla/dia/files/%{name}-%{version}.tar.gz
Source1:	dia.wmconfig
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	XFree86-devel
BuildPrereq:	libxml-devel
BuildPrereq:	zlib-devel
BuildPrereq:	imlib-devel
BuildPrereq:	gettext
Requires:	gtk+ >= 1.2.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Dia is a program designed to be much like the Windows program 'Visio'. It
can be used to draw different kind of diagrams. In this first version there
is support for UML static structure diagrams (class diagrams) and Network
diagrams. It can currently load and save diagrams to a custom fileformat and
export to postscript.

%description -l pl
Dia jest programem zaprojektowanym tak by byæ podobnym do programu 'Visio'
znanego z Windows. Dia mo¿e byæ u¿ywany do rysowania ró¿nego rodzaju diagramów.
W tej wersji znajduje siê wsparcie dla diagramów o statycznej strukturze UML
(diagramy klasowe) i dla diagramów sieciowych. Aktualnie mo¿e on ³adowaæ
i zapisywaæ diagramy we w³asnym formacie oraz eksportowaæ je do postscriptu.

%prep
%setup -q

%build
%configure \
	--prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/dia/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/dia
%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so*
%attr(755,root,root) %{_libdir}/dia/lib*.la
