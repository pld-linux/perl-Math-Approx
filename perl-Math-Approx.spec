%define	pdir	Math
%define	pnam	Approx
%include	/usr/lib/rpm/macros.perl
Summary:	Math-Approx perl module
Summary(pl):	Modu³ perla Math-Approx
Name:		perl-Math-Approx
Version:	0.200
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Math-Matrix
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-Approx perl module.

%description -l pl
Modu³ perla Math-Approx.

%prep
%setup -q -n Math-Approx-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Math/Approx.pm
%{_mandir}/man3/*
