%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CFB
Summary:	Crypt::CFB Perl module - encrypt data in Cipher Feedback Mode
Summary(pl):	Modu³ Perla Crypt::CFB - szyfruj±cy dane w trybie Cipher Feedback
Name:		perl-Crypt-CFB
Version:	0.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure Perl implementation of Cipher Feedback Mode for almost arbitrary
block ciphers and cryptographic hash functions.

%description -l pl
Modu³ ten jest czysto perlow± implementacj± Cipher Feedback Mode dla
prawie dowolnych szyfrów blokowych i kryptograficznych funkcji
mieszaj±cych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/CFB.pm
%{_mandir}/man3/*
