Summary:	HPGL converter into some vector and raster formats
Summary(pl):	Konwerter z jêzyka HPGL do ró¿nych formatów wektorowych i rastrowych
Name:		hp2xx
Version:	3.4.0
Release:	1
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
License:	GPL
Source0:	ftp://ftp.gnu.org/gnu/hp2xx/%{name}-%{version}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://www.gnu.org/software/hp2xx/hp2xx.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	XFree86-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
hp2xx reads HPGL ASCII source files, interprets them, and converts
them into either another vector-oriented format or one of several
rasterfile formats. Currently, its HPGL parser recognizes a subset of
HPGL/2.

hp2xx can be used as ImageMagick delegate to convert HPGL files.

%description -l pl
hp2xx czyta pliki ¼ród³owe HPGL, interpretuje i konwertuje do innego
formatu wektorowego lub którego¶ z formatów rastrowych. Aktualnie
parser HPGL rozpoznaje podzbiór HPGL/2.

hp2xx mo¿e byæ u¿ywany przez ImageMagick do konwersji plików HPGL.

%prep
%setup -q
%patch -p1

%build
%{__make} OPT="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf CHANGES README TODO doc/{changes,hp_cmds.lst}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
