Summary:	Dia - a GTK+ based diagram creation program
Summary(es):	Programa para dibujo de diagramas
Summary(pl):	Dia - program do tworzenia diagram�w
Summary(pt_BR):	Programa para desenho de diagramas
Summary(ru):	��������� ��� ��������� ��������
Summary(uk):	�������� ��� ��������� Ħ�����
Summary(zh_CN):	����GTK+������ͼ����
Name:		dia
Version:	0.95
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/dia/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	d319921a91d4600df3578a4a64416393
Patch0:		%{name}-python.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-gcc4.patch
URL:		http://www.gnome.org/projects/dia/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-utils
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libart_lgpl-devel >= 2.0
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

%description -l es
Programa proyectado para que fuera semejante al Visio. Puede usarse
para realizar diagramas de diferentes tipos e incluye soporte para
diagramas de estructuras UML est�ticas (diagramas de clase), modelos
de entidades y relacionamiento y diagramas de red. El programa Dia usa
un formato propio de archivo y tambi�n puede usar el formato .xml, as�
como tambi�n puede exportar para PostScript(TM).

%description -l pl
Dia jest programem zaprojektowanym tak by by� podobnym do programu
'Visio' znanego z Windows. Dia mo�e by� u�ywany do rysowania r�nego
rodzaju diagram�w. W tej wersji znajduje si� wsparcie dla diagram�w o
statycznej strukturze UML (diagramy klasowe) i dla diagram�w
sieciowych. Aktualnie mo�e on �adowa� i zapisywa� diagramy we w�asnym
formacie oraz eksportowa� je do postscriptu.

%description -l pt_BR
Programa projetado para ser semelhante ao Visio. Pode ser usado para
desenhar diferentes tipos de diagramas e inclui suporte a diagramas de
estruturas UML est�ticas (diagramas de classe), modelo de entidades e
relacionamento e diagramas de rede. O Dia usa um formato pr�prio de
arquivo e pode tamb�m usar o formato .xml, bem como exportar para
PostScript(TM).

%description -l ru
��������� Dia ����������� ��� ������������ Visio ��� Windows(TM). Dia
����� ������������ ��� ��������� ��������� ����� ��������, ���
�������� ��������� ����������� ����������� �������� UML (��������
�������), ������������� ��������� �������� � ������� ��������. Dia
����� ��������� � ��������� ��������� � ����������� ������� � �
������� .xml � ����� �������������� �� � PostScript(TM).

%description -l uk
�������� Dia ���������� �� ������������ Visio ��� Windows(TM). Dia
����� ��������������� ��� ��������� Ҧ�����Φ���� ��Ц� Ħ�����, ����
������� Ц������� ����������� ��������� Ħ����� UML (Ħ����� ���Ӧ�),
����������� צ������� ��'��Ԧ� �� ��������� Ħ�����. Dia ����
������������� �� ���Ҧ���� �������� � �������� �����Ԧ �� �����Ԧ .xml
� ����� ������������ �� � PostScript(TM).

%prep
%setup -q
%patch0 -p1
%patch1 -p1
#%patch2 -p1 -- needs check

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--enable-gnome \
	--with-python

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_desktopdir}

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

%{_mandir}/man1/*

%{_datadir}/dia
%{_desktopdir}/dia.desktop
%{_pixmapsdir}/*
