Summary:	HPGL converter into some vector and raster formats
Summary(pl):	Konwerter z jêzyka HPGL do ró¿nych formatów wektorowych i rastrowych
Name:		hp2xx
Version:	3.4.4
Release:	2
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.gnu.org/gnu/hp2xx/%{name}-%{version}.tar.gz
# Source0-md5:	18808580d24b7caf2c4c7045c093329f
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-emf-hack.patch
URL:		http://www.gnu.org/software/hp2xx/hp2xx.html
BuildRequires:	XFree86-devel
BuildRequires:	libEMF-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pdflib-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	OPT="%{rpmcflags}" \
	ALL_LIBS="-L/usr/X11R6/%{_lib} -lX11 -lm"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES README TODO doc/{changes,hp_cmds.lst}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*.info*
