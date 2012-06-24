Summary:	Dia - a gtk+ based diagram creation program
Summary(pl):	Dia - program do tworzenie diagram�w
Name:		dia
Version:	0.41
Release:	4
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Vendor:		Alexander Larsson <alla@lysator.liu.se>
Source0:	http://www.lysator.liu.se/~alla/dia/files/%{name}-%{version}.tar.gz
Source1:	dia.desktop
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	libxml-devel
BuildRequires:	zlib-devel
BuildRequires:	imlib-devel
BuildRequires:	gettext
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
Dia jest programem zaprojektowanym tak by by� podobnym do programu 'Visio'
znanego z Windows. Dia mo�e by� u�ywany do rysowania r�nego rodzaju diagram�w.
W tej wersji znajduje si� wsparcie dla diagram�w o statycznej strukturze UML
(diagramy klasowe) i dla diagram�w sieciowych. Aktualnie mo�e on �adowa�
i zapisywa� diagramy we w�asnym formacie oraz eksportowa� je do postscriptu.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/applnk/Graphics

make install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Graphics

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/dia/lib*.so.*.*

%find_lang %{name}

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
/etc/X11/applnk/Graphics/dia.desktop
%attr(755,root,root) %{_bindir}/dia
%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so*
%attr(755,root,root) %{_libdir}/dia/lib*.la
