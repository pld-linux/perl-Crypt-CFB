%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CFB
Summary:	Crypt::CFB Perl module - encrypt data in Cipher Feedback Mode
Summary(pl.UTF-8):	Moduł Perla Crypt::CFB - szyfrujący dane w trybie Cipher Feedback
Name:		perl-Crypt-CFB
Version:	0.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	861efb6dc6da228458faeb1415fd47d2
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pure Perl implementation of Cipher Feedback Mode for almost arbitrary
block ciphers and cryptographic hash functions.

%description -l pl.UTF-8
Moduł ten jest czysto perlową implementacją Cipher Feedback Mode dla
prawie dowolnych szyfrów blokowych i kryptograficznych funkcji
mieszających.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Crypt/CFB.pm
%{_mandir}/man3/*
