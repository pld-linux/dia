
%define snap 20021002.0723

Summary:	Dia - a gtk+ based diagram creation program
Summary(es):	Programa para dibujo de diagramas
Summary(pl):	Dia - program do tworzenia diagram�w
Summary(pt_BR):	Programa para desenho de diagramas
Summary(ru):	��������� ��� ��������� ��������
Summary(uk):	�������� ��� ��������� Ħ�����
Summary(zh_CN):	����gtk+������ͼ����
Name:		dia
Version:	0.90
Release:	1.%{snap}
Epoch:		1
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		James Henstridge <james@daa.com.au>
# this for final releases
#Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/dia/%{version}/%{name}-%{version}.tar.gz
# this only for snapshots
Source0:	http://www.crans.org/~chepelov/dia/snapshots/%{name}-CVS-%(echo %snap | sed 's/\./-/').tar.gz
URL:		http://www.lysator.liu.se/~alla/dia/dia.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	libgnomeui-devel
BuildRequires:	libxslt-devel
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
#%setup -q
%setup -q -n dia-cvs-snapshot

%build
./autogen.sh
%configure \
	--enable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Graphics

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/dia
%attr(755,root,root) %{_libdir}/dia/lib*.so
%attr(755,root,root) %{_libdir}/dia/lib*.la

%{_mandir}/man1/*

%{_applnkdir}/Graphics/dia.desktop
%{_datadir}/dia
%{_datadir}/mime-info/*
%{_pixmapsdir}/*
