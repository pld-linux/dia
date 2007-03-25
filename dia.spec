Summary:	Dia - a GTK+ based diagram creation program
Summary(es.UTF-8):	Programa para dibujo de diagramas
Summary(pl.UTF-8):	Dia - program do tworzenia diagramów
Summary(pt_BR.UTF-8):	Programa para desenho de diagramas
Summary(ru.UTF-8):	Программа для рисования диаграмм
Summary(uk.UTF-8):	Програма для малювання діаграм
Summary(zh_CN.UTF-8):	基于GTK+的流程图程序
Name:		dia
Version:	0.96
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/dia/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	0c173dd5f46672efb77952ecbd884bfd
Patch0:		%{name}-python.patch
Patch1:		%{name}-desktop.patch
URL:		http://www.gnome.org/projects/dia/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libart_lgpl-devel >= 2.0
BuildRequires:	libgnomeprint-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.3.9
BuildRequires:	libxslt-devel
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	python-PyXML
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
Requires(post,postun):	desktop-file-utils
Requires:	python-modules >= 1:2.3
Requires:	python-pygtk-gtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dia is a program designed to be much like the Windows program 'Visio'.
It can be used to draw different kind of diagrams. In this first
version there is support for UML static structure diagrams (class
diagrams) and Network diagrams. It can currently load and save
diagrams to a custom fileformat and export to postscript.

%description -l es.UTF-8
Programa proyectado para que fuera semejante al Visio. Puede usarse
para realizar diagramas de diferentes tipos e incluye soporte para
diagramas de estructuras UML estáticas (diagramas de clase), modelos
de entidades y relacionamiento y diagramas de red. El programa Dia usa
un formato propio de archivo y también puede usar el formato .xml, así
como también puede exportar para PostScript(TM).

%description -l pl.UTF-8
Dia jest programem zaprojektowanym tak by być podobnym do programu
'Visio' znanego z Windows. Dia może być używany do rysowania różnego
rodzaju diagramów. W tej wersji znajduje się wsparcie dla diagramów o
statycznej strukturze UML (diagramy klasowe) i dla diagramów
sieciowych. Aktualnie może on ładować i zapisywać diagramy we własnym
formacie oraz eksportować je do postscriptu.

%description -l pt_BR.UTF-8
Programa projetado para ser semelhante ao Visio. Pode ser usado para
desenhar diferentes tipos de diagramas e inclui suporte a diagramas de
estruturas UML estáticas (diagramas de classe), modelo de entidades e
relacionamento e diagramas de rede. O Dia usa um formato próprio de
arquivo e pode também usar o formato .xml, bem como exportar para
PostScript(TM).

%description -l ru.UTF-8
Программа Dia разработана как альтернатива Visio для Windows(TM). Dia
можно использовать для рисования различных типов диаграмм, она
включает поддержку структурных статических диаграмм UML (диаграмм
классов), моделирование отношений объектов и сетевых диаграмм. Dia
может загружать и сохранять диаграммы в собственном формате и в
формате .xml а также экспортировать их в PostScript(TM).

%description -l uk.UTF-8
Програма Dia розроблена як альтернатива Visio для Windows(TM). Dia
можна використовувати для малювання різноманітних типів діаграм, вона
включає підтримку структурних статичних діаграм UML (діаграм класів),
моделювання відношень об'єктів та мережевих діаграм. Dia може
завантажувати та зберігати диаграми у власному форматі та форматі .xml
а також експортувати їх в PostScript(TM).

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%{__sed} -i -e 's|/lib/|/%{_lib}/|' configure
%configure \
	--enable-gnome \
	--with-gnomeprint \
	--with-cairo \
	--with-python \
	--with-xslt-prefix=%{_libdir}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir}

rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so
%{_libdir}/dia/lib*.la
%{_docdir}/dia/*.xml
%dir %{_docdir}/dia
%dir %{_docdir}/dia/graphics
%{_docdir}/dia/graphics/*.png

%{_mandir}/man1/*

%{_datadir}/dia
%{_desktopdir}/dia.desktop
%{_pixmapsdir}/*
