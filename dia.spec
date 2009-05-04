Summary:	Dia - a GTK+ based diagram creation program
Summary(es.UTF-8):	Programa para dibujo de diagramas
Summary(hu.UTF-8):	Dia - gtk alapú diagram-készítő program
Summary(pl.UTF-8):	Dia - program do tworzenia diagramów
Summary(pt_BR.UTF-8):	Programa para desenho de diagramas
Summary(ru.UTF-8):	Программа для рисования диаграмм
Summary(uk.UTF-8):	Програма для малювання діаграм
Summary(zh_CN.UTF-8):	基于GTK+的流程图程序
Name:		dia
Version:	0.96.1
Release:	6
Epoch:		1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/dia/0.96/%{name}-%{version}.tar.bz2
# Source0-md5:	7b81b22baa2df55efe4845865dddc7b6
Source1:	http://dia-installer.de/shapes/central_data_processing/central_data_processing.zip
# Source1-md5:	103865b35609d2a0f8a0e034c49cf130
Source2:	http://dia-installer.de/shapes/chemistry_lab/chemistry_lab.zip
# Source2-md5:	988e4c992f0ca4452c9eb8e224b73adf
Source3:	http://dia-installer.de/shapes/cmos/cmos.zip
# Source3-md5:	65f319c9c0c15d0691f9e97fd034c005
Source4:	http://dia-installer.de/shapes/digital/digital.zip
# Source4-md5:	8eef8562b618254fc5ebd4ac3f4f15ed
Source5:	http://dia-installer.de/shapes/edpc/edpc.zip
# Source5-md5:	3cc6f6eb886715ea7ce1a09bd3a46a5e
Source6:	http://dia-installer.de/shapes/electronic/electronic.zip
# Source6-md5:	ddeca421f725af66be41f14ab170b2b8
Source7:	http://dia-installer.de/shapes/lst/lst.zip
# Source7-md5:	84d216457305ae53eb1635f6abaa4368
Source8:	http://dia-installer.de/shapes/optics/optics.zip
# Source8-md5:	6c2bb1ffa6229b832e2d24fb1fd927c9
Source9:	http://dia-installer.de/shapes/Racks/Racks.zip
# Source9-md5:	5ca48da8899b28ed266e21ba522d1e64
Source10:	http://dia-installer.de/shapes/renewable_energy/renewable_energy.zip
# Source10-md5:	13e7e934ab87b924101faaf56414ad00
Source11:	http://dia-installer.de/shapes/scenegraph/scenegraph.zip
# Source11-md5:	2bca8efa9bae10c13968ebacc9f1a00b
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
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%description -l hu.UTF-8
Dia egy program, amely a windows-os 'Visio' programhoz hasonló.
Különféle fajta diagramokat rajzolhatsz. Ebben a verzióban már van
lehetőség UML struktúra diagramok (osztálydiagramok) és Network
diagramok készítésére. Többféle fájlformátumot ismer, és képes
postscript-be exportálni.

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

%{__sed} -i -e s#sr\@Latn#sr\@latin# configure.in
mv -f po/sr\@{Latn,latin}.po

%build
%{__intltoolize}
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

unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE1}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE2}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE3}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE4}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE5}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE6}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE7}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE8}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE9}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE10}
unzip -n -d $RPM_BUILD_ROOT%{_datadir}/%{name} %{SOURCE11}

# Conflicts with Assorted/square.shape
sed -i "s@Square@Square2@" $RPM_BUILD_ROOT%{_datadir}/%{name}/shapes/chemistry_lab/square.shape

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
