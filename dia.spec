Summary:     Dia - a gtk+ based diagram creation program
Name:        dia
Version:     0.20
Release:     1
Copyright:   GPL
Group:       X11/Applications/Graphics
Vendor:      Alexander Larsson <alla@lysator.liu.se>
Source0:     http://www.lysator.liu.se/~alla/dia/%{name}-%{version}.tar.gz
Source1:     %{name}.wmconfig
URL:         http://www.lysator.liu.se/~alla/dia/dia.html
Requires:    gtk+ >= 1.2.1
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Dia is a program designed to be much like the Windows program 'Visio'. It
can be used to draw different kind of diagrams. In this first version there
is support for UML static structure diagrams (class diagrams) and Network
diagrams. It can currently load and save diagrams to a custom fileformat and
export to postscript.

%prep
%setup -q

%build
./configure --prefix=/usr/X11R6
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/wmconfig

make install prefix=$RPM_BUILD_ROOT/usr/X11R6

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

strip $RPM_BUILD_ROOT/usr/X11R6/{bin/*,lib/lib*.so.*.*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS NEWS README TODO
%attr(755, root, root) /usr/X11R6/bin/dia
%dir /usr/X11R6/lib/dia
%attr(755, root, root) /usr/X11R6/lib/dia/lib*.so.*

%changelog
* Sun Aug 30 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.20-1]
- first release in rpm package.
