Summary:	French dictionary for aspell
Summary(fr):	Il s'agit de deux dictionnaires fran�ais pour aspell
Summary(pl):	Francuski s�ownik dla aspella
Name:		aspell-fr
Version:	0.50
%define	subv	3
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/fr/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
French dictionary (i.e. word list) for aspell.

%description -l fr
Il s'agit de deux dictionnaires fran�ais pour aspell.

%description -l pl
Francuski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
