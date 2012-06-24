
#%%define	snap	20030908.0723
%define		pre		pre3

Summary:	Dia - a GTK+ based diagram creation program
Summary(es):	Programa para dibujo de diagramas
Summary(pl):	Dia - program do tworzenia diagram�w
Summary(pt_BR):	Programa para desenho de diagramas
Summary(ru):	��������� ��� ��������� ��������
Summary(uk):	�������� ��� ��������� Ħ�����
Summary(zh_CN):	����GTK+������ͼ����
Name:		dia
Version:	0.94
Release:	6
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		James Henstridge <james@daa.com.au>
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/0.94/%{name}-%{version}.tar.bz2
# Source0-md5:	63584224912dab49fed8d2cf87ea2d85
## this only for snapshots
##Source0:	http://www.crans.org/~chepelov/dia/snapshots/%{name}-CVS-%(echo %{snap} | tr . -).tar.gz
#Patch0:		dia-state.patch
#Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-locale-names.patch
Patch3:		%{name}-python.patch
Patch4:		%{name}-desktop.patch
Patch5:		%{name}-gcc4.patch
URL:		http://www.gnome.org/projects/dia/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	howl-devel >= 0.9.10
BuildRequires:	intltool >= 0.21
BuildRequires:	libart_lgpl-devel
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.3.9
BuildRequires:	libxslt-devel
BuildRequires:	popt-devel
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-pygtk-devel
Requires:	python-modules >= 2.3
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
#%patch0 -p1
#%patch1 -p1 - obsoleted?
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

mv po/{no,nb}.po

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
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1

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
