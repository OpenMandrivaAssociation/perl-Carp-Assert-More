%define upstream_name	 Carp-Assert-More
%define upstream_version 1.14

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.14
Release:	2

Summary:	Convenience wrappers around Carp::Assert module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/P/PE/PETDANCE/Carp-Assert-More-1.14.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(Carp::Assert)
BuildRequires:  perl(Test::Exception)
BuildArch:	noarch

%description
Carp::Assert::More is a set of wrappers around the Carp::Assert functions 
to make the habit of writing assertions even easier.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Carp
%{_mandir}/man3/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.120.0-2mdv2011.0
+ Revision: 680715
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.120.0-1mdv2011.0
+ Revision: 405957
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.12-5mdv2009.0
+ Revision: 255478
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-3mdv2008.1
+ Revision: 136890
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Nov 01 2006 Michael Scherer <misc@mandriva.org> 1.12-2mdv2007.0
+ Revision: 74870
- Rebuild for new extension
- Import perl-Carp-Assert-More


